# import pygame
# import math

# # Constants
# MX = 100000
# # vf = 20.0
# # time = 10  # Adjust as needed
# # fx, fy = [0.0] * (time + 1), [0.0] * (time + 1)
# # bx, by = [0.0] * (time + 1), [0.0] * (time + 1)
# # dist = [0.0] * (time + 1)
# # sin_theta = [0.0] * (time + 1)
# # cos_theta = [0.0] * (time + 1)

# with open('input.txt','r') as file:
#     xb = file.read().split()

# for i in range(xb.size()):
#     xb[i] = 2
#     # int(x)/2

# print('Enter velocity')
# vf = int(input())
# print('Enter bomber co-ordinates')
# xb = input().split()
# yb = input().split()
# print(xb)

# # Initialize Pygame
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Pure Pursuit Problem")

# # Read input data here or replace with your data
# # ...

# # Main loop
# running = True
# clock = pygame.time.Clock()

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Calculate new positions and distances
#     for i in range(time):
#         dist[i] = math.sqrt((bx[i] - fx[i]) ** 2 + (by[i] - fy[i]) ** 2)
#         if dist[i] !=0 :
#             sin_theta[i] = (by[i] - fy[i]) / dist[i]
#             cos_theta[i] = (bx[i] - fx[i]) / dist[i]
#         fx[i + 1] = fx[i] + vf * cos_theta[i]
#         fy[i + 1] = fy[i] + vf * sin_theta[i]

#     # Check for collision or termination condition
#     if any(dist[i] <= vf for i in range(time)):
#         print(f"Time: {i}\nDistance: {dist[i]}")
#         running = False

#     # Drawing code
#     screen.fill((0, 0, 0))
#     # Draw your objects here using Pygame drawing functions
#     # ...


#     # Initialize Pygame
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("Drawing Objects in Pygame")

#     # Colors (RGB)
#     WHITE = (255, 255, 255)
#     RED = (255, 0, 0)
#     GREEN = (0, 255, 0)
#     BLUE = (0, 0, 255)

#     # Main loop
#     running = True
#     clock = pygame.time.Clock()

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # Clear the screen
#         screen.fill((0, 0, 0))

#         # Draw objects
#         # Draw a circle (x, y, radius)

#         pygame.draw.circle(screen, RED, (200, 200), 50)

#         # Draw a filled rectangle (x, y, width, height)
#         pygame.draw.rect(screen, GREEN, (300, 300, 100, 50))

#         # Draw a line (start_position, end_position, line_thickness)
#         pygame.draw.line(screen, BLUE, (400, 400), (600, 500), 5)

#         # Update the display
#         pygame.display.flip()

#         # Control frame rate
#         clock.tick(60)

# pygame.quit()


import pygame
import math
import numpy as np


VF = 20
fighter_pos = (50,50)

pygame.init()
pygame.display.set_caption("Pure Pursuit")

width , height = 1000 , 700
screen = pygame.display.set_mode((width , height))

f = pygame.font.get_default_font()
font = pygame.font.SysFont(f , 45)

boomberPos = font.render("B" , True , (255,0,0), (0,0,0))
fighterPos = font.render("F" , True , (0,255,0) , (0,0,0))
caught = font.render("Caught" , True , (0,255,0) , (0,0,0))
escaped = font.render("Escaped" , True , (255,0,0) , (0,0,0))

textRect1 = boomberPos.get_rect()
textRect2 = fighterPos.get_rect()
textRect3 = caught.get_rect()
textRect4 = escaped.get_rect()

def calcDistance(fighter_pos , boomber_pos):
    x = pow(boomber_pos[0] - fighter_pos[0] , 2)
    y = pow(boomber_pos[1] - fighter_pos[1] , 2)
    return math.sqrt(x+y)

t = 0
prev_fighter_pos = (0,0)
prev_boomber_pos = (0,0)
running = True

boomber_pos = (500,500)

while running:
    pygame.time.delay(500)

    timerPos = font.render("Time: "+str(t) , True , (255,255,255) , (0,0,0))
    textRect5 = timerPos.get_rect()
    textRect5.center = (90,height-50)
    screen.blit(timerPos , textRect5)

    x = np.random.randint( max(boomber_pos[0]-100,10) , min(boomber_pos[0]+100,width))
    y = np.random.randint( max(boomber_pos[1]-100,10) , min(boomber_pos[1]+100,width))
    boomber_pos = (x,y)

    if t == 0:
        textRect1.center = boomber_pos ; textRect2.center = fighter_pos
        screen.blit(boomberPos , textRect1) ; screen.blit(fighterPos , textRect2)

    else :
        pygame.draw.line(screen , (255,0,0) , prev_boomber_pos , boomber_pos , 2)
        pygame.draw.line(screen , (0,255,0) , prev_fighter_pos , fighter_pos , 2)
        pygame.draw.circle(screen , (255,255,255) , fighter_pos , 4)
        pygame.draw.circle(screen , (255,255,255) , boomber_pos , 4)


    dist = calcDistance(fighter_pos , boomber_pos)

    if t > 45:
        textRect4.center = (width / 2 , height / 2)
        screen.blit(escaped , textRect4)
        running = False

    if dist <= 100 :
        textRect3.center = (width / 2 , height / 2)
        screen.blit(caught , textRect3)
        running = False

    prev_boomber_pos = boomber_pos
    prev_fighter_pos = fighter_pos


    x = fighter_pos[0] + (VF * ((boomber_pos[0] - fighter_pos[0]) / dist))
    y = fighter_pos[1] + (VF * ((boomber_pos[1] - fighter_pos[1]) / dist))
    fighter_pos = (x,y)

    t += 1
    pygame.display.flip()

pygame.time.delay(3000)
pygame.quit()