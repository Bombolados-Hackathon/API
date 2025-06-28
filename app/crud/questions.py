from sqlalchemy.orm import Session

from app.helper import get_random_question_type
from app.services.ollama import Ollama
from app.crud.lectures import get_random_lecture


async def create_questions(db: Session, task_id: int, user_id: int) -> None:
    for i in range(3):
        lecture = get_random_lecture(db, user_id)
        ollama = Ollama(lecture, task_id)
        question_type = get_random_question_type()

        if question_type == 'multiple_choice':
            question, mcq_options = await ollama.generate_mcq_question()
            db.add(question)
            for mcq_option in mcq_options:
                mcq_option.id_question = question.id
            db.add_all(mcq_options)
            db.commit()
            db.refresh(question)
            for mcq_option in mcq_options:
                db.refresh(mcq_option)
        elif question_type == 'true_false':
            question, tf_answer = await ollama.generate_tf_question()
            db.add(question)
            db.commit()
            db.refresh(question)
            tf_answer.id_question = question.id
            db.add(tf_answer)
            db.commit()
            db.refresh(tf_answer)
        elif question_type == 'matching':
            question, matching_pairs = await ollama.generate_matching_question()
            db.add(question)
            for matching_pair in matching_pairs:
                matching_pair.id_question = question.id
            db.add_all(matching_pairs)
            db.commit()
            db.refresh(question)
            for matching_pair in matching_pairs:
                db.refresh(matching_pair)
        else:
            raise ValueError(f"Unknown question type: {question_type}")

