from typing import List, Optional
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


def get_accuracy_by_user_and_subject(db: Session, user_id: int, subject_id: int) -> Optional[float]:
    """
    Retorna o valor de accuracy para um usuário em uma disciplina específica.

    Args:
        db: sessão SQLAlchemy.
        user_id: ID do usuário.
        subject_id: ID da disciplina.

    Returns:
        float: Valor de accuracy do usuário na disciplina especificada.
               Retorna None se não existir relação entre o usuário e a disciplina.
    """
    result = (
        db.query(SubjectUser.accuracy_percent)
        .filter(SubjectUser.id_user == user_id,
                SubjectUser.id_subject == subject_id)
        .first()
    )

    return result[0] if result else None
