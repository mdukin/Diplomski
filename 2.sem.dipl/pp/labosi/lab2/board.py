class Board:
    EMPTY = 0
    HUMAN = 1
    CPU = 2

    def __init__(self):
        self.field = None
        self.height = None
        self.rows = 0
        self.cols = 0
        self.last_mover = None
        self.last_col = -1

    def free(self):
        self.field = None
        self.height = None

    def take(self):
        self.field = [[self.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]
        self.height = [0] * self.cols

    def load(self, filename):
        with open(filename, "r") as f:
            self.rows, self.cols = map(int, f.readline().split())
            self.free()
            self.take()
            for r in range(self.rows-1, -1, -1):
                line = f.readline().split()
                for c in range(self.cols):
                    self.field[r][c] = int(line[c])
            for c in range(self.cols):
                for h in range(self.rows):
                    if self.field[h][c] != self.EMPTY:
                        self.height[c] = h + 1
                    else:
                        break

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(f"{self.rows} {self.cols}\n")
            for r in range(self.rows-1, -1, -1):
                f.write(" ".join(map(str, self.field[r])) + "\n")

    def move_legal(self, col):
        return col < self.cols and self.field[self.rows - 1][col] == self.EMPTY

    def move(self, col, player):
        if not self.move_legal(col):
            return False
        self.field[self.height[col]][col] = player
        self.height[col] += 1
        self.last_mover = player
        self.last_col = col
        return True

    def undo_move(self, col):
        if col < self.cols and self.height[col] > 0:
            self.height[col] -= 1
            self.field[self.height[col]][col] = self.EMPTY
            return True
        return False

    def game_end(self, last_col):
        if last_col >= self.cols:
            return False
        row = self.height[last_col] - 1
        if row < 0:
            return False
        player = self.field[row][last_col]

        def check_sequence(direction_row, direction_col):
            r, c, seq = row, last_col, 0
            while r >= 0 and r < self.rows and c >= 0 and c < self.cols and self.field[r][c] == player:
                seq += 1
                r += direction_row
                c += direction_col
            return seq >= 4

        directions = [(-1, 0), (0, -1), (-1, -1), (-1, 1)]
        for dr, dc in directions:
            if check_sequence(dr, dc) or check_sequence(-dr, -dc):
                return True
        return False

    def get_columns(self):
        return self.cols

    def get_rows(self):
        return self.rows
