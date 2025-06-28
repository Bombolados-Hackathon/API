from sqlalchemy import Column, Integer, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    xp_value = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # ← novo
    is_finished = Column(Boolean, default=False)
    id_subject = Column(Integer, ForeignKey("subjects.id"))
    id_user = Column(Integer, ForeignKey("users.id"))

    subject = relationship("Subject", back_populates="tasks") # NOVO
    user = relationship("User", back_populates="tasks")
    questions = relationship("Question", back_populates="task", cascade="all, delete")  # ← NOVO
