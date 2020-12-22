import dataclasses
from dataclasses import dataclass
import json


@dataclass
class User:
    id: str
    name: str
    age: int
    address: str
    points: int = 0  # must be positive

    def add_point(self):
        if self.points is None:
            self.points = 0

        # TODO: check for max int?!
        self.points += 1
        return True

    def sub_point(self):
        if self.points is None or self.points <= 0:
            return False

        self.points -= 1

        return True

    def to_json(self):
        return json.dumps(dataclasses.asdict(self))

    def to_dict(self):
        return dataclasses.asdict(self)
