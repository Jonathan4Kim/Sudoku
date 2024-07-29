from sudoku import Sudoku
import pygame
import requests


def createBoard():
    """
    Description:
    Pulls sudoku board from Dosuku API
    (https://sudoku-api.vercel.app/)
    and creates/returns a Sudoku
    instance.
    Args: None
    Returns: Sudoku class instance
    """
    # pull from Dosuku API to get sudoku instance in json file
    r = requests.get("https://sudoku-api.vercel.app/api/dosuku").json()
    # obtain the initial board and solution arrays
    init = r['newboard']['grids'][0]['value']
    sol = r['newboard']['grids'][0]['solution']
    # pull the difficulty from the board
    difficulty = r['newboard']['grids'][0]['difficulty']
    # return a Sudoku instance using the pulled attributes necessary
    return Sudoku(init, sol, difficulty)


class Game(object):

    def __init__(self) -> None:
        """
        Description:
        Initialization of Game object.
        Contains the necessary attributes for running
        a  full game
        Args: None
        Attributes:
            self.sudoku: Sudoku instance from createBoard() function
            self.screen: pygame display (1200x900 dimensions)
            self.clock: pygame clock
            self.color: black, good for initialization, text, and lines
            Will blit onto screen.
        Returns: None
        """
        self.sudoku = createBoard()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1200, 900), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.color = pygame.color.Color(0, 0, 0)

        # fill screen with background and instantiate surface with same color
        self.screen.fill(color=pygame.Color(251, 255, 241))
        self.surface = pygame.Surface((925, 925))
        # draw the grid and initial board and then blit grid onto screen
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
        """
        Description: draws all the border lines for the Sudoku Board.
        Args: None
        Returns: None
        """
        values = [0, 100, 200, 300, 400, 500, 600, 700, 800]

        # Draw horizontal lines
        for val in values:
            if val == 0 or val == 300 or val == 600:
                pygame.draw.line(self.surface, (0, 0, 0), (0, val),
                                 (900, val), width=5)
            pygame.draw.line(self.surface, (0, 0, 0), (0, val), (900, val))

        # Draw vertical lines
        for val in values:
            if val == 0 or val == 300 or val == 600:
                pygame.draw.line(self.surface, (0, 0, 0), (val, 0),
                                 (val, 900), width=5)
            pygame.draw.line(self.surface, (0, 0, 0), (val, 0), (val, 900))
        
        # making sure 

        # Additional lines for the outer boundary if needed
        pygame.draw.line(self.surface, (0, 0, 0), (0, 900), (900, 900),
                         width=5)
        pygame.draw.line(self.surface, (0, 0, 0), (900, 0), (900, 900),
                         width=5)

    def drawBoard(self):
        """
        Description Draws the numbers.  Uses self.surface to do so.
        Args: None
        Returns: None
        """
        # create rows and necessary buffer into axis
        rows = [0, 100, 200, 300, 400, 500, 600, 700, 800]
        axis = [38 + val for val in rows]
        # get the sudoku board for values
        board = self.sudoku.getBoard()
        # create initial font
        font = pygame.font.Font(None, 55)
        # iterate through, rendering the value and blitting to screen
        for i in range(9):
            for j in range(9):
                val = font.render(str(board[i][j]), True, self.color)
                self.surface.blit(val, (axis[i], axis[j]))

    def drawSideBar(self):
        surface = pygame.Surface((250, 900))
        surface.fill(color=pygame.Color(251, 255, 241))
        titleFont = pygame.font.Font(None, 100)
        title = "Sudoku"
        titleVal = titleFont.render(title, True, self.color)
        self.screen.blit(titleVal, (900, 0))
        # buttonFont = pygame.font.Font(None, 40)

    def playGame(self):
        """
        Description: Plays the python pygame.
        Handles event types
        Args: None
        Returns: None
        """
        running = True
        mouse_clicked = False
        x, y = -1, -1
        while running:
            if self.sudoku.win():
                print("You won!")
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # turn running to False and quit game
                    running = False
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    mouse_clicked = True
                    # handle buttons here like save game, check game
                elif (event.type == pygame.KEYDOWN
                      and mouse_clicked):
                    print("I'm here")
                    print(x)
                    print(y)
                    if 0 <= x and x <= 900 and 0 <= y and y <= 900:
                        # cast to the valid box
                        x, y = x // 100, y // 100
                    if event.key == pygame.K_1:
                        self.sudoku.move(x, y, 1)
                        self.drawSudoku()
                    elif event.key == pygame.K_2:
                        self.sudoku.move(x, y, 2)
                        self.drawSudoku()
                    elif event.key == pygame.K_3:
                        self.sudoku.move(x, y, 3)
                        self.drawSudoku()
                    elif event.key == pygame.K_4:
                        self.sudoku.move(x, y, 4)
                        self.drawSudoku()
                    elif event.key == pygame.K_5:
                        self.sudoku.move(x, y, 5)
                        self.drawSudoku()
                    elif event.key == pygame.K_6:
                        self.sudoku.move(x, y, 6)
                        self.drawSudoku()
                    elif event.key == pygame.K_7:
                        self.sudoku.move(x, y, 7)
                        self.drawSudoku()
                    elif event.key == pygame.K_8:
                        self.sudoku.move(x, y, 8)
                        self.drawSudoku()
                    elif event.key == pygame.K_9:
                        self.sudoku.move(x, y, 9)
                        self.drawSudoku()
                    elif event.key == pygame.K_DELETE:
                        self.sudoku.remove(x, y, self.sudoku.getVal(x, y))
            self.clock.tick(60)


if __name__ == "__main__":
    # initialize pygame instance
    pygame.init()
    # pygame display
    pygame.display.init()
    # make the mouse visible
    pygame.mouse.set_visible(True)
    # create game instance
    game = Game()
    # play the game/run loop
    game.playGame()
