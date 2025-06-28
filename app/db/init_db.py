from sqlalchemy import text
from app.db.session import engine
from app.db.base import Base
import app.db.models  # side-effect que registra tabelas


def run() -> None:
    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        Base.metadata.create_all(bind=conn)
    print("✅ Banco inicializado com sucesso.")


if __name__ == "__main__":
    run()
