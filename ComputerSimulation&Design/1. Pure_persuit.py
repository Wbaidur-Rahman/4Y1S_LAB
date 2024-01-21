import pygame as pg
import numpy as np

pg.init()
pg.display.set_caption('Pure Persuit Game')
screen = pg.display.set_mode((900,700))

fighter_pos = (50,50)
fighter_velocity = 30
bomber_pos = (400,400)

font = pg.font.Font(None, 45)
t1 = font.render('Fighter', True, (255,255,255))
t2 = font.render('Bomber', True, (255,255,255))
t3 = font.render('Caught', True, (255,255,255))
t4 = font.render('Escaped', True, (255,255,255))

x1 = t1.get_rect().center = (30,30)
x2 = t2.get_rect().center = (390,390)
x3 = t3.get_rect().center = (730,30)
x4 = t4.get_rect().center = (730,30)

def distance(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

screen.blit(t1, x1)
screen.blit(t2, x2)
running = True; t=0
while running:
    t5 = font.render('Time: '+str(t) , True, (255,255,255), (0,0,0))
    x5 = t5.get_rect().center = (100,600)
    screen.blit(t5,x5)
    
    prev_fp = fighter_pos
    prev_bp = bomber_pos

    dist = distance(fighter_pos, bomber_pos)
    if dist<=10:
        running &= 0
        screen.blit(t3, x3)
    elif dist>600 or t>35:
        running &= 0
        screen.blit(t4, x4)

    else:
        bomber_pos = (np.random.randint(max(1,bomber_pos[0]-100), min(900,bomber_pos[0]+100)),  np.random.randint(max(1,bomber_pos[1]-100), min(700,bomber_pos[1]+100)))
        fighter_pos = (fighter_pos[0]+fighter_velocity*(bomber_pos[0]-fighter_pos[0])/dist, fighter_pos[1]+fighter_velocity*(bomber_pos[1]-fighter_pos[1])/dist)
        pg.draw.line(screen, (0,255,255), prev_fp, fighter_pos, 2)
        pg.draw.line(screen, (255,255,0), prev_bp, bomber_pos, 2)

    pg.draw.circle(screen, (0,255,0), fighter_pos, 4)
    pg.draw.circle(screen, (255,0,0), bomber_pos, 4)
    t+=1
    pg.time.delay(500)
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN:
            running = False

running =True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN:
            running = False
pg.quit()