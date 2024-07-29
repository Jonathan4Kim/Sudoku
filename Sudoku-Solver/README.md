# Sudoku Solver
This code implements a Sudoku solver and game using Python and Tkinter for the graphical user interface. Below is a detailed explanation of the main components and how they work together.

### Main Components

1. **SudokuError Class:**
   - A custom exception class for handling application-specific errors.

2. **SudokuBoard Class:**
   - Represents the Sudoku board.
   - `create_board` method initializes the board from a string of 81 characters where '*' represents an empty cell.

3. **SudokuGame Class:**
   - Manages the state of the Sudoku game.
   - `start` method initializes the game.
   - `check_valid` method validates the current state of the board by checking rows, columns, and 3x3 boxes.

4. **SudokuUI Class:**
   - Responsible for the graphical user interface using Tkinter.
   - Methods like `draw_grid` and `draw_puzzle` handle the rendering of the board.
   - `solve_click_*` methods call different solving algorithms from the `Sudoku` class to solve the puzzle and update the UI.

5. **Sudoku Class:**
   - Implements various Sudoku solving algorithms.
   - `sudoku_cells` returns all possible cell coordinates on the board.
   - `sudoku_arcs` and `get_arcs` handle the arc consistency for solving algorithms.
   - `read_board` reads a board from a file.
   - `unique_cell` checks if a cell value is unique in its row, column, and 3x3 box.

### UI Components

- **Canvas:** The main drawing area for the Sudoku grid.
- **Buttons:** Allow the user to clear the board, solve the puzzle using different algorithms, and reset the puzzle.
- **Entry:** A text entry for users to input a new Sudoku puzzle.

### Solving Algorithms

- **AC3 (Arc Consistency 3):** Implements arc consistency algorithm.
- **Improved AC3:** A more efficient version of the AC3 algorithm.
- **AC3 with Guessing:** Combines AC3 with a guessing mechanism to solve harder puzzles.

### Main Execution

- Initializes a Sudoku game with a sample puzzle.
- Creates a Tkinter root window and starts the `SudokuUI`.
- Runs the Tkinter main loop to handle user interactions.

### Sample Execution

Here is how you can run this Sudoku solver and GUI:

```python
if __name__ == '__main__':
    game = SudokuGame('821*****7***8***6**6*93***5**82*16*****7**28424*6*37**6*5***1*3*7**5****912*****6')
    game.start()
    root = Tk()
    SudokuUI(root, game)
    root.geometry("700x500")
    root.mainloop()
```

This code initializes the game with a sample Sudoku puzzle, starts the UI, and runs the application. Users can interact with the UI to solve the puzzle using different algorithms and see the results visually.