from shipboard.gameplay.constants import DEFAULT_ALPHABET, DEFAULT_SIZE, CellContent
from shipboard.gameplay.cell import Cell


class Board:
    size: int
    alphabet: str
    is_hidden: bool
    fields: list[list[Cell]]

    def __init__(self, is_hidden: bool, size: int = DEFAULT_SIZE, alphabet: str = DEFAULT_ALPHABET):
        self.size = size
        self.is_hidden = is_hidden
        self.alphabet = alphabet
        self.fields = self.create_empty_board()

    def create_empty_board(self):
        result = []
        symbol_to_fill = CellContent.SEA if self.is_hidden else CellContent.FOG
        for i in range(self.size):
            result.append(
                [Cell(row=i, col=j, symbol=symbol_to_fill) for j in range(self.size)]
            )
        return result

    def fire_at(self, cell: Cell) -> bool:
        is_hit = False
        row, col = cell.coordinate
        target_cell = self.fields[row][col]
        if target_cell.content == CellContent.DCK:
            self.fields[row][col] = CellContent.HIT


        return is_hit

    def visualize(self) -> list[list[str]]:
        result = [list()] * self.size
        for i in range(self.size):
            result[i] = []
            for j in range(self.size):
                cell = self.fields[i][j]
                result[i].append(str(cell.content))
        return result


