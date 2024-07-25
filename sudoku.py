class Sudoku:
    def __init__(self, board, sol, diff):
        """
        Initializer for our class.
        Attributes:
        self.board: saves current/initial instance to the game
        self.sol: solution board
        self.diff: stores the difficulty of sudoku game
        """
        self.board = board
        self.sol = self.sol
        self.diff = diff
        self.rows = [set() for i in range(9)]
        self.cols = [set() for i in range(9)]
        self.boxes = [[set() for i in range(3)] for j in range(3)]

    def move(self, i, j, val):
        if self.isValidMove(i, j):
            self.board[i][j] = val
            self.rows[i].add(val)
            self.cols[j].add(val)
            self.boxes[i][j].add(val)

    def remove(self, i, j, val):
        if val != 0:
            self.board[i][j] = 0
            self.rows[i].remove(val)
            self.cols[j].remove(val)
            self.boxes[i][j].remove(val)

    def isValidMove(self, i, j, val):
        return (val not in self.rows[i] and
                val not in self.cols[j] and
                val not in self.boxes[i // 3][j // 3])

    def isSolution(self):
        return self.board == self.sol

    def win(self):
        """
        Checks if the sudoku board works and is
        equivalent to the solution at hand.
        """
        return self.board == self.sol
