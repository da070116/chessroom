from shipboard.field.coordinate_manager import Coordinate


class Ship:
    name: str
    size: int
    position: set[Coordinate]
    damage: list[Coordinate]

    def __init__(self, name, position):
        self.name = name
        self.size = len(position)
        self.position = position
        self.damage = []

    def get_coordinates(self):
        return self.position

    def check_damage(self, coordinate: Coordinate):
        if coordinate in self.position and coordinate not in self.damage:
            self.damage.append(coordinate)

    @property
    def is_sink(self):
        return self.damage == self.position