"""
Importa cada model para que o metadata da Base conheça todas as tabelas
antes de chamar create_all().
"""
from app.db.base import Base  # noqa: F401

from .subjects import Subject  # noqa: F401
from .users import User  # noqa: F401
from .subject_user import SubjectUser  # noqa: F401
from .lectures import Lecture  # noqa: F401
from .tasks import Task  # noqa: F401
from .questions import Question  # noqa: F401
from .mcq_options import MCQOption  # noqa: F401
from .tf_answers import TFAnswer  # noqa: F401
from .matching_pairs import MatchingPair  # noqa: F401
