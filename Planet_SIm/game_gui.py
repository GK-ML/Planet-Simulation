import pygame

class Display():
    screen_width = 100
    screen_height = 100
    fps = 10

    def __init__(self, screen_width =100, screen_height=100, fps=50, close=False, caption=" " ):
        """
         *Sets the display attributes
        """

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = fps
        self.close = close

        self.surface = pygame.display.init()
        pygame.display.set_mode((self.screen_width,self.screen_height))
        clock = pygame.time.Clock().tick(self.fps)
