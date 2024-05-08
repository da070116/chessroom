import pytest

from shipboard.gameplay.board import Cell
from shipboard.gameplay.exceptions import CoordinateHasNoDigit, CoordinateNoSuchLetterInGivenAlphabet


def test_coordinate_creation():
    alphabet = "abcdef"
    by_val_is_fine = Cell("a1")
    assert isinstance(by_val_is_fine, Cell) is True
    pytest.raises(CoordinateHasNoDigit, Cell, alphabet, "aa")
    pytest.raises(CoordinateNoSuchLetterInGivenAlphabet, Cell, alphabet, "j1")

    by_key = Cell(alphabet, row=0, col=0)
    assert isinstance(by_key, Cell)
    assert by_key.name == by_val_is_fine.name
    pytest.raises(CoordinateHasNoDigit, Cell, alphabet, row=0)
