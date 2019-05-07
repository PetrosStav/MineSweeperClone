# Minesweeper Game
# Developer: Peter Stavropoulos
 
import pygame
import random
 
# Define some colors

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
grey     = ( 200, 200, 200)
blue     = (   0,   0, 255)
 
# This sets the width and height of each grid location

width  = 20
height = 20
win = False
gameover = False

# This sets the margin between each cell

margin = 5

# Check for more blanks nearby

def checkforblanks():
    if row < 9 and row > 0 and column < 9 and column > 0:
        agrid[row-1][column] = grid[row-1][column]
        agrid[row+1][column] = grid[row+1][column]
        agrid[row][column-1] = grid[row][column-1]
        agrid[row][column+1] = grid[row][column+1]
        agrid[row+1][column+1] = grid[row+1][column+1]
        agrid[row-1][column-1] = grid[row-1][column-1]
        agrid[row-1][column+1] = grid[row-1][column+1]
        agrid[row+1][column-1] = grid[row+1][column-1]
    elif row == 0 and column == 0:
        agrid[row+1][column] = grid[row+1][column]
        agrid[row][column+1] = grid[row][column+1]
        agrid[row+1][column+1] = grid[row+1][column+1]
    elif row == 9 and column == 9:
        agrid[row-1][column] = grid[row-1][column]
        agrid[row][column-1] = grid[row][column-1]
        agrid[row-1][column-1] = grid[row-1][column-1]
    elif row == 0 and column == 9:
        agrid[row+1][column] = grid[row-1][column]
        agrid[row][column-1] = grid[row][column-1]
        agrid[row+1][column-1] = grid[row+1][column-1]
    elif row == 9 and column == 0:
        agrid[row-1][column] = grid[row-1][column]
        agrid[row][column+1] = grid[row][column+1]
        agrid[row-1][column+1] = grid[row-1][column+1]
    elif row == 0:
        agrid[row+1][column] = grid[row+1][column]
        agrid[row][column-1] = grid[row][column-1]
        agrid[row][column+1] = grid[row][column+1]
        agrid[row+1][column+1] = grid[row+1][column+1]
        agrid[row+1][column-1] = grid[row+1][column-1] 
    elif row == 9:
        agrid[row-1][column] = grid[row-1][column]
        agrid[row][column-1] = grid[row][column-1]
        agrid[row][column+1] = grid[row][column+1]
        agrid[row-1][column] = grid[row-1][column]
        agrid[row-1][column+1] = grid[row-1][column+1]
    elif column == 0:
        agrid[row-1][column] = grid[row-1][column]
        agrid[row+1][column] = grid[row+1][column]
        agrid[row][column+1] = grid[row][column+1]
        agrid[row+1][column+1] = grid[row+1][column+1]
        agrid[row-1][column+1] = grid[row-1][column+1]
    elif column == 9:
        agrid[row-1][column] = grid[row-1][column]
        agrid[row+1][column] = grid[row+1][column]
        agrid[row][column-1] = grid[row][column-1]
        agrid[row-1][column-1] = grid[row-1][column-1]
        agrid[row+1][column-1] = grid[row+1][column-1]       
    
# Flags for mines

def setremoveflag():
    if grid[row][column] <> agrid[row][column]:
        if flag[row][column] == 0:
            flag[row][column] = 1
        else:
            flag[row][column] = 0

# Check if you won the game

def checkwin():
    uncovered = 0
    for row in range(10):
        for column in range(10):
            if grid[row][column] <> 10 and grid[row][column] == agrid[row][column]:
                uncovered += 1
    if uncovered == (100 - mines):
        global win
        win = True

# Check what the player clicked

def checkgrid():
    if grid[row][column] == 10:
        agrid[row][column] = 10
        global gameover
        gameover = True
    elif grid[row][column] == 9:
        agrid[row][column] = 9
    elif grid[row][column] == 1:
        agrid[row][column] = 1
    elif grid[row][column] == 2:
            agrid[row][column] = 2
    elif grid[row][column] == 3:
            agrid[row][column] = 3 
    elif grid[row][column] == 4:
            agrid[row][column] = 4
    elif grid[row][column] == 5:
            agrid[row][column] = 5
    elif grid[row][column] == 6:
            agrid[row][column] = 6
    elif grid[row][column] == 7:
            agrid[row][column] = 7
    elif grid[row][column] == 8:
            agrid[row][column] = 8

grid = []
agrid = []
flag = []

# Grid that the player clicks

for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0) # Append a cell

# Actuall grid of minesweeper

for row in range(10):
    agrid.append([])
    for column in range(10):
        agrid[row].append(0)

# Flag grid

for row in range(10):
    flag.append([])
    for column in range(10):
        flag[row].append(0)

# Set the mines

global mines
mines = 10
for i in range(mines):
    good = 0
    while good == 0:
        row = random.randint(0,9)
        column = random.randint(0,9)
        if (row == 1 or row == 9 or column == 1 or column == 9):
            if grid[row][column]<>10:
                grid[row][column] = 10
                good = 1
        elif grid[row-1][column] <> 10 and grid[row+1][column] <> 10 and grid[row][column-1] <> 10 and grid[row][column+1] <> 10 and grid[row+1][column+1] <> 10 and grid[row-1][column-1] <> 10 and grid[row+1][column-1] <> 10 and grid[row-1][column+1] <> 10 and grid[row][column]<>10:
            grid[row][column] = 10
            good = 1
for row in range(10):
    for column in range(10):
        if grid[row][column] <> 10:
            grid[row][column] = 9
print mines

# Set the numbers

# Left corner
if grid[0][0] <> 10:
    mns = 0
    if grid[0][1] == 10:
        mns += 1
    if grid[1][0] == 10:
        mns += 1
    if grid[1][1] == 10:
        mns += 1
    if mns <> 0:
        grid[0][0] = mns

# Right corner
if grid[0][9] <> 10:
    mns = 0
    if grid[0][8] == 10:
        mns += 1
    if grid[1][9] == 10:
        mns += 1
    if grid[1][8] == 10:
        mns += 1
    if mns <> 0:
        grid[0][9] = mns

# Left Down Corner
if grid[9][0] <> 10:
    mns = 0
    if grid[8][0] == 10:
        mns += 1
    if grid[8][1] == 10:
        mns += 1
    if grid[9][1] == 10:
        mns += 1
    if mns <> 0:
        grid[9][0] = mns

# Right Down Corner
if grid[9][9] <> 10:
    mns = 0
    if grid[9][8] == 10:
        mns += 1
    if grid[8][9] == 10:
        mns += 1
    if grid[8][8] == 10:
        mns += 1
    if mns <> 0:
        grid[9][9] = mns
        
# Left Column
for row in range(1,9):
    if grid[row][0] <> 10:
        mns = 0
        if grid[row-1][0] == 10:
            mns += 1
        if grid[row+1][0] == 10:
            mns += 1
        if grid[row-1][1] == 10:
            mns += 1
        if grid[row][1] == 10:
            mns += 1
        if grid[row+1][1] == 10:
            mns += 1
        if mns <> 0:
            grid[row][0] = mns

# Right Column
for row in range(1,9):
    if grid[row][9] <> 10:
        mns = 0
        if grid[row-1][9] == 10:
            mns += 1
        if grid[row+1][9] == 10:
            mns += 1
        if grid[row-1][8] == 10:
            mns += 1
        if grid[row][8] == 10:
            mns += 1
        if grid[row+1][8] == 10:
            mns += 1
        if mns <> 0:
            grid[row][9] = mns

# Top Row
for column in range(1,9):
    if grid[0][column] <> 10:
        mns = 0
        if grid[0][column-1] == 10:
            mns += 1
        if grid[0][column+1] == 10:
            mns += 1
        if grid[1][column] == 10:
            mns += 1
        if grid[1][column-1] == 10:
            mns += 1
        if grid[1][column+1] == 10:
            mns += 1
        if mns <> 0:
            grid[0][column] = mns

# Bottom Row
for column in range(1,9):
    if grid[9][column] <> 10:
        mns = 0
        if grid[9][column-1] == 10:
            mns += 1
        if grid[9][column+1] == 10:
            mns += 1
        if grid[8][column] == 10:
            mns += 1
        if grid[8][column-1] == 10:
            mns += 1
        if grid[8][column+1] == 10:
            mns += 1
        if mns <> 0:
            grid[9][column] = mns

# The Rest Grid
for row in range(1,9):
    for column in range(1,9):
        if not(grid[row][column] == 10):
                mns = 0
                if grid[row+1][column] == 10:
                    mns += 1
                if grid[row-1][column] == 10:
                    mns += 1  
                if grid[row][column+1] == 10:
                    mns += 1  
                if grid[row][column-1] == 10:
                    mns += 1
                if grid[row+1][column+1] == 10:
                    mns += 1    
                if grid[row-1][column-1] == 10:
                    mns += 1
                if grid[row+1][column-1] == 10:
                    mns += 1  
                if grid[row-1][column+1] == 10:
                    mns += 1
                if mns <> 0:    
                    grid[row][column] = mns

        
# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size = [255, 255]
screen=pygame.display.set_mode(size)
 
# Set title of screen
mines_str = str(mines)
pygame.display.set_caption("Minesweeper-Mines: "+mines_str)

#Setup the font
font = pygame.font.Font(None,30)
 
#Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and gameover == False and win == False:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            # Make sure that the box isn't flagged
            if (row < 10 and row > -1) and (column < 10 and column > -1):
                if flag[row][column] <> 1:
                    checkgrid()
                    checkwin()
            print("Click ", pos, "Grid coordinates: ", row, column)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and gameover == False and win == False:
            # User clicks right mouse button
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            setremoveflag()
 
    # Set the screen background
    screen.fill(black)
 
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = white
            pygame.draw.rect(screen,
                            color,
                            [(margin+width)*column+margin,
                            (margin+height)*row+margin,
                            width,
                            height])
            #Shows the mines - for debugging
            #if grid[row][column] == 10:
            #    color = black
            #    pygame.draw.rect(screen,
            #                    color,
            #                    [(margin+width)*column+margin,
            #                    (margin+height)*row+margin,
            #                    width,
            #                    height])            
            if flag[row][column] == 1:
                flag1 = font.render("F",True,blue)
                screen.blit(flag1,[(margin+width)*column+margin+3,
                                    (margin+height)*row+margin+2])
            if agrid[row][column] == 10:
                color = red
                pygame.draw.rect(screen,
                                 color,
                                 [(margin+width)*column+margin,
                                 (margin+height)*row+margin,
                                 width,
                                 height])
            if agrid[row][column] == 9:
                color = grey
                pygame.draw.rect(screen,
                                 color,
                                 [(margin+width)*column+margin,
                                 (margin+height)*row+margin,
                                 width,
                                 height])
                checkforblanks()
            if agrid[row][column] == 1:
                text1 = font.render("1",True,black)
                screen.blit(text1,[(margin+width)*column+margin+3,
                                    (margin+height)*row+margin+2])
            if agrid[row][column] == 2:
                text2 = font.render("2",True,black)
                screen.blit(text2,[(margin+width)*column+margin+3,
                                    (margin+height)*row+margin+2])
            if agrid[row][column] == 3:
                text3 = font.render("3",True,black)
                screen.blit(text3,[(margin+width)*column+margin+3,
                                    (margin+height)*row+margin+2])
            if agrid[row][column] == 4:
                text4 = font.render("4",True,black)
                screen.blit(text4,[(margin+width)*column+margin+3,
                                    (margin+height)*row+margin+2])
            if agrid[row][column] == 5:
                text5 = font.render("5",True,black) 
                screen.blit(text5,[(margin+width)*column+margin+3,
                                    (margin+height)*row+margin+2])
            if agrid[row][column] == 6:
                text6 = font.render("6",True,black)
                screen.blit(text6,[(margin+width)*column+margin+3,
                                    (margin+height)*row+margin+2])
            if agrid[row][column] == 7:
                text7 = font.render("7",True,black)
                screen.blit(text7,[(margin+width)*column+margin+3,
                                    (margin+height)*row+margin+2])
            if agrid[row][column] == 8:
                text8 = font.render("8",True,black)
                screen.blit(text8,[(margin+width)*column+margin+3,
                                    (margin+height)*row+margin+2])
    # Gameover
    if gameover == True:
        textover = font.render("GAME OVER!!!",True,red)
        screen.blit(textover,[50,10])
    
    # Win
    if win == True:
        textwin = font.render("YOU WON!!!",True,green)
        screen.blit(textwin,[50,10])
    
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()