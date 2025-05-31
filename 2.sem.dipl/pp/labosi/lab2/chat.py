from mpi4py import MPI
import numpy as np

# Dimenzije igraćeg polja
ROWS = 6
COLS = 7
WIN_SEQ = 4

# Vrijednosti za igrače
EMPTY = 0
PLAYER = 1
COMPUTER = 2

# MPI inicijalizacija
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Provjera pobjedničkog niza
def check_winner(board, row, col, player):
    def count_seq(board, row, col, delta_row, delta_col):
        count = 0
        r, c = row, col
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
            count += 1
            r += delta_row
            c += delta_col
        return count

    # Horizontalno
    if count_seq(board, row, col, 0, 1) + count_seq(board, row, col, 0, -1) - 1 >= WIN_SEQ:
        return True
    # Vertikalno
    if count_seq(board, row, col, 1, 0) + count_seq(board, row, col, -1, 0) - 1 >= WIN_SEQ:
        return True
    # Dijagonalno /
    if count_seq(board, row, col, 1, 1) + count_seq(board, row, col, -1, -1) - 1 >= WIN_SEQ:
        return True
    # Dijagonalno \
    if count_seq(board, row, col, 1, -1) + count_seq(board, row, col, -1, 1) - 1 >= WIN_SEQ:
        return True

    return False

# Dodavanje poteza
def make_move(board, col, player):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return row, col
    return None, None

# Uklanjanje poteza (za vraćanje poteza)
def undo_move(board, row, col):
    board[row][col] = EMPTY

# Ocjena poteza
def evaluate_move(board, depth, maximizing_player):
    if check_winner(board, row, col, COMPUTER):
        return 1
    if check_winner(board, row, col, PLAYER):
        return -1
    if depth == 0:
        return 0
    scores = []
    for col in range(COLS):
        if board[0][col] == EMPTY:
            row, col = make_move(board, col, COMPUTER if maximizing_player else PLAYER)
            if row is not None:
                score = evaluate_move(board, depth-1, not maximizing_player)
                scores.append(score)
                undo_move(board, row, col)
    return max(scores) if maximizing_player else min(scores)

# Računanje najboljeg poteza
def compute_best_move(board, depth):
    best_score = -float('inf')
    best_move = None
    for col in range(COLS):
        if board[0][col] == EMPTY:
            row, col = make_move(board, col, COMPUTER)
            if row is not None:
                score = evaluate_move(board, depth-1, False)
                if score > best_score:
                    best_score = score
                    best_move = col
                undo_move(board, row, col)
    return best_move

# Paralelno računanje poteza
def parallel_best_move(board, depth):
    if rank == 0:
        # Master process: raspodijeli zadatke
        moves = list(range(COLS))
        move_chunks = np.array_split(moves, size)
    else:
        move_chunks = None

    # Scatter move chunks to all processes
    move_chunk = comm.scatter(move_chunks, root=0)

    # Calculate best move in each chunk
    local_best_score = -float('inf')
    local_best_move = None
    for col in move_chunk:
        if board[0][col] == EMPTY:
            row, col = make_move(board, col, COMPUTER)
            if row is not None:
                score = evaluate_move(board, depth-1, False)
                if score > local_best_score:
                    local_best_score = score
                    local_best_move = col
                undo_move(board, row, col)

    # Gather best moves from all processes
    all_best_moves = comm.gather((local_best_score, local_best_move), root=0)

    if rank == 0:
        # Master process: choose the overall best move
        best_score, best_move = max(all_best_moves)
        return best_move
    else:
        return None

# Glavna funkcija
def main():
    board = np.zeros((ROWS, COLS), dtype=int)
    depth = 7

    while True:
        if rank == 0:
            print(board)
            player_move = int(input("Unesite potez (0-6): "))
            make_move(board, player_move, PLAYER)

            if check_winner(board, *make_move(board, player_move, PLAYER), PLAYER):
                print("Pobijedili ste!")
                break

        best_move = parallel_best_move(board, depth)

        if rank == 0:
            print(f"Računalo odabire potez: {best_move}")
            make_move(board, best_move, COMPUTER)

            if check_winner(board, *make_move(board, best_move, COMPUTER), COMPUTER):
                print("Računalo je pobijedilo!")
                break

if __name__ == "__main__":
    main()
