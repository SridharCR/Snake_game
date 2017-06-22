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
time.sleep(5)
