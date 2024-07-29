import copy
############################################################
# Sudoku Solver
############################################################


def sudoku_cells():
    # returns all possible index pairs on Sudoku board
    return [(i, j) for i in range(9) for j in range(9)]


def sudoku_arcs():
    # create answer aray
    ans = []
    # iterate through all cells
    for tup in sudoku_cells():
        # get arcs for each cell
        ans += get_arcs(tup)
    # return answer
    return ans


def get_arcs(tup):
    # de-tuple tuple
    r, c = tup
    # storage of all arcs
    arcs = []
    # iterate through columns
    for j in range(9):
        # don't add itself to arcs
        if j == c:
            continue
        # add comparison of arcs btwn diff cols
        arcs.append((tup, (r, j)))
    for i in range(9):
        # don't add itself to arcs
        if i == r:
            continue
        # add comparison of arcs btwn diff rows
        arcs.append((tup, (i, c)))
    # get 3x3 inner box
    borders = get3x3(tup)
    # de-tuple ranges
    x1, y1 = borders[0]
    x2, y2 = borders[1]
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            # don't add iterated rows or cols
            if (i, j) == tup or i == r or j == c:
                continue
            # add new pairs to arcs
            arcs.append((tup, (i, j)))
    # return list of arcs
    return arcs


def get3x3(cell):
    # de-tuple cell
    r, c = cell
    # check upper 3 parts
    if 0 <= r and r <= 2:
        if 0 <= c and c <= 2:
            return [(0, 0), (2, 2)]
        if 3 <= c and c <= 5:
            return [(0, 3), (2, 5)]
        if 6 <= c and c <= 8:
            return [(0, 6), (2, 8)]
    # check middle 3 boxes
    if 3 <= r and r <= 5:
        if 0 <= c and c <= 2:
            return [(3, 0), (5, 2)]
        if 3 <= c and c <= 5:
            return [(3, 3), (5, 5)]
        if 6 <= c and c <= 8:
            return [(3, 6), (5, 8)]
    # check lower 3 boxes
    if 6 <= r and r <= 8:
        if 0 <= c and c <= 2:
            return [(6, 0), (8, 2)]
        if 3 <= c and c <= 5:
            return [(6, 3), (8, 5)]
        if 6 <= c and c <= 8:
            return [(6, 6), (8, 8)]


def read_board(path):
    # open the file via path with read option
    f = open(path, "r")
    # split string/txt by newline/row
    f = f.read().split("\n")
    # instantiate board to return
    board = []
    # iterate through every row
    for row in f:
        # create temporary row array
        temp = []
        # iterate through every row element
        for x in row:
            # check if it's a 'null' value
            if x == "*":
                # if so, add it as 0
                temp.append(0)
            else:
                # otherwise, add nonzero value
                temp.append(int(x))
        # add the row array to the total board array
        board.append(temp)
    # new dictionary object for return value
    dic = {}
    # available set: for if value is 0
    avail = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # iterate through all possible rows
    for i in range(9):
        for j in range(9):
            # if we have an empty value
            if board[i][j] == 0:
                # set it to all possibilities
                dic[(i, j)] = copy.copy(avail)
            else:
                # it has one possibility: set it to that
                dic[(i, j)] = set([board[i][j]])
    # return instantiated dictionary object
    return dic


class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()

    def __init__(self, board):
        # instantiate a board attribute
        self.board = board

    def get_values(self, cell):
        # return the value of the cell key in the board
        return self.board[cell]

    def print_board(self):
        # create board in array form
        board = [[0 for i in range(9)] for j in range(9)]
        # iterate through keys and values
        for k, v in self.board.items():
            # Extract the row and column from the tuple key
            row, col = k
            # Update the board with the value
            board[row][col] = v
        for row in board:
            print(row)
        return None

    def unique_cell(self, elem, cell):
        # initialize potential values
        # horizontal check
        row = False
        # vertical check
        col = False
        # box check
        box = False
        # get row and col
        x1, y1 = cell
        # check same row
        for y2 in range(9):
            # get the second cell we'll compare to
            adv = (x1, y2)
            if cell != adv:
                # check if in row
                if elem in self.board[adv]:
                    row = True
        # check same 3x3 grid
        li = get3x3(cell)
        x1, y1 = li[0]
        x2, y2 = li[1]
        for x2 in range(x1, x2 + 1):
            for y2 in range(y1, y2 + 1):
                # get the second cell we'll compare to
                adv = (x2, y2)
                if cell != adv:
                    # check if it is placed
                    if elem in self.board[adv]:
                        box = True
        # check same col
        for x2 in range(9):
            adv = (x2, y1)
            if cell != adv:
                # check if in col
                if elem in self.board[adv]:
                    col = True
        # return the conglomerate of what we get
        return not row or not col or not box

    def get_board(self):
        # create board in array form
        board = [[0 for i in range(9)] for j in range(9)]
        # iterate through keys and values
        for k, v in self.board.items():
            # Extract the row and column from the tuple key
            row, col = k
            # Update the board with the value
            board[row][col] = v
        # return board
        return board

    def remove_inconsistent_values(self, cell1, cell2):
        # check if the cells are in arcs
        if (cell1, cell2) in self.ARCS:
            # check if cell2 is placed
            if len(self.board[cell2]) == 1:
                # get value from cell2
                v2 = self.board[cell2]
                # check if v2 is in cell1 possible values
                if v2.issubset(self.board[cell1]):
                    self.board[cell1] -= self.board[cell2]
                    return True
        return False

    def is_solved(self):
        # iterate through all cells
        for key in self.CELLS:
            # if one doesn't have length 1, it's not solved
            if len(self.board[key]) != 1:
                # return false
                return False
        # otherwise, we've iterated through! Return true
        return True

    def infer_ac3(self):
        # create queue
        q = []
        # iterate through arcs, add to queue
        for arc in self.ARCS:
            q.append(arc)
        # while queue is greater than 0
        while len(q) > 0:
            # pop out first element
            y1, y2 = q.pop()
            # if we removed a value
            if self.remove_inconsistent_values(y1, y2):
                # if the length of this board is 0
                if len(self.board[y1]) == 0:
                    # return false, solution not possible
                    return False
                # iterate through all arcs
                for arc in self.ARCS:
                    # if there is no solution for the first element
                    if len(self.board[arc[0]]) != 1 and arc[1] == y1:
                        # add it
                        q.append(arc)

    def infer_improved(self):
        # set extra inference to true
        extra_inf = True
        # while true
        while extra_inf:
            # see if we don't have to do work
            self.infer_ac3()
            # set extra inf to false for now
            extra_inf = False
            # iterate through the cells
            for cell in Sudoku.CELLS:
                # if we still need to solve for a value
                if len(self.board[cell]) > 1:
                    # iterate through its elements
                    for elem in self.board[cell]:
                        # if this value is unique to its neighbors
                        if self.unique_cell(elem, cell):
                            # move forward
                            extra_inf = True
                            # this is the only value to set the board to
                            s = set([elem])
                            # set it as such
                            self.board[cell] = s
                            # break: we found our unique cell value
                            break

    def infer_with_guessing(self):
        # do nothing if the board is solved: do as much as possible
        if self.is_solved():
            return
        # see if we also don't have to do anything: infer_improved!
        self.infer_improved()
        # iterate through cells
        for cell in Sudoku.CELLS:
            # get current cell we want to look at
            curr = self.board[cell]
            # if we don't have a set value for it
            if len(self.board[cell]) != 1:
                # iterate through all possible elements
                for elem in curr:
                    # copy the board
                    copied = copy.deepcopy(self.board)
                    # create a set of only the element itself
                    self.board[cell] = set([elem])
                    # recursively call the guess inference
                    self.infer_with_guessing()
                    # if we've solved it at this point, break
                    if self.is_solved():
                        break
                    else:
                        # otherwise, set it to the board
                        self.board = copied
                return
