import pygame
from sys import exit
import numpy as np
import time

def nsum(a):
    b = np.roll(a,-1,0) + np.roll(a,-1,1) + np.roll(np.roll(a,-1,0),-1,1) + np.roll(np.roll(a,1,0),-1,1) + np.roll(np.roll(a,-1,0),1,1) + np.roll(np.roll(a,1,0),1,1) + np.roll(a,1,1) + np.roll(a,1,0)
    return b

def dtime():
    global t0
    print(time.time() - t0)
    t0 = time.time()

pygame.init()

width,height = 512,512
nx,ny = 128,128 
dx,dy = int(width/nx),int(width/ny)
screen = pygame.display.set_mode((width,height))

bg = 25,25,25
screen.fill(bg)


gameState = np.random.randint(0,2,(nx,ny),dtype='B')
#gameState = np.zeros((nx,ny),dtype='B')

poly = {}
for y in range(ny):
    for x in range(nx):
        poly[(x,y)] = [(x*dx,y*dy),((x+1)*dx,y*dy),((x+1)*dx,(y+1)*dy),(x*dx,(y+1)*dy)]

color = {1:(255,255,255),0:(128,128,128)}
pauseExect = False
n = 0
while True:
    n += 1
    print("Generación {}".format(n))

    t0 = time.time()

    pass
    screen.fill(bg)

    dtime()

    #time.sleep(0.01)

    if not pauseExect:
        n_neigh = nsum(gameState)
        newGameState = np.zeros((nx,ny),dtype='B') + (n_neigh*(gameState==1)==3)*1 + (n_neigh*(gameState==1)==2)*1 + (n_neigh*(gameState==0)==3)*1
    print(n_neigh.dtype,newGameState.dtype)
    
    dtime()

    for y in range(ny):
        for x in range(nx):
            #pygame.draw.polygon(screen,color[newGameState[x,y]],poly[(x,y)],0)
            #pygame.draw.rect(screen,color[newGameState[x,y]],pygame.Rect((x*dx,y*dy),(dx,dy)),0)
            pygame.draw.rect(screen,(255,255,255)*newGameState[x,y] + (128,128,128)*(1 - newGameState[x,y]),pygame.Rect((x*dx,y*dy),(dx,dy)),0)

            
    pygame.display.flip()

    dtime()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        click = pygame.mouse.get_pressed()
        if sum(click)>0:
            px,py = pygame.mouse.get_pos()
            cx,cy = int(np.floor(px/dx)),int(np.floor(py/dy))
            newGameState[cx,cy] = not click[2]
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    gameState = np.copy(newGameState)

    dtime()

