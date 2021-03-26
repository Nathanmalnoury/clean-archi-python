import abc
from dataclasses import dataclass
from domain.ports.user_repository import AbstractUserRepository

@dataclass
class Model:
    user_repo: AbstractUserRepository
