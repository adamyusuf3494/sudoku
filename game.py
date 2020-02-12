import sys
import pygame
import config
import drawGame


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(
            (config.CONSOLE_WIDTH, config.CONSOLE_HEIGHT))
        self.running = True
        self.grid = config.NEW_BOARD
        self.solution = config.SOLUTION
        self.selectedCell = []
        self.mousePos = None
        self.boardButtons = []
        self.lockedCells = []
        self.incorrectCells = []
        self.font = pygame.font.SysFont('arial', config.CELL_SIZE//2)
        self.solutionShown = False
        self.board = drawGame.DrawGame(self.window, self.grid, self.solution, self.selectedCell, self.boardButtons, self.lockedCells, self.incorrectCells, self.font, self.solutionShown)
        

    def play(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

##################################################################################################################################
##################################################### PLAY #######################################################################
##################################################################################################################################

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = self.mouseonGrid()
                if cell:
                    self.selectedCell = cell

            # Key in number
            if event.type == pygame.KEYDOWN:
                if self.selectedCell != None and self.selectedCell not in self.lockedCells:
                    if self.isNumber(event.unicode):
                        # cell changed
                        self.incorrectCells = []
                        self.grid[self.selectedCell[1]][self.selectedCell[0]] = int(event.unicode)
                        if self.solution[self.selectedCell[1]][self.selectedCell[0]] != int(event.unicode):
                            if self.grid[self.selectedCell[1]][self.selectedCell[0]] == 0:
                                self.board.drawSelection(self.window, (self.selectedCell[1], self.selectedCell[0]))
                            else:
                                self.incorrectCells.append([self.selectedCell[0], self.selectedCell[1]])

    def update(self):
        self.mousePos = pygame.mouse.get_pos()
        for item in self.boardButtons:
            item.update(self.mousePos)

    def draw(self):
        self.board.selectedCell = self.selectedCell
        self.board.incorrectCells = self.incorrectCells
        self.board.draw()


#################################################################################################################################
############################################################ FUNCTION ###########################################################
#################################################################################################################################

    
    def mouseonGrid(self):
        if self.mousePos[0] < config.GRID_POS[0] or self.mousePos[1] < config.GRID_POS[1]:
            self.selectedCell = []
            return False
        if self.mousePos[0] > config.GRID_POS[0]+config.GRID_SIZE or self.mousePos[1] > config.GRID_POS[1]+config.GRID_SIZE:
            self.selectedCell = []
            return False
        return ((self.mousePos[0]-config.GRID_POS[0])//config.CELL_SIZE, (self.mousePos[1]-config.GRID_POS[1])//config.CELL_SIZE)

    def isNumber(self, string):
        try:
            int(string)
            return True
        except:
            return False
        