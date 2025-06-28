from typing import Optional, Any

from sqlalchemy.orm import Session

from app.db.models.tasks import Task
from app.db.models.users import User
from app.crud.questions import create_questions


async def create_task(db: Session, subject_id: int, user_id: int, xp_value: int) -> None:
    task = Task(
        xp_value=xp_value,
        is_finished=False,
        id_subject=subject_id,
        id_user=user_id,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    await create_questions(db, task.id, user_id)

def completed_task(db: Session, user_id: int) -> type[Task] | None:
    """
    Retorna uma lista de tasks concluídas (`is_finished = True`) do usuário.

    Args:
        db: sessão SQLAlchemy aberta.
        user_id: ID do usuário (users.id).

    Returns:
        Lista de Task concluídas ou vazia se não houver registros.
    """
    return (
        db.query(Task)
        .filter(Task.id_user == user_id, Task.is_finished.is_(True))
        .order_by(Task.id)
        .first()
    )


def complete_task(db: Session, task_id: int) -> Optional[int]:
    """
    • Define `is_finished = True` na task.
    • Soma `task.xp_value` no `user.xp`.
    • Retorna `(user.name, user.xp)` depois da operação.

    Retorna **None** se a task não existir ou não tiver usuário vinculado.
    """
    task: Task | None = db.get(Task, task_id)
    if task is None or task.id_user is None:
        return None  # Task inexistente ou “solta”

    user: User = task.user  # relacionamento ORM (Task.user)

    if not task.is_finished:  # só processa 1ª vez
        task.is_finished = True
        user.xp += task.xp_value
        db.commit()  # persiste ambas as alterações
        db.refresh(user)  # pega xp atualizado

    return task.xp_value
