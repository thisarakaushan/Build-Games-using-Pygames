# PART 01..............................................................

# Import libaries
import pygame,sys
import time
import random

# Initialize
pygame.init()

# Setting the screen size
white = (255,255,255)
black = (100,0,0)
red = (255,0,0)

window_width = 800
window_height = 600

gameDisplay = pygame.display.set_mode((window_width,window_height)) # setting the screen size
pygame.display.set_caption('slither') # Giving the caption the screen


# PART 02..............................................................

# Refresh the screen 
clock = pygame.time.Clock()

# Screen get refresh 5 times per second
FPS = 5 # FPS - Frame Per Second

blockSize = 20 # block - size of the snake head
noPixel = 0

'''
sizeGrd = window_width // blockSize
row = 0
col = 0
for nextline in range(sizeGrd):
'''

def myquit():
    ''' Self explanatory '''
    pygame.quit()
    sys.exit(0)

font = pygame.font.SysFont(None, 25, bold=True)

def drawGrid():
    sizeGrd = window_width // blockSize
    

# PART 03..............................................................

# snakelist - no. of block in the snake
def snake(blockSize, snakelist):

    #x = 250 - (segment_width + segment_margin) * i
    for size in snakelist:
        pygame.draw.rect(gameDisplay, black,[size[0]+5,size[1],blockSize,blockSize],2)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/2, window_height/2])
    

# PART 04..............................................................

def gameLoop():
    gameExit = False # Quit from the game
    gameOver = False # Restart a new game after gameover

    lead_x = window_width/2
    lead_y = window_height/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    snakelist = []
    snakeLength = 1 # when it starts snake length is 1, means only 1 block

    # create the random x and y and generate the apple
    randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0

    while not gameExit: # Start the game when somebody says exit
        
        # Give the lives
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press c to play again or Q to quit", red)
            pygame.display.update()
    
            # Getting the data, what action we want to perform
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: # quit
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c: # continue
                        gameLoop()
                        
        # Logic 01 (Check the keys and events).............................
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()
                
                # checking the key what they are clicking like Right, left, up, Down
                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN

                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel
                elif upArrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel
                elif downArrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel
                    
                    
         # Logic 02 (Check the boundries/ window).............................
        
            # Maintain the boundries
            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True

        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        gameDisplay.fill(white)

        AppleThickness = 20
        
        # Logic 03 (Generate apples and the places).............................
        
        # Generate the random apple in the screen
        print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        pygame.draw.rect(gameDisplay, red, [randomAppleX,randomAppleY,AppleThickness,AppleThickness])

        allspriteslist = []
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)

        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist [:-1]:
            if eachSegment == allspriteslist:
                gameOver = True
                
        # Logic 04 (Draw the snake).............................
        
        # Draw Snake
        snake(blockSize, snakelist)

        pygame.display.update()
        
        # Logic 05.............................
        
        # Eat the apple from the snake
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
                randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0
                snakeLength += 1
        
        # clock is refresh        
        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()