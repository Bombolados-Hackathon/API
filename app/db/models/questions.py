import enum
from sqlalchemy import Column, Integer, Text, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base


class QuestionType(str, enum.Enum):
    multiple_choice = "multiple_choice"
    true_false = "true_false"
    matching = "matching"


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_type = Column(Enum(QuestionType, name="question_type"), nullable=False)
    title = Column(Text, nullable=False)                    # RENOMEADO

    mcq_options = relationship("MCQOption", back_populates="question", cascade="all, delete-orphan")
    tf_answer = relationship("TFAnswer", back_populates="question", uselist=False, cascade="all, delete-orphan")
    matching_pairs = relationship("MatchingPair", back_populates="question", cascade="all, delete-orphan")
    lecture_links = relationship("LectureQuestion", back_populates="question", cascade="all, delete")
    task_links = relationship("QuestionTask", back_populates="question", cascade="all, delete")
