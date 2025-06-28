from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    users = relationship("SubjectUser", back_populates="subject", cascade="all, delete")
    lectures = relationship("Lecture", back_populates="subject", cascade="all, delete")
    tasks = relationship("Task", back_populates="subject", cascade="all, delete")  # NOVO
