# Import libaries
import pygame

# Set the colors of the window/ screen
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()

# Initializing the display window
size = (800,600)
screen = pygame.display.set_mode(size) # setting the screen size
pygame.display.set_caption("pong") # Giving the caption the screen

# Starting coordinates of the paddle
rect_x = 400
rect_y = 580

# Initial speed of the paddle
rect_change_x = 0
rect_change_y = 0

# Initial position of the ball
ball_x = 50
ball_y = 50

# Speed of the ball
ball_change_x = 5
ball_change_y = 5

score = 0

# Draws the paddle. Also restricts its movement between the edges of the window.
def drawrect(screen,x,y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699    
    pygame.draw.rect(screen,RED,[x,y,100,20])

# Game's main loop    
done = False
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_change_x = -6
            elif event.key == pygame.K_RIGHT:
                rect_change_x = 6
            #elif event.key == pygame.K_UP:
                #rect_change_y = -6
            #elif event.key == pygame.K_DOWN:
                #rect_change_y = 6'''            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rect_change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rect_change_y = 0            
    screen.fill(BLACK) # screen fill with the black
    rect_x += rect_change_x
    rect_y += rect_change_y
    
    ball_x += ball_change_x
    ball_y += ball_change_y

    # This handles the movement of the ball.
    if ball_x<0: # if we hits the base we want to change the direction
        ball_x=0
        ball_change_x = ball_change_x * -1
    elif ball_x>785:
        ball_x=785
        ball_change_x = ball_change_x * -1
    elif ball_y<0:
        ball_y=0
        ball_change_y = ball_change_y * -1
    elif ball_x>rect_x and ball_x<rect_x+100 and ball_y==565:
        ball_change_y = ball_change_y * -1
        score = score + 1 # when ball hits on the paddle increase the score
    elif ball_y>600:
        ball_change_y = ball_change_y * -1
        score = 0  # when ball misses the paddle the score will be 0                      
    pygame.draw.rect(screen,WHITE,[ball_x,ball_y,15,15])

    # Drawball(screen,ball_x,ball_y)
    drawrect(screen,rect_x,rect_y)

    # Score board
    font= pygame.font.SysFont('Calibri', 15, False, False)
    text = font.render("Score = " + str(score), True, WHITE)
    screen.blit(text,[600,100])    

    pygame.display.flip()         
    clock.tick(60) # 60 frame per second

pygame.quit()   