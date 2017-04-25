import pygame
import time

#========TODO=========
# -make ai paddle img
# -fix ai paddle collisions
# -make ai paddle more interesting 
# -fix bug when ball hits top of paddle
# -fix player score and make ai score
#

pygame.init()

#window width and height
d_width = 800
d_height = 600

#=======Colors=======
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#height of paddle roughly
p_height = 100;
#Starting location for ball
b_x = d_width/2
b_y = d_height/2

gameDisplay = pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption('Python Pong')
clock = pygame.time.Clock()

pPaddleImg = pygame.image.load('player_paddle.png')

def ball(b_x, b_y, color):
    pygame.draw.circle(gameDisplay, color, (b_x,b_y), 10, 0)

def p_paddle(x,y):
    gameDisplay.blit(pPaddleImg,(x,y))


def ai_paddle(x,y):
    gameDisplay.blit(pPaddleImg,(x,y))



    

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def score_player(score_p):
    text = pygame.font.Font('freesansbold.ttf', 75)
    TextSurf, TextRect = text_objects(score_p, text)
    TextRect.center = ((d_width/2),(d_height/8))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def score_ai(score_p):
    text = pygame.font.Font('freesansbold.ttf', 75)
    TextSurf, TextRect = text_objects(score_p, text)
    TextRect.center = ((d_width/2),(d_height/8))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def game_loop():
    #balls x and y starting pos
    b_x = (d_width / 2)
    b_y = (d_height / 2)

    #players paddle x and y starting pos
    x = (d_width * 0.05)
    y = (d_height / 2) - 45

    #ai paddle starting pos
    ai_x = (d_width * 0.95)
    ai_y = (d_height / 2) - 45
    
    #initialize paddle speed
    y_change = 0

    #initialize ball direction
    b_x_speed = 4
    b_y_speed = 0

    #dont exit game instantly (duh)
    gameExit = False;

    #loop for most everything i guess
    while not gameExit:
        for event in pygame.event.get():
            #exit game 
            if event.type == pygame.QUIT:
                gameExit = True
            #if a key is  pressed    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameExit = True
                    game_loop()
                #if up is pressed move up
                if event.key == pygame.K_UP and y > 10:
                    y_change = -4
                #if down is pressed move down
                if event.key == pygame.K_DOWN and y < d_height - p_height:
                    y_change = 4
               
            #if ey released, stop moving        
	    if event.type == pygame.KEYUP:
                if (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                    y_change = 0
                
            
        #move players paddle
        y += y_change
        
        #render background black
        gameDisplay.fill(black)
        
#============Everything you draw comes after this!!==========================
        #Draw ball
        ball(b_x,b_y,white)
        
        #ball logic!
        b_x -= b_x_speed
        b_y += b_y_speed
        
        #Flip balls y direction if hits top or bottom
        if b_y > d_height - 10 or b_y < 10:
            b_y_speed = -b_y_speed
        if b_x > d_width -10:
            b_x_speed = - b_x_speed
            
        #render player paddle 
        p_paddle(x,y)

#==================== Enemy ai paddle logic ====================
        #ai is a bit of a stretch here.... 
        ai_y = b_y *0.9 - 40
        
        #idea. if ball_x is within 15 pixels, have a 10-30% chance of randomly jerking other direction to throw player off
        #idea. if ball_y within 40 pixels of bottom / top and x > 200 away from screen wdith, start moving paddle slowly in other direction

        
        #render ai paddle
        ai_paddle(ai_x,ai_y)
        
        #render scores
        score_player('0')
        score_ai('0')
        
        #stop player from exiting screen
        if y  > d_height - p_height or y < 10:
            y_change = 0;

        #Logic for ball collisions
        if y < b_y + 10:
            #Rather lengthy collision check for player paddle
            if (x < b_x and x+30 > b_x) and (y <  b_y+10 and  y+100 > b_y+ 10):
                b_x_speed = -b_x_speed
                b_y_speed += y_change /2
           # same lengthy collision check but for ai. probably a more efficient way to handle this
           #this does not work. fix this !
            if (ai_x < b_x+10 and ai_x-30 > b_x+10) and (ai_y <  b_y and  ai_y+100 > b_y+ 10):
               b_x_speed = -b_x_speed
               b_y_speed += y_change /2
        pygame.display.update()
        clock.tick(120)

game_loop()        
pygame.quit()

quit()
