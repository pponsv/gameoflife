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

width,height = 1000,1000
nx,ny = 1000,1000
dx,dy = int(width/nx),int(width/ny)
screen = pygame.display.set_mode((width,height))

bg = 25,25,25
screen.fill(bg)

ones = np.ones((nx,ny),dtype='B')
gameState = np.random.randint(0,2,(nx,ny),dtype='B')
def mksurf(gs):
    Z = 255*np.kron(gs,np.ones((dx,dy),dtype='B'))
    return pygame.surfarray.make_surface(Z)

pauseExect = False
n = 0
T = time.time()
while n<1000:
    t0 = time.time()

    n += 1
    print("Generación {}".format(n))

    pass
    
    screen.blit(mksurf(gameState),(0,0))

    dtime()

    if not pauseExect:
        n_neigh = nsum(gameState)
        newGameState = ((n_neigh*(gameState==1)==3) + (n_neigh*(gameState==1)==2) + (n_neigh*(gameState==0)==3))*ones
    
    dtime()

    pygame.display.flip()


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
            print(time.time()-T,n)
            exit()

    dtime()

    gameState = np.copy(newGameState)

    dtime()
print(time.time()-T)
