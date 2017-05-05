
import pygame
import random
#pygame.init()


class Ball(object):
    def __init__(self,x,y,image,gameDisplay,displayWidth,displayHeight):
        #initilize anything later on
        #self.vel = [1,1]
        #used for collisions
	self.x = x
	self.y = y
	self.diameter  = 20
       	self.image = image
	self.gameDisplay = gameDisplay
	self.speed = 1
	self.dWidth = displayWidth
	self.dHeight = displayHeight

	self.movingDown = True
	self.movingRight = True
	#self.draw(gameDisplay)

    def draw(self):
        self.gameDisplay.blit(self.image,(self.x,self.y))

    
        
    def move(self,x,y):
	
	if(self.x + self.diameter > self.dWidth):
		self.movingRight = False
	if(self.x < 0):
		self.movingRight = True
	if(self.y + self.diameter > self.dHeight):
        	self.movingDown = False
	if(self.y < 0):
		self.movingDown = True
	if self.movingRight:	
		self.x += x * self.speed
	else:
		self.x -= x * self.speed
	if self.movingDown:
		self.y += y * self.speed
        else:
		self.y -= y * self.speed
   # def hit_paddle(paddle_player, paddle_ai):
        
       # if x<paddle_player.x+paddle_width and y > player_paddle.y and y+diameter > player_paddle.y+paddle_height:
            
            
    def run(self,x,y,):
        self.move(x,y)
	self.draw()
        
        
