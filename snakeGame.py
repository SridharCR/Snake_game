# Snake Game !

import pygame
import sys
import random
import time
#Check for errors
check_errors=pygame.init()
#(6 , 0)
if check_errors[1]>0:
    print("(!)Error occured!!!".format(check_errors[1]))
    sys.exit(-1)
else:
    print("No errors")
#Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game !")
#time.sleep(5)

#Color
red = pygame.Color(255,0,0) #game over
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(165,42,42) #food

#FPS Controller
fpsController = pygame.time.Clock()

#Important Variables
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]
