from typing import Optional, Tuple

from sqlalchemy.orm import Session

from app.db.models.tasks import Task
from app.db.models.users import User


def complete_task(db: Session, task_id: int) -> Optional[int]:
    """
    • Define `is_finished = True` na task.
    • Soma `task.xp_value` no `user.xp`.
    • Retorna `(user.name, user.xp)` depois da operação.

    Retorna **None** se a task não existir ou não tiver usuário vinculado.
    """
    task: Task | None = db.get(Task, task_id)
    if task is None or task.id_user is None:
        return None                       # Task inexistente ou “solta”

    user: User = task.user                # relacionamento ORM (Task.user)

    if not task.is_finished:              # só processa 1ª vez
        task.is_finished = True
        user.xp += task.xp_value
        db.commit()                       # persiste ambas as alterações
        db.refresh(user)                  # pega xp atualizado

    return task.xp_value
