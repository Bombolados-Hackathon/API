from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    xp = Column(Integer, default=0)
    streak = Column(Integer, default=0)
    freeze_attack_count = Column(Integer, default=0)
    clear_pending_count = Column(Integer, default=0)
    skip_question_count = Column(Integer, default=0)

    subjects = relationship("SubjectUser", back_populates="user", cascade="all, delete")
    tasks = relationship("Task", back_populates="user", cascade="all, delete")
