import pygame

class Paddle(object):
    def __init__(self,x,y,image,width,height,gameDisplay,displayWidth,displayHeight):
	self.x = x
	self.y = y
        self.speed = 8
	self.image = image
        self.image_rec = image.get_rect()
	self.width = width
	self.height = height
	self.gameDisplay = gameDisplay
	self.dWidth = displayWidth
	self.dHeight = displayHeight

        paddleImg = pygame.image.load('player_paddle.png')
        
        self.surface = pygame.Surface((width,height))



    def draw(self):
        self.gameDisplay.blit(self.image,(self.x,self.y))


    def moveD(self):
        self.y += self.speed
        self.image_rec.move(self.x,self.y)


    def moveU(self):
        self.y -= self.speed
        self.image_rec.move(self.x,self.y)

    
    
