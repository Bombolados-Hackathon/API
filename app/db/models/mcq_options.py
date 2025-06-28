from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class MCQOption(Base):
    __tablename__ = "mcq_options"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_question = Column(Integer, ForeignKey("questions.id"))
    option_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False)

    question = relationship("Question", back_populates="mcq_options")
