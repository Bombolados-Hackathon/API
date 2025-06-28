from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.tasks import complete_task, completed_task, create_task as insert_task
from app.crud.subject_user import get_subject_ids_by_user, get_accuracy_by_user_and_subject
from app.db.models import Task
from app.db.session import get_db
from app.helper import calculate_xp
from app.schemas.tasks import TaskXPValueResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get(
    "/{task_id}/xp",
    response_model=TaskXPValueResponse,
    summary="Retorna XP ganho ao concluir tarefa",
    responses={404: {"description": "Tarefa não encontrada"}},
)
def get_user_xp(task_id: int, db: Session = Depends(get_db)):
    result = complete_task(db, task_id)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada",
        )

    xp = result
    return TaskXPValueResponse(xp=xp)

@router.get(
    "/{user_id}/tasks/completed",
    summary="Retorna tarefas concluídas do usuário",
    responses={404: {"description": "Usuário não encontrado"}},
)
def get_completed_task(user_id: int, db: Session = Depends(get_db)):
    tasks = completed_task(db, user_id)
    if tasks is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado",
        )
    return tasks

@router.get(
    "/{user_id}/create_task",
    summary="Retorna XP ganho ao concluir tarefa",
    responses={404: {"description": "Tarefa não encontrada"}},
)
async def create_task(user_id: int, db: Session = Depends(get_db)):
    subject_id = get_subject_ids_by_user(db, user_id)[0]
    accuracy = get_accuracy_by_user_and_subject(db, user_id, subject_id)
    xp_value = calculate_xp(accuracy) if accuracy is not None else 0
    await insert_task(db, subject_id, user_id, xp_value)

@router.get(
    "/",
    summary="Retorna todas as tarefas",
    responses={404: {"description": "Nenhuma tarefa encontrada"}},
)
async def get_tasks(db: Session = Depends(get_db)):
    """
    Endpoint para obter todas as tarefas.
    """
    tasks = db.query(Task).all()
    if not tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma tarefa encontrada",
        )
    return tasks