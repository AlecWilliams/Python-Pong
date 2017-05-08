import pygame


class setup():
    def _init_():#maybe add params to change size, difficulty or what not
        pygame.init()
        self.fps = 120
        
        w_width = 800
        w_height = 600

        game_exit = False
        #==Colors==
        black = (0,0,0)
        white = (255,255,255)

        gameDisplay = pygame.display.set_mode((w_width,w_height))
        pygame.display.set_caption('Python Pong')
    

    def game_loop():

        while not gme_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUITT:
                    game_exit = True

        
    
            
                    gameDisplay.fill(black)
                    pygame.display.update()
                    clock.tick(fps)

game_loop()
pygame.quit()
quit()
