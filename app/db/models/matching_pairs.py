from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class MatchingPair(Base):
    __tablename__ = "matching_pairs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_question = Column(Integer, ForeignKey("questions.id"))
    left_item = Column(Text, nullable=False)
    right_item = Column(Text, nullable=False)

    question = relationship("Question", back_populates="matching_pairs")
