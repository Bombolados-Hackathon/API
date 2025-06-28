from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class LectureQuestion(Base):
    __tablename__ = "lecture_question"

    id_lecture = Column(Integer, ForeignKey("lectures.id"), primary_key=True)   # mantém o nome do DBML
    id_question = Column(Integer, ForeignKey("questions.id"), primary_key=True)

    lecture = relationship("Lecture", back_populates="lecture_questions")
    question = relationship("Question", back_populates="lecture_links")
