from sqlalchemy.orm import Session

from app.helper import get_random_question_type
from app.services.ollama import Ollama
from app.crud.lectures import get_random_lecture


def create_questions(db: Session, task_id: int, user_id: int) -> None:
    for i in range(7):
        lecture = get_random_lecture(db, user_id)
        ollama = Ollama(lecture)
        question_type = get_random_question_type()

        if question_type == 'multiple_choice':
            question, mcq_options = ollama.generate_mcq_question()
            db.add(question)
            db.add_all(mcq_options)
            db.commit()
            db.refresh(question)
            db.refresh(mcq_options)
        elif question_type == 'true_false':
            question, tf_answer = ollama.generate_tf_question()
            db.add(question)
            db.add(tf_answer)
            db.commit()
            db.refresh(question)
            db.refresh(tf_answer)
        elif question_type == 'matching':
            question, matching_pairs = ollama.generate_matching_question()
            db.add(question)
            db.add_all(matching_pairs)
            db.commit()
            db.refresh(question)
            db.refresh(matching_pairs)
        else:
            raise ValueError(f"Unknown question type: {question_type}")

