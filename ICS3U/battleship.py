from cmu_graphics import *


app.background = 'black'
app.gameState = 'setup'

# background
Polygon(0, 80, 50, 50, 150, 50, 200, 80, 250, 50, 350, 50, 400, 80,
        400, 320, 350, 350, 250, 350, 200, 320, 150, 350, 50, 350, 0, 320,
        fill='mediumSeaGreen', border='limeGreen', borderWidth=6)
Label('PLAYER', 100, 330, size=25, font='monospace')
Label('ENEMY', 300, 330, size=25, font='monospace')

instructions = Label('Click to place four ships of size two', 200, 94,
                     fill='white', size=17, font='monospace', bold=True)

def makeBoard(startX, startY):
    rows = 8
    cols = 8
    gridSize = 24
    board = makeList(rows, cols)
    for row in range(rows):
        for col in range(cols):

            # Draw a rectangular cell for this row and column.
            x0 = startX + col*gridSize
            y0 = startY + row*gridSize
            cell = Rect(x0, y0, gridSize, gridSize, fill="mediumBlue", border="white", borderWidth=1)


            # Sets the cell properties and add it to the board.
            cell.status = 'ocean'
            cell.row = row
            cell.col = col
            board[row][col] = cell

    return board

app.playerBoard = makeBoard(3, 110)
app.enemyBoard = makeBoard(205, 110)
app.shipPartsPlaced = 0
app.lastClicked = None

def findCell(x, y, board):

    # Find the cell that the point (x, y) lies in.
    for i in range(8):
        for j in range(8):
            if(board[i][j].contains(x, y)):
                return board[i][j]
        


    return None

def isAdjacent(cell, cellClicked):
    # Checks if two cells are adjacent.
    clickedRow = cellClicked.row
    clickedCol = cellClicked.col
    cellRow = cell.row
    cellCol = cell.col


    # If either the rows are equal and the columns are within 1, or
    # the columns are equal and the rows are within 1, they are adjacent.
    if clickedRow == cellRow:
        if clickedCol + 1 == cellCol or clickedCol - 1 == cellCol:
            return True
    
    if clickedCol == cellCol:
        if clickedRow + 1 == cellRow or clickedRow - 1 == cellRow:
            return True
    
    return False


def isLegalShip(cell, board, numParts):
    # If the location is not an ocean, it is not legal.
    if ((cell == None) or (cell.status != 'ocean')):
        return False

    # Every ship has length 2 so if this is a new ship, it is legal.
    if (numParts % 2 == 0):
        app.lastClicked = cell
        return True
    else:
        # If we already placed the first part of a ship, make sure the second
        # part is next to the first.
        if (isAdjacent(cell, app.lastClicked) == True):
            return True
        else:
            return False

def placePlayer(mouseX, mouseY):
    cell = findCell(mouseX, mouseY, app.playerBoard)


    # Place a player ship in the cell if it will be a legal move.
    #          Also change the fill and increment app.shipPartsPlaced.)
    if isLegalShip(cell, app.playerBoard, app.shipPartsPlaced):
        cell.status = "hiddenShip"
        cell.fill = "grey"
        app.shipPartsPlaced += 1


def placeEnemies():
    # Randomly places enemy ships until there are 4 ships of size 2 on the board.
    numShipParts = 0
    while (numShipParts < 8):
        randomRow = randrange(0, 8)
        randomCol = randrange(0, 8)
        randomCell = app.enemyBoard[randomRow][randomCol]
        if (isLegalShip(randomCell, app.enemyBoard, numShipParts) == True):
            # Places the ship.
            randomCell.status = 'hiddenShip'
            numShipParts += 1

def playTurn(mouseX, mouseY):
    # On each turn, see if the cell clicked was valid.
    cell = findCell(mouseX, mouseY, app.enemyBoard)
    if (sinkOrMiss(cell) == True):
        enemyTurn()

    # Check if the game ends.
    if (checkWin(app.enemyBoard) == True):
        Rect(0, 160, 400, 90, fill='green')
        Label('YOU WON!', 200, 200, fill='white', size=30)
        app.gameState = 'over'
        app.stop()

def enemyTurn():
    # On an enemy turn, randomly pick a new cell to attack.
    newSpot = False
    while (newSpot == False):
        # Pick a random cell by choosing a row and column.
        ### (HINT: Choose the row first in order to autograde properly.)
        ### Place Your Code Here ###
        row = randrange(0, 8)
        col = randrange(0, 8)
        randomCell = app.playerBoard[row][col]
        
        # If the cell has not been attacked yet, end the loop.
        ### Place Your Code Here ###
        if randomCell.status == "ocean" or randomCell.status == "hiddenShip":
            break
        pass

    # Checks if the attacked cell is a ship then check if the game ends.
    sinkOrMiss(randomCell)
    if (checkWin(app.playerBoard) == True):
        # Draw the game lost screen.
        ### Place Your Code Here ###
        Rect(0, 160, 400, 90, fill='red')
        Label('YOU LOST!', 200, 200, fill='white', size=30)
        app.gameState = 'over'
        app.stop()
        pass

def sinkOrMiss(cell):
    if (cell != None):
        # If the cell has no ship, draws a ripple.
        if (cell.status == 'ocean'):
            cell.status = 'missed'
            drawRipple(cell)
            return True

        # If the cell has a ship, draws a hit.
        elif (cell.status == 'hiddenShip'):
            cell.status = 'hit'
            drawHit(cell)
            return True

        else:
            return False

def drawRipple(cell):
    radiusList = [ 11, 7, 3 ]
    # Draw a ripple in the cell.
    for i in range(3):
        Circle(cell.centreX, cell.centreY, radiusList[i], fill="aqua", border="blue", borderWidth=0.5)


def drawHit(cell):
    # Draw a hit as a star at the center of the cell.
    Star(cell.centreX, cell.centreY, 15, 6, roundness=30, fill=gradient("yellow", "red", "red"))
    pass


def checkWin(opponentBoard):
    # If any cell still has a hidden ship, return False.
    for i in range(8):
        for j in range(8):
            if opponentBoard[i][j].status == "hiddenShip":
                return False
                
    return True
    pass


def onMousePress(mouseX, mouseY):
    # If on the start screen, place ship parts until the player has
    # 4 ships. Then creates 4 enemy ships.
    if (app.gameState == 'setup'):
        placePlayer(mouseX, mouseY)
        if (app.shipPartsPlaced == 8):
            placeEnemies()

            # Enters playing mode.
            app.gameState = 'play'
            instructions.value = 'Guess the location of the enemy ships'

    # Otherwise play a turn.
    elif (app.gameState == 'play'):
        playTurn(mouseX, mouseY)

def onKeyPress(key):
    # Don't change this function! It is for testing purposes.
    if (key == 's'):
        for position in range(8):
            onMousePress(15 + position * 24, 115)

    if (key == 'e'):
        for col in range(8):
            cell = app.playerBoard[0][col]
            sinkOrMiss(cell)

        enemyTurn()


cmu_graphics.run()