from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Topic:
    author_uuid: str
    topic_name: str
    created_date: datetime = datetime.utcnow()
    uuid: Any = None

    def set_id(self, id):
        self.uuid = id

    @property
    def id(self):
        return self.uuid
