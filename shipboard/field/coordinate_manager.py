class Coordinate:
    name: str
    row: int
    col: int

    def __init__(self, row, col, name):
        self.col = col
        self.row = row
        self.name = name

    def __str__(self):
        return self.name

    def get_tuple(self):
        return self.row, self.col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


class CoordinateManager:
    alphabet: str

    def __init__(self, alphabet: str):
        self.alphabet = alphabet

    def coordinate_from_str(self, value: str):
        try:
            letter = value[0].capitalize()
            col = int(value[1:]) - 1
            row = self.alphabet.find(letter)
        except (ValueError, TypeError, IndexError):
            col = 0
            row = 0
            letter = self.alphabet[0].capitalize()

        name = f"{letter}{col + 1}"

        return Coordinate(row, col, name)

