import unittest
from sudoku import Sudoku

b = [[0, 0, 4, 7, 6, 3, 2, 0, 0],
     [8, 6, 0, 0, 0, 0, 3, 5, 0],
     [9, 0, 2, 0, 5, 1, 4, 6, 0],
     [0, 1, 5, 6, 0, 0, 0, 4, 0],
     [4, 0, 0, 0, 1, 0, 0, 7, 0],
     [6, 7, 9, 3, 0, 0, 0, 0, 0],
     [7, 0, 6, 0, 4, 9, 0, 3, 0],
     [0, 9, 0, 0, 3, 0, 0, 8, 0],
     [0, 0, 3, 2, 0, 0, 0, 0, 6]]

sol = [[1, 5, 4, 7, 6, 3, 2, 9, 8],
       [8, 6, 7, 4, 9, 2, 3, 5, 1],
       [9, 3, 2, 8, 5, 1, 4, 6, 7],
       [3, 1, 5, 6, 2, 7, 8, 4, 9],
       [4, 2, 8, 9, 1, 5, 6, 7, 3],
       [6, 7, 9, 3, 8, 4, 1, 2, 5],
       [7, 8, 6, 1, 4, 9, 5, 3, 2],
       [2, 9, 1, 5, 3, 6, 7, 8, 4],
       [5, 4, 3, 2, 7, 8, 9, 1, 6]]

diff = 'Medium'


class TestSudoku(unittest.TestCase):
    # board initialization
    def testInitializeBoard(self):
        s = Sudoku(b, sol, diff)
        self.assertEqual(s.board, b, 'The board is wrong')

    def testInitializeSol(self):
        s = Sudoku(b, sol, diff)
        self.assertEqual(s.sol, sol, 'The solution board is wrong')

    def testInitializeDiff(self):
        s = Sudoku(b, sol, diff)
        self.assertEqual(s.diff, "Medium", "Wrong difficulty")

    # movement
    def testMove(self):
        pass

    # valid move

    def testValidMove(self):
        pass
    # checking a win

    def testWin(self):
        pass


if __name__ == '__main__':
    unittest.main()
