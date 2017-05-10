import pygame

class Paddle(object):
    def __init__(self,x,y,image,width,height,gameDisplay,displayWidth,displayHeight, ball = None):
        if ball is None:
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
            self.movingDown = False
            
            paddleImg = pygame.image.load('player_paddle.png')
            self.surface = pygame.Surface((width,height))
        else:
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
            self.movingDown = False

            self.ball = ball
            
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




#============aiPaddle methods below===============
#
#
    def moveAi(self):
        if self.ball.x > self.dWidth / 2:
            #if ball is above, move up
            if self.ball.y < self.y + self.height / 2:
                self.y -= self.speed
            #if ball is below, move down
            if self.ball.y > self.y+ self.height / 2:
                self.y += self.speed
            




    
