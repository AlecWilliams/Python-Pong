
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
	self.movingRight = False
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
                #self.image_rec =  self.image_rec.move(self.x,self.
            

    #Player paddle collisions
    def playerCollision(self,playerP):
        #Collisions for front of player paddle
        if (self.y > playerP.y and self.y < playerP.y + 100) and (self.x <= playerP.x + 20):
            if self.movingRight:
                self.movingRight = False
            else:
                self.movingRight = True
            #check which way player is moving and create more if statements as
            #necesarry to create correct movement
            if self.movingDown and playerP.movingDown:
                self.movingDown = True
            if not self.movingDown:
                self.movingDown = False
            else:
                self.movingDown = True
            
        #Collisions for top of player paddle
        if (self.x+10 > playerP.x and self.x < playerP.x + 20) and (self.y + 25  >= playerP.y and self.y + 25 < playerP.y+10):
            self.movingDown = False
            print('Top Hit')
#====================================================#
    #aiPaddle collisions
    def aiCollision(self,playerP):
        #Collisions for front of player paddle
        if (self.y > playerP.y and self.y < playerP.y + 100) and (self.x+10 >= playerP.x):
            if self.movingRight:
                self.movingRight = False
            else:
                self.movingRight = True
            
            if self.movingDown and playerP.movingDown:
                self.movingDown = True
            if not self.movingDown:
                self.movingDown = False
            else:
                self.movingDown = True
            
        #Collisions for top of player paddle
        if (self.x+10 > playerP.x and self.x < playerP.x) and self.y + 25  >= playerP.y:
            self.movingDown = False
            print('Top Hit AI')
                

    
    def run(self,x,y,playerSpr,aiPaddle):
        self.move(x,y)
        self.playerCollision(playerSpr)
        self.aiCollision(aiPaddle)
	self.draw()
        
        
