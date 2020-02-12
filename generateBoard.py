import random


def make_board():

    board = [[None for _ in range(9)] for _ in range(9)]

    def search(c=0):
        "Recursively search for a solution starting at position c."
        i, j = divmod(c, 9)
        i0, j0 = i - i % 3, j - j % 3 # Origin of mxm block
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+3]         # block
                        for row in board[i0:i])): 
                board[i][j] = x
                if c + 1 >= 81 or search(c + 1):
                    return board
        else:
            # No number is valid in this cell: backtrack and try again.
            board[i][j] = None
            return None

    return search()

def printBoard( board):
        spacer = "++---+---+---++---+---+---++---+---+---++"
        print (spacer.replace('-','='))
        for i,line in enumerate(board):
            print("|| {} | {} | {} || {} | {} | {} || {} | {} | {} ||"
        .format(*(cell or ' ' for cell in line)))
            if (i+1) % 3 == 0: print(spacer.replace('-','='))
            else: print(spacer)



#A function to check if the grid is full
def checkGrid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False

  #We have a complete grid!  
  return True 

#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def solveGrid(grid, counter):
  
  #Find next empty cell
  for i in range(0,81):
    row, col = divmod(i, 9)
    rowOrigin, colOrigin = row - row % 3, col - col % 3 # Origin of mxm block
    if grid[row][col]==0:
      for x in range (1,10):
            if (x not in grid[row]                     # row
                and all(gridRow[col] != x for gridRow in grid) # column
                and all(x not in row[colOrigin:colOrigin+3]         # block
                        for gridRow in grid[row:row])):
            
                square=[grid[row][colOrigin:colOrigin+3] for i in range(rowOrigin,rowOrigin+3)]
            
                #Check that this value has not already be used on this 3x3 square
                if not x in (square[0] + square[1] + square[2]):
                    grid[row][col]=x
                    if checkGrid(grid):
                        counter[0]+=1
                        break
                    else:
                        if solveGrid(grid, counter):
                            return True
      break
  grid[row][col]=0 


def clearBoard(solution):
    counter = []
    counter.append(0)
    attempts = 5
    while attempts>0:
        #Select a random cell that is not already empty
        row = random.randint(0,8)
        col = random.randint(0,8)
        while solution[row][col]==0:
            row = random.randint(0,8)
            col = random.randint(0,8)
        #Remember its cell value in case we need to put it back  
        backup = solution[row][col]
        solution[row][col]=0
        
        #Take a full copy of the grid
        copyGrid = []
        for r in range(0,9):
            copyGrid.append([])
            for c in range(0,9):
                copyGrid[r].append(solution[r][c])
        
        #Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
        counter[0]=0      
        solveGrid(copyGrid, counter)   
        #If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
        if counter[0]!=1:
            solution[row][col]=backup
            #We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
            attempts -= 1

    return solution
