import pygame


class Score(object):
    def __init__(self,ball,gameDisplay,dWidth):
        self.ball = ball
        self.playerScore = 0
        self.aiScore = 0
        self.gameDisplay = gameDisplay
        self.dWidth = dWidth
        self.white = (255,0,255)

    def run(self):
        if self.ball.x <= 0:
            self.aiScore += 1
        if self.ball.x >= self.dWidth:
            self.playerScore += 1


    def textObject(self,text, font):
        textSurface = font.render(str(text), True, self.white)
        return textSurface, textSurface.get_rect()
    
    def displayScores(self):
        text = pygame.font.Font('freesansbold.ttf', 75)
        textSurf, textRect = self.textObject(self.aiScore, text)
        #textRect = self.textObject(self.playerScore, text)
        textRect.center = ((self.dWidth/4), (20))
        self.gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        



    
