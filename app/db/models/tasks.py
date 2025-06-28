from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    xp_value = Column(Integer, default=0)
    is_finished = Column(Boolean, default=False)
    id_subject = Column(Integer, ForeignKey("subjects.id"))   # NOVO
    id_user = Column(Integer, ForeignKey("users.id"))

    subject = relationship("Subject", back_populates="tasks") # NOVO
    user = relationship("User", back_populates="tasks")
    questions = relationship("QuestionTask", back_populates="task", cascade="all, delete")
