import enum
import os

from dotenv import load_dotenv

load_dotenv()
SIZE = int(os.getenv("SIZE"))
LETTERS = "ABCDEFGHIJ"

FAREWELLS = [
    "More power to you!",
    "Fair winds and following seas!",
    "Have a good one!",
    "Safe travels!"
]


class CellType(enum.Enum):
    """ All possible states of cell. """
    AIM = "#"
    FOG = " "
    HIT = "*"
    MISS = '.'
    SET = "+"

    def __str__(self):
        return self.value


def get_empty_board() -> list:
    f = str(CellType.FOG)
    return [
        [f for _ in range(SIZE)] for _ in range(SIZE)
    ]


def console_draw(board: list):

    print(" ", ",".join(f"{number+1:4}" for number in range(SIZE)), sep="")

    for num, _ in enumerate(board):
        print(LETTERS[num], board[num])
