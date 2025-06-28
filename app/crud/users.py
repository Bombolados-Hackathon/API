# crud/users.py
from typing import Optional
from sqlalchemy.orm import Session

from app.db.models.users import User


def get_user(db: Session, user_id: int) -> Optional[User]:
    """Busca o usuário completo (ou None)."""
    return db.get(User, user_id)


def get_user_name_and_xp(db: Session, user_id: int) -> Optional[tuple[str, int]]:
    """
    Retorna apenas (name, xp) do usuário,
    usando projeção para evitar sobrecarga de colunas.
    """
    return (
        db.query(User.name, User.xp)
        .filter(User.id == user_id)
        .one_or_none()             # devolve tupla ou None
    )
