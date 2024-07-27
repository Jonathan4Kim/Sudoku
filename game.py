from sudoku import Sudoku
import pygame
import requests
from pygame.locals import QUIT, MOUSEWHEEL


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
        self.surface = pygame.Surface((1200, 900))
        self.surface.fill(color=pygame.Color(251, 255, 241))
        # draw the grid and initial board and then blit grid onto screen
        self.drawGrid()
        self.drawBoard()
        self.screen.blit(self.surface, (0, 0))
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
            pygame.draw.line(self.surface, (0, 0, 0), (0, val), (900, val))

        # Draw vertical lines
        for val in values:
            pygame.draw.line(self.surface, (0, 0, 0), (val, 0), (val, 900))

        # Additional lines for the outer boundary if needed
        pygame.draw.line(self.surface, (0, 0, 0), (0, 900), (900, 900))
        pygame.draw.line(self.surface, (0, 0, 0), (900, 0), (900, 900))

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
                self.screen.blit(val, (axis[i], axis[j]))
        # display flip to see changes
        pygame.display.flip()

    def playGame(self):
        """
        Description: None
        Args: None
        Returns: None
        """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == MOUSEWHEEL:
                    pass
                    # can access properties with
                    # proper notation(ex: event.y) pygame.key.key_code()¶
            self.drawBoard()
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
