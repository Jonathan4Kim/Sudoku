# Classic Sudoku in Pygame

## Overview

This project is a classic Sudoku game built using Pygame. The purpose of this project is to learn more about Pygame's capabilities, understand how to pull data from APIs using the `requests` library, and practice encapsulating drawing and game logic in different classes.

## Features

- **Dynamic Sudoku Board**: Fetches a new Sudoku board from the Dosuku API each time the game starts.
- **User Interaction**: Allows users to input numbers into the Sudoku grid and check their progress.
- **Pygame Integration**: Utilizes Pygame for rendering the board, handling user inputs, and managing the game loop.
- **Encapsulation**: Separates drawing logic and game logic into distinct classes for better code organization and maintainability.

## Technologies Used

- Python
- Pygame
- Requests

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/classic-sudoku-pygame.git
    cd classic-sudoku-pygame
    ```

2. **Install the dependencies**:
    ```bash
    pip install pygame requests
    ```

3. **Run the game**:
    ```bash
    python main.py
    ```

## How to Play

1. **Start the Game**:
    - Run the script and the game window will open in full screen mode.

2. **Game Controls**:
    - Click on a cell to select it.
    - Use number keys (1-9) to input numbers into the selected cell.
    - Press `Escape` to quit the game.
    - Press `F11` to toggle full screen mode.
    - Press `-` to stop the game.

3. **New Game**:
    - Click the "New Game" button on the right sidebar to fetch a new Sudoku puzzle from the API.

## Code Structure

- **`main.py`**: Contains the game loop, event handling, and rendering logic.
- **`sudoku.py`**: Defines the `Sudoku` class which encapsulates the game logic.

## Example Code

```python
from sudoku import Sudoku
import pygame
import requests

def createBoard():
    r = requests.get("https://sudoku-api.vercel.app/api/dosuku").json()
    init = r['newboard']['grids'][0]['value']
    sol = r['newboard']['grids'][0]['solution']
    difficulty = r['newboard']['grids'][0]['difficulty']
    return Sudoku(init, sol, difficulty)

class Game(object):
    def __init__(self) -> None:
        self.sudoku = createBoard()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.color = pygame.color.Color(0, 0, 0)
        self.screen.fill(color=pygame.Color(251, 255, 241))
        self.surface = pygame.Surface((925, 925))
        self.drawSudoku()

    def drawSudoku(self):
        self.surface = pygame.Surface((925, 925))
        self.surface.fill(color=pygame.Color(251, 255, 241))
        self.drawBoard()
        self.drawGrid()
        self.screen.blit(self.surface, (0, 0))
        self.drawSideBar()
        pygame.display.flip()

    def drawGrid(self):
        values = [0, 100, 200, 300, 400, 500, 600, 700, 800]
        for val in values:
            if val == 0 or val == 300 or val == 600:
                pygame.draw.line(self.surface, (0, 0, 0), (0, val), (900, val), width=5)
            pygame.draw.line(self.surface, (0, 0, 0), (0, val), (900, val))
        for val in values:
            if val == 0 or val == 300 or val == 600:
                pygame.draw.line(self.surface, (0, 0, 0), (val, 0), (val, 900), width=5)
            pygame.draw.line(self.surface, (0, 0, 0), (val, 0), (val, 900))
        pygame.draw.line(self.surface, (0, 0, 0), (0, 900), (900, 900), width=5)
        pygame.draw.line(self.surface, (0, 0, 0), (900, 0), (900, 900), width=5)

    def drawBoard(self):
        initial = self.sudoku.getInitial()
        rows = [0, 100, 200, 300, 400, 500, 600, 700, 800]
        axis = [38 + val for val in rows]
        board = self.sudoku.getBoard()
        font = pygame.font.Font(None, 55)
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    continue
                if (i, j) in initial:
                    val = font.render(str(board[i][j]), True, pygame.Color(1, 25, 120))
                    self.surface.blit(val, (axis[i], axis[j]))
                    continue
                val = font.render(str(board[i][j]), True, self.color)
                self.surface.blit(val, (axis[i], axis[j]))

    def drawSideBar(self):
        surface = pygame.Surface((250, 900))
        surface.fill(color=pygame.Color(251, 255, 241))
        titleFont = pygame.font.Font(None, 200)
        rect = pygame.Rect(950, 300, 450, 100)
        pygame.draw.rect(self.screen, color=self.color, rect=rect, width=5)
        newGameFont = pygame.font.Font(None, 75)
        newGameVal = newGameFont.render("New Game", True, self.color)
        self.screen.blit(newGameVal, (1025, 325))
        title = "Sudoku"
        titleVal = titleFont.render(title, True, self.color)
        self.screen.blit(titleVal, (915, 50))
        diffFont = pygame.font.Font(None, 75)
        diffVal = diffFont.render("Difficulty: " + self.sudoku.getDiff(), True, self.color)
        self.screen.blit(diffVal, (950, 210))
        if self.sudoku.win():
            winFont = pygame.font.Font(None, 100)
            winVal = winFont.render("You won!", True, pygame.color(0, 255, 0))
            self.screen.blit(winVal, (950, 800))

    def playGame(self):
        running = True
        mouse_clicked = False
        while running:
            if self.sudoku.win():
                print("You won!")
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_F11:
                        self.toggle_fullscreen()
                    elif mouse_clicked:
                        x, y = pygame.mouse.get_pos()
                        if 0 <= x <= 900 and 0 <= y <= 900:
                            x, y = x // 100, y // 100
                            if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                                self.sudoku.move(x, y, int(event.unicode))
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_MINUS:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 950 <= x and x <= 1400 and 300 <= y and y <= 400:
                        self.sudoku = createBoard()
                    mouse_clicked = True
            self.screen.fill(pygame.Color(251, 255, 241))
            self.drawSudoku()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption("Sudoku Game")
    pygame.mouse.set_visible(True)
    game = Game()
    game.playGame()
```

---