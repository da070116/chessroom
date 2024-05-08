from builtins import property

from shipboard.gameplay.constants import DEFAULT_ALPHABET, CellContent
from shipboard.gameplay.exceptions import (
    CoordinateBadArgsGiven,
    CoordinateHasNoDigit,
    CoordinateNoSuchLetterInGivenAlphabet,
)


class Cell:
    row: int
    col: int
    name: str
    content: CellContent

    def __init__(self, symbol: CellContent, alphabet: str = None, val: str = None, **kwargs):
        if not alphabet:
            alphabet = DEFAULT_ALPHABET
        if kwargs:
            r = kwargs.get("row")
            c = kwargs.get("col")
            if not isinstance(r, int):
                raise CoordinateBadArgsGiven()
            if r > len(alphabet) or r < 0:
                raise CoordinateNoSuchLetterInGivenAlphabet()
            if not isinstance(c, int) or c < 0:
                raise CoordinateHasNoDigit()
            self.row = r
            self.col = c
            self.name = f"{alphabet[r].capitalize()}{c + 1}"
        else:
            letter = val[0]
            try:
                digit = int(val[1:])
            except ValueError:
                raise CoordinateHasNoDigit()
            r = alphabet.lower().find(letter.lower())
            if r == -1:
                raise CoordinateNoSuchLetterInGivenAlphabet()
            self.row = r
            self.col = digit - 1
            self.name = f"{alphabet[r].capitalize()}{digit}"
        self.content = symbol

    @property
    def coordinate(self) -> tuple[int, int]:
        return self.row, self.col

    def __str__(self):
        return f"{self.name}: {str(self.content)}"



