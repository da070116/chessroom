import enum
import os

from dotenv import load_dotenv

from shipboard.field.coordinate_manager import Coordinate, CoordinateManager
from shipboard.utils.exceptions import ShipCoordinatesCollision
from shipboard.ships.ship import Ship, SHIP_TYPES

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

    def get_empty_board(self, filler: CellType | None = None) -> list:
        if not filler:
            filler = CellType.FOG
        return list([filler for _ in range(self.size)] for _ in range(self.size))

    def fire_at(self, coord: Coordinate):
        for s in self.ships:
            s.check_damage(coord)
        row, col = coord.get_tuple()
        if row > self.size or col > self.size:
            return
        if self.hidden_cells[row][col] == CellType.SET:
            self.cells[row][col] = CellType.HIT
        else:
            self.cells[row][col] = CellType.MISS

    def get_max_damage(self):
        return sum([s.size for s in self.ships])

    def get_current_damage(self):
        return sum([len(s.damage) for s in self.ships])

    def draw_gameplay(self, tries: int):
        print("TRIES LEFT:", tries)
        print("BOARD".center((self.size + 1) * self.cell_width))
        self.console_draw(self.cells)

    def console_draw(self, source:list[list[CellType]]):
        print(" ", " ".join(f"{number + 1:{self.cell_width}}" for number in range(self.size)), sep="")
        for row in range(self.size):
            print(self.alphabet[row], end=" ")
            for col in range(self.size):
                cell = str(source[row][col])
                print(cell.center(self.cell_width), end=" ")
            print("")

    @staticmethod
    def place_coordinate(coordinate: Coordinate, source: list[list[CellType]]):
        row_position, col_position = coordinate.get_tuple()
        point = source[row_position][col_position]
        if point == CellType.SET:
            print(f"Wrong board position: point [{row_position}, {col_position}] is busy")
        else:
            source[row_position][col_position] = CellType.SET

    def add_ships_manually(self, coordinate_manager: CoordinateManager):
        # input ships
        ships = []


        # for name, size in SHIP_TYPES.items():
        #     self.console_draw(self.hidden_cells)
        #     coordinates_list = []
        #     start_coordinate = coordinate_manager.coordinate_from_str(input(f"Input start coordinate for {name}: "))
        #     end_coordinate = coordinate_manager.coordinate_from_str(input(f"Input end coordinate for {name}: "))
        #     # for i in range(size):
        #     #     raw_ship_point = input(f"Input {i+1} of {size} coordinate for {name}: ")
        #     #     coordinate = coordinate_manager.coordinate_from_str(raw_ship_point)
        #     #     coordinates_list.append(coordinate)
        #     #     self.place_coordinate(coordinate, self.hidden_cells)
        #     ships.append(Ship(name, coordinates_list))
        #
        # self.ships = ships
        # #
        # # for s in ships:
        # #     for coord in s.position:
        # #         row_position, col_position = coord.get_tuple()
        # #         point = self.hidden_cells[row_position][col_position]
        # #         if point == CellType.SET:
        # #             print(f"Wrong board position: point [{row_position}, {col_position}] is busy")
        # #             break
        # #         else:
        # #             self.hidden_cells[row_position][col_position] = CellType.SET
        # #     else:
        # #         self.ships.append(s)
        # if len(self.ships) != len(SHIP_TYPES):
        #     raise ShipCoordinatesCollision()

    def place_ship(self, name: str, coordinate_manager: CoordinateManager, field: list[list[CellType]]):
        print(f"Add coordinates for {name}")
        while True:
            start_coordinate = coordinate_manager.coordinate_from_str(input(f"Input start coordinate for {name}: "))
            end_coordinate = coordinate_manager.coordinate_from_str(input(f"Input end coordinate for {name}: "))
            try:
                coordinate_manager.compare()

