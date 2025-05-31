import chess
import chess.pgn
import random
import math

class Node:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0
        self.untried_moves = list(board.legal_moves)
        self.player_turn = board.turn

    def uct_select_child(self):
        """ Select a child node with the highest UCT value. """
        return sorted(self.children, key=lambda c: c.wins / c.visits + math.sqrt(2 * math.log(self.visits) / c.visits))[-1]

    def add_child(self, move, board):
        """ Add a child node for the given move. """
        child_node = Node(board, self)
        self.untried_moves.remove(move)
        self.children.append(child_node)
        return child_node

    def update(self, result):
        """ Update this node's statistics. """
        self.visits += 1
        self.wins += result

def simulate(board):
    """ Simulate a random game from the current board state. """
    while not board.is_game_over():
        move = random.choice(list(board.legal_moves))
        board.push(move)
    result = board.result()
    if result == "1-0":
        return 1 if board.turn == chess.WHITE else 0
    elif result == "0-1":
        return 1 if board.turn == chess.BLACK else 0
    else:
        return 0.5

def mcts(root, itermax):
    """ Run MCTS for a given number of iterations. """
    for _ in range(itermax):
        node = root
        board = root.board.copy()

        # Selection
        while node.untried_moves == [] and node.children != []:
            node = node.uct_select_child()
            board.push(node.board.move_stack[-1])

        # Expansion
        if node.untried_moves != []:
            move = random.choice(node.untried_moves)
            board.push(move)
            node = node.add_child(move, board.copy())

        # Simulation
        result = simulate(board)

        # Backpropagation
        while node is not None:
            node.update(result)
            node = node.parent

    return sorted(root.children, key=lambda c: c.visits)[-1].board.move_stack[-1]

def best_move(board, itermax=1000):
    """ Determine the best move using MCTS. """
    root = Node(board)
    best_move = mcts(root, itermax)
    return best_move

if __name__ == "__main__":
    board = chess.Board()
    move = best_move(board, itermax=1000)
    print(f"Best move: {move}")
    board.push(move)
    print(board)
