import re
from semantic_kernel import Kernel
from semantic_kernel.kernel import KernelArguments
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion
from ..db.models.tf_answers import TFAnswer
from ..db.models.mcq_options import MCQOption
from ..db.models.matching_pairs import MatchingPair
from ..db.models.questions import Question
from ..db.models.questions import QuestionType
from ..db.models.lectures import Lecture  #
from .consts import tf_prompt, mcq_prompt, matching_prompt


class Ollama:
    def __init__(self, lecture: Lecture, task_id: int, model="deepseek-r1:14b"):
        self.lecture = lecture
        self.task_id = task_id
        self.kernel = Kernel()
        chat_completion = OllamaChatCompletion(ai_model_id=model)
        self.kernel.add_service(chat_completion)

    async def _invoke_prompt(self, prompt: str) -> str:
        func = self.kernel.add_function(plugin_name="default", prompt=prompt, function_name="generate_question")
        args = KernelArguments(content=self.lecture.raw_text)
        result = await func.invoke(self.kernel, args)
        output = re.sub(r"<think>.*?</think>", '', str(result), flags=re.DOTALL).strip()
        return output

    async def generate_tf_question(self):
        output = await self._invoke_prompt(tf_prompt)
        lines = output.strip().split("\n")
        prompt_text = lines[0].replace("Pergunta: ", "")
        answer_text = lines[1].split(":")[-1].strip().lower() in ["verdadeiro", "true"]

        question = Question(question_type=QuestionType.true_false, title=prompt_text, task_id=self.task_id)
        tf_answer = TFAnswer(correct=answer_text)

        return question, tf_answer

    async def generate_mcq_question(self):
        output = await self._invoke_prompt(mcq_prompt)
        lines = output.strip().split("\n")
        prompt_text = lines[0].replace("Pergunta: ", "")
        options = []

        for i in range(1, 5):
            text = lines[i][3:].strip()  # remove "A) ", "B) ", ...
            options.append(text)
        correct_letter = lines[5].split(":")[-1].strip().upper()

        question = Question(question_type=QuestionType.multiple_choice, title=prompt_text, task_id=self.task_id)
        mcq_options = []
        for idx, opt_text in enumerate(options):
            mcq_options.append(
                MCQOption(
                    option_text=opt_text,
                    is_correct=(chr(65 + idx) == correct_letter)
                )
            )
        return question, mcq_options

    async def generate_matching_question(self):
        output = await self._invoke_prompt(matching_prompt)
        lines = output.strip().split("\n")
        prompt_text = lines[0].replace("Pergunta: ", "")
        pairs = []
        for line in lines[1:]:
            if " - " in line:
                left, right = line.split(" - ")
                pairs.append((left.strip(" 123456789. "), right.strip()))

        question = Question(question_type=QuestionType.matching, title=prompt_text, task_id=self.task_id)
        matching_pairs = [
            MatchingPair(left_item=left, right_item=right)
            for left, right in pairs
        ]
        return question, matching_pairs
