import pygame
import time
from Ball import Ball
from player_paddle import Paddle


pygame.init()

#window width and height
dWidth = 800
dHeight = 600


ballImg = pygame.image.load('ball.png')
ballImg = pygame.transform.scale(ballImg,(20,20))
playerPaddleImg = pygame.image.load('player_paddle.png')
#playerPaddleRec = playerPaddleImg.get_rect()

#=======Colors=======
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


#initialize the gameDisplay and clock
gameDisplay = pygame.display.set_mode((dWidth,dHeight))
pygame.display.set_caption('Python Pong')
clock = pygame.time.Clock()

#Initialize the objects
ball = Ball(200,200,ballImg,gameDisplay,dWidth,dHeight)
playerPaddle = Paddle(10,350,playerPaddleImg,50,100,gameDisplay,dWidth,dHeight)

x = 5
y = 5

def game_loop():
 
    #dont exit game instantly (duh)
    gameExit = False;
   
    #loop for most everything i guess
    while not gameExit:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            #exit game 
            if event.type == pygame.QUIT:
                gameExit = True
            #if a key is  pressed    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameExit = True
                    game_loop()
        if keys[pygame.K_DOWN]:
            playerPaddle.moveD()
        if keys[pygame.K_UP]:
            playerPaddle.moveU()
        #render background black
        gameDisplay.fill(black)
	
	ball.run(x,y,playerPaddle)
	playerPaddle.draw()
	


	

        pygame.display.update()
        clock.tick(60)

game_loop()        
pygame.quit()

quit()
