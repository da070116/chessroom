import os
from random import shuffle
import subprocess

from shipboard.field.board import GameBoard
from shipboard.field.coordinate_manager import CoordinateManager
from shipboard.utils.exceptions import TerminateInput

FAREWELLS = [
    "More power to you!",
    "Fair winds and following seas!",
    "Have a good one!",
    "Safe travels!"
]

# def main():
#     board = get_empty_board()
#     ship_coordinates = [(0, 0), (0, 1)]
#     hidden_board = add_ships(ship_coordinates)
#     msg = {
#         "tries": TRIES,
#         "hits": 0,
#         "info": "",
#         "errors": []
#     }
#     while True:
#         subprocess.run("clear")
#
#         if msg.get("tries") == 0:
#             random.shuffle(FAREWELLS)
#             console_draw(hidden_board)
#             print(f"This game is over. Out of ammo. {FAREWELLS.pop()}")
#             break
#
#         if msg.get("hits") == len(ship_coordinates):
#             random.shuffle(FAREWELLS)
#             console_draw(hidden_board)
#             print(f"All ships have sunk. {FAREWELLS.pop()}")
#             break
#         else:
#             console_draw(board)
#
#         while msg["errors"]:
#             print(msg["errors"].pop())
#
#         code = input(f"Ammo left: {msg.get('tries')}. Input a coordinate please: ")
#         if code == "q":
#             random.shuffle(FAREWELLS)
#             print(FAREWELLS.pop())
#             break
#
#         letter = code[0].capitalize()
#         col = int(code[1:]) - 1
#         row = LETTERS.find(letter)
#         try:
#             _try: str = board[row][col]
#             if not msg.get("info"):
#                 msg["info"] = "Shoot or enter `q` for exit"
#             if str(CellType.FOG) == _try:
#                 if hidden_board[row][col] == str(CellType.SET):
#                     board[row][col] = str(CellType.HIT)
#                     msg["hits"] += 1
#                 else:
#                     board[row][col] = str(CellType.MISS)
#             else:
#                 msg["errors"].append("Already tried that cell!")
#         except IndexError:
#             msg["errors"].append("Cell out of range!")
#         finally:
#             msg["tries"] -= 1


if __name__ == '__main__':

    board = GameBoard()
    cm = CoordinateManager(alphabet=board.alphabet)
    try:
        board.add_ships_manually(coordinate_manager=cm)
    except TerminateInput:
        print("Game was terminated")
        exit()
    tries = (board.size ** 2) - (board.size ** 2 // 5)
    while True:
        subprocess.run("clear")
        board.draw_gameplay(tries)

        if tries == 0:
            shuffle(FAREWELLS)
            print(f"This game is over. Out of ammo. {FAREWELLS.pop()}")
            break
        a = board.get_current_damage()
        b = board.get_max_damage()
        if a == b and a > 0:
            shuffle(FAREWELLS)
            print(f"All ships have sunk. {FAREWELLS.pop()}")
            break

        action = input("Shoot or enter `q` for exit: ")
        if action == "q":
            shuffle(FAREWELLS)
            print(FAREWELLS.pop())
            break

        board.fire_at(coord=cm.coordinate_from_str(action))
        tries -= 1
