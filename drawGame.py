import config
import button
import generateBoard
import pygame
import copy

class DrawGame:
    def __init__(self, window, grid, solution, selectedCell, boardButtons, lockedCells, incorrectCells, font, solutionShown):
        self.window = window
        self.grid = grid
        self.solution = solution
        self.selectedCell = selectedCell
        self.boardButtons = boardButtons
        self.lockedCells = lockedCells
        self.incorrectCells = incorrectCells
        self.font = font
        self.solutionShown = solutionShown
        self.tempGrid = []
        self.load()
        self.loadButtons()




##########################################################################################################################
################################## MAIN ##################################################################################
##########################################################################################################################

    def draw(self):
        
        self.window.fill((config.WHITE))
        for item in self.boardButtons:
            item.draw(self.window)
        if self.selectedCell:
            self.drawSelection(self.window, self.selectedCell)


        self.shadeLockedCells(self.window, self.lockedCells)
        if len(self.incorrectCells) == 1:
            self.shadeIncorrectCells(self.window, self.incorrectCells)
        self.drawNumbers(self.window)

        self.drawGrid(self.window)
        pygame.display.update()




##########################################################################################################################
################################## BUTTONS ###############################################################################
##########################################################################################################################

    def drawGrid(self, window):
        pygame.draw.rect(window, config.BLACK, (
            config.GRID_POS[0], config.GRID_POS[1], config.CONSOLE_WIDTH-150, config.CONSOLE_HEIGHT-150), 2)
        self.horizontalLine(window)
        self.verticalLine(window)

    def horizontalLine(self, window):
        for x in range(9):
            if x % 3 == 0:
                pygame.draw.line(window, config.BLACK, (config.GRID_POS[0]+(
                    x*config.CELL_SIZE), config.GRID_POS[1]), (config.GRID_POS[0]+(x*config.CELL_SIZE), config.GRID_POS[1]+450), 2)
            else:
                pygame.draw.line(window, config.BLACK, (config.GRID_POS[0]+(
                    x*config.CELL_SIZE), config.GRID_POS[1]), (config.GRID_POS[0]+(x*config.CELL_SIZE), config.GRID_POS[1]+450))

    def verticalLine(self, window):
        for x in range(9):
            if x % 3 == 0:
                pygame.draw.line(window, config.BLACK, (config.GRID_POS[0], (
                    x*config.CELL_SIZE)+config.GRID_POS[1]), (config.GRID_POS[0]+450, (x*config.CELL_SIZE)+config.GRID_POS[1]), 2)
            else:
                pygame.draw.line(window, config.BLACK, (config.GRID_POS[0], (
                    x*config.CELL_SIZE)+config.GRID_POS[1]), (config.GRID_POS[0]+450, (x*config.CELL_SIZE)+config.GRID_POS[1]))

    def textToScreen(self, window, text, pos):
        font = self.font.render(text, False, config.BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        fontWidthAlign = (config.CELL_SIZE - fontWidth)//2
        fontHeightAlign = (config.CELL_SIZE - fontHeight)//2
        window.blit(font, (pos[0]+fontWidthAlign, pos[1]+fontHeightAlign))

    def drawNumbers(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    xPos = (xidx * config.CELL_SIZE) + config.GRID_POS[0]
                    yPos = (yidx *config.CELL_SIZE) + config.GRID_POS[1]
                    pos = xPos, yPos 
                    self.textToScreen(window, str(num), pos)

    def load(self):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    self.lockedCells.append([xidx, yidx])

    def shadeLockedCells(self, window, lockedCells):
        for cells in lockedCells:
            pygame.draw.rect(window, config.LOCKED_CELL_COLOR, ((cells[0] * config.CELL_SIZE) + config.GRID_POS[0], (
                cells[1] * config.CELL_SIZE) + config.GRID_POS[1], config.CELL_SIZE, config.CELL_SIZE))

    def drawSelection(self, window, position):
        pygame.draw.rect(window, config.LIGHT_BLUE, ((position[0]*config.CELL_SIZE)+config.GRID_POS[0], (
            position[1]*config.CELL_SIZE)+config.GRID_POS[1], config.CELL_SIZE, config.CELL_SIZE))


    def shadeIncorrectCells(self, window, incorrectCells):
        if incorrectCells [0] == 0:
            incorrectCells = []
        for cells in incorrectCells:
            pygame.draw.rect(window, config.INCORRECT_CELL_COLOR, ((cells[0] * config.CELL_SIZE) + config.GRID_POS[0], (
                cells[1] * config.CELL_SIZE) + config.GRID_POS[1], config.CELL_SIZE, config.CELL_SIZE))


##########################################################################################################################
################################## BUTTONS ###############################################################################
##########################################################################################################################

    def loadButtons(self):
        self.boardButtons.append(button.Button(20, 40, 120, 40, "Quit Game", self.quitGame))
        self.boardButtons.append(button.Button(240, 40, 120, 40, "Play Again", self.playAgain))
        self.boardButtons.append(button.Button(460, 40, 120, 40, "Show Solution", self.showSolution))


    def quitGame(self):
        pygame.quit()
        quit()

    def showSolution(self):
        
        if  not self.solutionShown and len(self.tempGrid) == 0:
            self.solutionShown = not self.solutionShown
            self.tempGrid = copy.deepcopy(self.grid)
            self.grid = copy.deepcopy(config.SOLUTION)
        self.boardButtons.pop()
        self.boardButtons.append(button.Button(460, 40, 120, 40, "Hide Solution", self.hideSolution ))
        
        
        

    def hideSolution(self):
        
        if   self.solutionShown and len(self.tempGrid) != 0:
            self.solutionShown = not self.solutionShown
            self.grid = copy.deepcopy(self.tempGrid)
            self.tempGrid = []
        self.boardButtons.pop()
        self.boardButtons.append(button.Button(460, 40, 120, 40, "Show Solution", self.showSolution ))
        
            
    def playAgain(self):
        config.SOLUTION = generateBoard.make_board()
        config.board = copy.deepcopy(config.SOLUTION)
        config.NEW_BOARD = generateBoard.clearBoard(config.board)
        self.grid = copy.deepcopy(config.NEW_BOARD)
        if self.solutionShown:
            self.tempGrid = []
            self.solutionShown = False
            self.boardButtons.pop()
            self.boardButtons.append(button.Button(460, 40, 120, 40, "Show Solution", self.showSolution ))
        self.lockedCells = []
        self.load()
        self.draw()


