import sys
import time
import random
from board import Board

DEPTH = 6  # default dubina stabla

def evaluate(current, last_mover, last_col, depth):
    if current.game_end(last_col):
        if last_mover == 'CPU':
            return 1  # pobjeda
        else:
            return -1  # poraz

    if depth == 0:
        return 0

    depth -= 1
    new_mover = 'HUMAN' if last_mover == 'CPU' else 'CPU'
    total = 0
    moves = 0
    all_win = True
    all_lose = True

    for col in range(current.get_columns()):
        if current.move_legal(col):
            moves += 1
            current.move(col, new_mover)
            result = evaluate(current, new_mover, col, depth)
            current.undo_move(col)

            if result > -1:
                all_lose = False
            if result != 1:
                all_win = False
            if result == 1 and new_mover == 'CPU':
                return 1
            if result == -1 and new_mover == 'HUMAN':
                return -1

            total += result

    if all_win:
        return 1
    if all_lose:
        return -1

    return total / moves

def main():
    if len(sys.argv) < 2:
        print("Uporaba: <program> <fajl s trenutnim stanjem> [<dubina>]")
        return

    filename = sys.argv[1]
    filename = "ploca.txt"
    B = Board()
    B.load(filename)
    print(B.get_columns)
    print(B.get_rows)
    depth = DEPTH
    if len(sys.argv) > 2:
        depth = int(sys.argv[2])

    random.seed(time.time())

    for col in range(B.get_columns()):
        if B.game_end(col):
            print("Igra zavrsena!")
            return

    best_col = -1
    best_result = -1

    while best_result == -1 and depth > 0:
        print(f"Dubina: {depth}")
        for col in range(B.get_columns()):
            if B.move_legal(col):
                if best_col == -1:
                    best_col = col
                B.move(col, 'CPU')
                result = evaluate(B, 'CPU', col, depth - 1)
                B.undo_move(col)
                if result > best_result or (result == best_result and random.randint(0, 1) == 0):
                    best_result = result
                    best_col = col
                print(f"Stupac {col}, vrijednost: {result}")
        depth //= 2

    print(f"Najbolji: {best_col}, vrijednost: {best_result}")
    B.move(best_col, 'CPU')
    B.save(sys.argv[1])

    for col in range(B.get_columns()):
        if B.game_end(col):
            print("Igra zavrsena! (pobjeda racunala)")
            return

if __name__ == "__main__":
    main()
