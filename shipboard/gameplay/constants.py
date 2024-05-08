from enum import StrEnum
from typing_extensions import Final

DEFAULT_ALPHABET: Final[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DEFAULT_MAX_SIZE: Final[int] = len(DEFAULT_ALPHABET)
DEFAULT_SIZE: Final[int] = 10


class CellContent(StrEnum):
    FOG = "?"
    HIT = "☒"
    MIS = "∙"
    SEA = "~"
    DCK = "☐"

    def __str__(self):
        return self.value
