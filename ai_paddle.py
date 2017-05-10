import pygame

class aiPaddle(object):
    def __init__(self,image,width,height,gameDisplay,displayWidth,displayHeight):
	self.x = displayWidth - 50
	self.y = (displayHeight / 2) - (height /2)
        self.speed = 8
	self.image = image
        self.image_rec = image.get_rect()
	self.width = width
	self.height = height
	self.gameDisplay = gameDisplay
	self.dWidth = displayWidth
	self.dHeight = displayHeight
        self.movingDown = False

        paddleImg = pygame.image.load('player_paddle.png')
        
        self.surface = pygame.Surface((width,height))



    def draw(self):
        self.gameDisplay.blit(self.image,(self.x,self.y))


    def moveD(self):
        if self.y +self.height < self.dHeight:
            self.y += self.speed
            self.movingDown = True
            #self.image_rec.move(self.x,self.y)


    def moveU(self):
        if self.y > 10:
            self.y -= self.speed
            self.movingDown = False
            #self.image_rec.move(self.x,self.y)

    
    
