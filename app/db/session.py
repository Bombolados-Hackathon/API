from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core import config    # POSTGRES_DSN lá dentro

# ───────────────────────────────────────────────
# Engine síncrono (psycopg2).  Se mudar p/ async,
# troque create_engine → create_async_engine  +
# "postgresql+asyncpg://…"  e adapte get_db.
# ───────────────────────────────────────────────
engine = create_engine(
    config.POSTGRES_DSN,
    pool_pre_ping=True,        # testa conexão antes de reutilizar
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency p/ FastAPI.

    Uso:
        @router.get(...)
        def endpoint(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
