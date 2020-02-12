import generateBoard
import copy

CONSOLE_WIDTH = 600
CONSOLE_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (100, 215, 235)
LOCKED_CELL_COLOR = (150, 150, 150)
INCORRECT_CELL_COLOR = (200, 125, 125)

# Boards
TEST_BOARDS = [[0 for x in range(9)] for x in range(9)]
SOLUTION = generateBoard.make_board()
board = copy.deepcopy(SOLUTION)
NEW_BOARD = generateBoard.clearBoard(board)

# Position and sizes
GRID_POS = (75, 100)
CELL_SIZE = 50
GRID_SIZE = 9*CELL_SIZE