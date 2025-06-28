from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class QuestionTask(Base):
    __tablename__ = "question_task"

    id_question = Column(Integer, ForeignKey("questions.id"), primary_key=True)
    id_task = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    question = relationship("Question", back_populates="task_links")
    task = relationship("Task", back_populates="questions")
