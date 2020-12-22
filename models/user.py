from dataclasses import dataclass


@dataclass
class User:
    id: str
    name: str
    age: int
    address: str
    points: int = 0  # must be positive

    def add_point(self):
        # TODO: check for max int?!
        self.points += 1
        return True

    def sub_point(self):
        if self.points > 0:
            self.points -= 1
            return True

        return False
