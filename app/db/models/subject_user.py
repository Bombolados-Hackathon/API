from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class SubjectUser(Base):
    __tablename__ = "subject_user"

    id_subject = Column(Integer, ForeignKey("subjects.id"), primary_key=True)
    id_user = Column(Integer, ForeignKey("users.id"), primary_key=True)
    accuracy_percent = Column(Numeric(5, 2), default=0)

    subject = relationship("Subject", back_populates="users")
    user = relationship("User", back_populates="subjects")
