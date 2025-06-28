from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, autoincrement=True)
    raw_text = Column(Text, nullable=False)
    was_watched = Column(Boolean, default=False)           # ← renomeado
    id_subject = Column(Integer, ForeignKey("subjects.id"))

    subject = relationship("Subject", back_populates="lectures")
    questions = relationship("Question", back_populates="lecture", cascade="all, delete")  # ← novo
