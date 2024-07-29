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
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.screen = pygame.display.set_mode((1200, 900), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.color = pygame.color.Color(0, 0, 0)
        # fill screen with background and instantiate surface with same color
        self.screen.fill(color=pygame.Color(251, 255, 241))
        self.surface = pygame.Surface((925, 925))
        # draw the grid and initial board and then blit grid onto screen
        self.drawSudoku()

    def drawSudoku(self):
        """
        Draws the Sudoku Board.
        """
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
        # get initial points: should be drawn differently
        initial = self.sudoku.getInitial()
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
                if (i, j) in initial:
                    val = font.render(str(board[i][j]), True,
                                      pygame.Color(1, 25, 120))
                    self.surface.blit(val, (axis[i], axis[j]))
                    continue
                val = font.render(str(board[i][j]), True, self.color)
                self.surface.blit(val, (axis[i], axis[j]))

    def drawSideBar(self):
        # create surface for sidebar
        surface = pygame.Surface((250, 900))
        surface.fill(color=pygame.Color(251, 255, 241))
        titleFont = pygame.font.Font(None, 200)

        # title rendering
        title = "Sudoku"
        titleVal = titleFont.render(title, True, self.color)
        self.screen.blit(titleVal, (915, 50))
        diffFont = pygame.font.Font(None, 75)

        # difficulty rendering
        diffVal = diffFont.render("Difficulty: " + self.sudoku.getDiff(),
                                  True, self.color)
        self.screen.blit(diffVal, (950, 210))

        # new game rendering


        # check for win condition/print you won!
        if self.sudoku.win():
            winFont = pygame.font.Font(None, 100)
            winVal = winFont.render("You won!", True,
                                    pygame.color(0, 255, 0))
            self.screen.blit(winVal, (950, 800))

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
                            if event.key in (pygame.K_1, pygame.K_2,
                                             pygame.K_3, pygame.K_4,
                                             pygame.K_5, pygame.K_6,
                                             pygame.K_7, pygame.K_8,
                                             pygame.K_9):
                                self.sudoku.move(x, y, int(event.unicode))
                                self.drawSudoku()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_MINUS:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    mouse_clicked = True
                    # handle buttons here like save game, check game

            self.screen.fill(pygame.Color(251, 255, 241))
            self.drawSudoku()
            pygame.display.flip()
            self.clock.tick(60)

        # quit the game
        pygame.quit()


if __name__ == "__main__":
    # initialize pygame instance
    pygame.init()
    # pygame display
    pygame.display.init()
    # pygame caption
    pygame.display.set_caption("Sudoku Game")
    # make the mouse visible
    pygame.mouse.set_visible(True)
    # create game instance
    game = Game()
    # play the game/run loop
    game.playGame()
