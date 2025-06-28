from typing import Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.db.models.lectures import Lecture


def get_random_lecture(db: Session) -> Optional[Lecture]:
    return (
        db.query(Lecture)
        .filter(Lecture.was_watched.is_(True))  # campo novo
        .order_by(func.random())
        .first()
    )
