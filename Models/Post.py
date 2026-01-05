from dataclasses import dataclass, field
import datetime
@dataclass(init=True)
class Post:
    creator_name: str
    content: str
    posting_date: datetime.datetime = field(default_factory=datetime.datetime.now)