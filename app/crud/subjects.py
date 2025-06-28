from typing import List
from sqlalchemy.orm import Session

from app.db.models.subject_user import SubjectUser   # ponte many-to-many


def get_subject_ids_by_user(db: Session, user_id: int):
    """
    Retorna uma lista de IDs de subjects associados ao user informado.

    Args:
        db: sessão SQLAlchemy.
        user_id: valor de users.id.

    Returns:
        List[int]: IDs únicos das disciplinas encontradas.
    """
    rows = (
        db.query(SubjectUser.id_subject)
        .filter(SubjectUser.id_user == user_id)
        .distinct()                 # evita duplicatas
        .all()                      # devolve List[Tuple[int]]
    )
    return [row[0] for row in rows]
