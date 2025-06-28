from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.tasks import complete_task
from app.db.session import get_db
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
