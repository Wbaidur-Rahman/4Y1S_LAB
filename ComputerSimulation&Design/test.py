import pygame
import math
import numpy as np

vf = 20
fighter_pos = (50,50)

pygame.init()
pygame.display.set_caption('Bomber Chasing')

width, height = 1000,800
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
pygame.display.flip()

font = pygame.font.Font('Laila-Bold.ttf',36)

text1 = font.render('Fighter', True, (255,0,0))
text2 = font.render('Bomber', True, (255,0,0))
text3 = font.render('Caughted', True, (255,0,0))
text4 = font.render('Escaped', True, (255,0,0))

#update the display
# pygame.display.flip()

def CalculateDistance(fighterPosition, bomberPosition):
    x = fighterPosition[0]-bomberPosition[0]
    y = fighterPosition[1]-bomberPosition[1]
    return math.sqrt(x**2+y**2)

previousFighterPosition = (200,200)
currentFighterPosition = (200,200)
previousBomberPosition = (500,500)
time = 0

#wait for user input or an event
running = True
while True:

    if time == 0:
        screen.blit(text1,(200,200))
        screen.blit(text2,(500,500))
    
    else:
        x = np.random.randint(100,700)
        y = np.random.randint(100,700)
        currentBomberPosition = (x,y)

        distance = CalculateDistance(currentFighterPosition, currentBomberPosition)

        if distance<30:
            screen.blit(text3, (100, 200))
            pygame.display.flip()
            break

        if time>15:
            screen.blit(text4, (100, 200))
            pygame.display.flip()
            break

        x = currentFighterPosition[0] + vf*(currentBomberPosition[0]-currentFighterPosition[0])/distance
        y = currentFighterPosition[1] + vf*(currentBomberPosition[1]-currentFighterPosition[1])/distance

        currentFighterPosition = (x,y)

        pygame.draw.line(screen, (0, 255, 0), previousFighterPosition, currentFighterPosition)
        pygame.draw.line(screen, (0, 0, 255), previousBomberPosition, currentBomberPosition)

        previousBomberPosition = currentBomberPosition
        previousFighterPosition = currentFighterPosition

    # screen.blit(text2, (300,300))
    pygame.time.delay(500)
    time+=1
    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

pygame.quit()
