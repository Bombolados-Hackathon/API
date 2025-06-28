# api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.users import get_user_name_and_xp
from app.db.session import get_db
from app.schemas.users import UserXPResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/{user_id}/xp",
    response_model=UserXPResponse,
    summary="Retorna nome e XP de um usuário",
    responses={404: {"description": "Usuário não encontrado"}},
)
def get_user_xp(user_id: int, db: Session = Depends(get_db)):
    result = get_user_name_and_xp(db, user_id)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado",
        )

    name, xp = result
    return UserXPResponse(name=name, xp=xp)
