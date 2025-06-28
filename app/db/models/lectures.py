from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    raw_text = Column(Text, nullable=False)
    has_watched = Column(Boolean, default=False)          # NOVO
    id_subject = Column(Integer, ForeignKey("subjects.id"))

    subject = relationship("Subject", back_populates="lectures")
    lecture_questions = relationship(
        "LectureQuestion",
        back_populates="lecture",
        cascade="all, delete"
    )
