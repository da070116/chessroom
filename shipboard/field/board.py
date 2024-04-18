import enum
import os

from dotenv import load_dotenv

from shipboard.field.coordinate_manager import Coordinate
from shipboard.ships.ship import Ship

load_dotenv()


class CellType(enum.Enum):
    """ All possible states of cell. """
    FOG = "~"
    HIT = "@"
    MISS = '.'
    SET = "#"

    def __str__(self):
        return self.value


class GameBoard:
    size: int
    alphabet: str
    cells: list[list[CellType]]
    hidden_cells: list[list[CellType]]
    cell_width: int
    ships: list[Ship]

    @staticmethod
    def get_default_size(max_value: int):
        try:
            return env_value if (env_value := int(os.getenv("SIZE"))) <= max_value else max_value
        except (ValueError, TypeError):
            return max_value

    def __init__(self, size: int = None):
        self.ships = []
        self.alphabet = os.getenv("ALPHABET", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.cell_width = 3

        if size and size <= len(self.alphabet):
            self.size = size
        else:
            self.size = self.get_default_size(max_value=len(self.alphabet))

        self.cells = self.get_empty_board()
        self.hidden_cells = self.get_empty_board()

        self.add_ships([
            Ship(name="Cruiser", position=[
                Coordinate(0, 0, "A1"),
                Coordinate(1, 0, "B1"),
                Coordinate(2, 0, "C1"),
            ])
        ])

    def get_empty_board(self, filler: CellType | None = None) -> list:
        if not filler:
            filler = CellType.FOG
        return list([filler for _ in range(self.size)] for _ in range(self.size))

    def fire_at(self, coord: Coordinate):
        for s in self.ships:
            s.check_damage(coord)
        row, col = coord.get_tuple()
        if self.hidden_cells[row][col] == CellType.SET:
            self.cells[row][col] = CellType.HIT
        else:
            self.cells[row][col] = CellType.MISS

    def get_max_damage(self):
        return sum([s.size for s in self.ships])

    def get_current_damage(self):
        return sum([len(s.damage) for s in self.ships])

    def console_draw(self, tries: int):
        print("TRIES LEFT:", tries)
        print("BOARD".center((self.size + 1) * self.cell_width))
        print(" ", " ".join(f"{number + 1:{self.cell_width}}" for number in range(self.size)), sep="")

        for row in range(self.size):
            print(self.alphabet[row], end=" ")
            for col in range(self.size):
                cell = str(self.cells[row][col])
                print(cell.center(self.cell_width), end=" ")
            print("")

    def add_ships(self, ships: list[Ship]):
        for s in ships:
            self.ships.append(s)
            for coord in s.position:
                row_position, col_position = coord.get_tuple()
                self.hidden_cells[row_position][col_position] = CellType.SET
