class Sudoku:
    def __init__(self, board, sol, diff):
        """
        Initializer for our Sudoku class.  This will encapsulate
        the game that we are creating, separating it from the visual
        components.
        Attributes:
        self.board: saves current/initial instance to the game
        self.sol: solution board
        self.diff: stores the difficulty of sudoku game
        self.rows: stores unique number values for every row
        self.cols: stores unique number values for every column
        self.boxes: stores unique number values for every 3x3 box
        self.initial: stores initial coordinates for every non-zero value
        """
        self.board = board
        self.sol = sol
        self.diff = diff
        self.rows = [set() for i in range(9)]
        self.cols = [set() for i in range(9)]
        self.boxes = [[set() for i in range(3)] for j in range(3)]
        self.initial = set()
        # add all non-zero value coordinates to the set
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != 0:
                    self.initial.add((i, j))

    def getBoard(self):
        """
        Description: Getter for drawing board.
        Args: None
        Returns: 9x9 board state (2d array)
        """
        return self.board

    def getVal(self, i, j):
        """
        Description: gets the val at specific
        coordinates.
        Args: i (row), j (column)
        Returns: value at row i and col j of board.
        """
        return self.board[i][j]

    def getDiff(self):
        """
        Description: gets the difficulty of the board
        for SideBar Drawing.
        Args: None
        Returns: string denoting board difficulty.
        """
        return self.diff

    def getSol(self):
        """
        Description: Getter for Solution board.
        Args: None
        Returns: 9x9 board state (2d array)
        """
        return self.sol

    def getInitial(self):
        """
        Description: Gets a set of all initial coordinates.
        Important for coloring points differently.
        Args: None
        Returns: set of (x, y) tuples
        """
        return self.initial

    def move(self, i, j, val):
        """
        Description: Moves the value to the (i, j) coordinate in
        self.board, provided that:
        1. The move itself is valid
        2. the coordinates in question were not one of the initial
        coordinates, as they should not be changed.
        Args: i (row), j (col), val (value in question)
        Returns: None
        """
        if self.isValidMove(i, j, val) and (i, j) not in self.initial:
            self.board[i][j] = val
            self.rows[i].add(val)
            self.cols[j].add(val)
            self.boxes[i // 3][j // 3].add(val)

    def remove(self, i, j):
        """
        Description: Removes the value to the (i, j) coordinate in
        self.board, provided that:
        1. The removal itself is valid
        2. the coordinates in question were not one of the initial
        coordinates, as they should not be changed.
        Args: i (row), j (col), val (value in question)
        Returns: None
        """
        if self.board[i][j] != 0 and (i, j) not in self.initial:
            val = self.board[i][j]
            self.board[i][j] = 0
            self.rows[i].remove(val)
            self.cols[j].remove(val)
            self.boxes[i // 3][j // 3].remove(val)

    def isValidMove(self, i, j, val):
        """
        Description: makes sure the value
        in question is not in any relevant sets.
        Args: i (row), j (col), val (nonzero value)
        Returns: True if value is not in any rel.
        sets, False otherwise
        """
        return (val not in self.rows[i] and
                val not in self.cols[j] and
                val not in self.boxes[i // 3][j // 3])

    def win(self):
        """
        Description: Checks if the sudoku board works and is
        equivalent to the solution at hand.
        """
        return self.board == self.sol
