import os, sys
import pygame
from pygame.locals import *
class PyManMain:
    def __init__(self, width=640,height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
    def MainLoop(self):
        # pygame.draw.rect(self.screen, (0, 80, 0), Rect(10, 10, 80, 50), 5)
        # pygame.display.update()
        # pygame.draw.ellipse(self.screen,(0,100,0),(50,50,200,100))
        # pygame.display.update()
        # while 1:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             sys.exit()
        x = 100
        y = 200
        while 1:
            pygame.display.update()
            pygame.time.wait(30)
            pygame.draw.circle(self.screen, (0, 200, 0), (x, y), 5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_LEFT:
                        x -= 5
                    if event.key == K_RIGHT:
                        x += 5
                    if event.key == K_UP:
                        y -= 5
                    if event.key == K_DOWN:
                        y += 5

MainWindow = PyManMain()
MainWindow.MainLoop()