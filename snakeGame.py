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

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

#Gameover function
def gameOver():
    myFont = pygame.font.SysFont('monaco',72)
    GOsurf = myFont.render("Game Over !!",True,red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360,15)
    playSurface.blit(GOsurf,GOrect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit() #pygame exit
    sys.exit() #console exit

#Main Logic of the game
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = "LEFT"
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = "UP"
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = "DOWN"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

# Validation of direction
    if changeto == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeto == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if changeto == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeto == "DOWN" and not direction == "UP":
        direction = "DOWN"

#Update snake position [x,y]
    if direction == "RIGHT":
        snakePos[0] += 10
    if direction == "LEFT":
        snakePos[0] -= 10
    if direction == "UP":
        snakePos[1] -= 10
    if direction == "DOWN":
        snakePos[1] += 10

#Snake body mechanisms
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
    else:
        snakeBody.pop()
#Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
#Drawing part
    playSurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(playSurface,brown,pygame.Rect(foodPos[0],foodPos[1],10,10))
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
    pygame.display.update()
    fpsController.tick(20)
