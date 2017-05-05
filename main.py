import pygame
import time
from Ball import Ball


pygame.init()

#window width and height
dWidth = 800
dHeight = 600


ballImg = pygame.image.load('ball.png')
ballImg = pygame.transform.scale(ballImg,(20,20))


#=======Colors=======
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)



gameDisplay = pygame.display.set_mode((dWidth,dHeight))
pygame.display.set_caption('Python Pong')
clock = pygame.time.Clock()


ball = Ball(200,200,ballImg,gameDisplay,dWidth,dHeight)
x = 5
y = 5

def game_loop():
 
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
        #render background black
        gameDisplay.fill(black)
	
	ball.run(x,y)
	


	

        pygame.display.update()
        clock.tick(60)

game_loop()        
pygame.quit()

quit()
