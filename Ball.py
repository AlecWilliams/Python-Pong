
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
        self.image_rec = self.image.get_rect()
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
                #self.image_rec =  self.image_rec.move((self. x * self.speed),0)
	else:
		self.x -= x * self.speed
                #self.image_rec =  self.image_rec.move(self.x,self.y)
	if self.movingDown:
		self.y += y * self.speed
                #self.image_rec =  self.image_rec.move(self.x,self.y)
        else:
		self.y -= y * self.speed
                #self.image_rec =  self.image_rec.move(self.x,self.y)

        #print(self.image_rec)
 
   # def hit_paddle(paddle_player, paddle_ai):
        
       # if x<paddle_player.x+paddle_width and y > player_paddle.y and y+diameter > player_paddle.y+paddle_height:
            


    def playerCollision(self,playerP):
        if (self.y > playerP.y and self.y < playerP.y + 100) and (self.x <= playerP.x + 50):
            if self.movingRight:
                self.movingRight = False
            else:
                self.movingRight = True
            #check which way player is moving and create more if statements as
            #necesarry to create correct movement
            if self.movingDown:
                self.movingDown = False
            else:
                self.movingDown = True
            
        
            
                

    
    def run(self,x,y,playerSpr):
        self.move(x,y)
        self.playerCollision(playerSpr)
	self.draw()
        
        
