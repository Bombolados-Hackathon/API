from typing import Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.db.models.lectures import Lecture


def get_random_lecture(
    db: Session,
    subject_id: int,                      # ← novo parâmetro
) -> Optional[Lecture]:
    """
    Retorna uma Lecture aleatória já assistida (`was_watched = True`)
    que pertença ao Subject indicado.

    Args:
        db: sessão SQLAlchemy aberta.
        subject_id: ID da disciplina (subjects.id).

    Returns:
        Lecture ou None se não houver registros que satisfaçam o filtro.
    """
    return (
        db.query(Lecture)
        .filter(
            Lecture.id_subject == subject_id,   # ← novo filtro
            Lecture.was_watched.is_(True),
        )
        .order_by(func.random())
        .first()
    )
