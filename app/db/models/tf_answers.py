from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class TFAnswer(Base):
    __tablename__ = "tf_answers"

    id_question = Column(Integer, ForeignKey("questions.id"), primary_key=True)
    correct = Column(Boolean, nullable=False)

    question = relationship("Question", back_populates="tf_answer")
