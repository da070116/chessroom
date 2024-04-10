import os
import random
import subprocess

from board.utils import console_draw
from shipboard.board.utils import FAREWELLS, LETTERS, get_empty_board, CellType


def main():
    board = get_empty_board()
    while True:
        subprocess.run("clear")
        console_draw(board)
        code = input("Input a coordinate please: ")
        if code == "q":
            random.shuffle(FAREWELLS)
            print(FAREWELLS.pop())
            break

        letter = code[0].capitalize()
        digit = int(code[1:]) - 1
        letter_index = LETTERS.find(letter)
        board[letter_index][digit] = str(CellType.AIM)
        print("Shoot again or press `q` for exit")


if __name__ == '__main__':
    main()
