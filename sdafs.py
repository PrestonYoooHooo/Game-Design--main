import pygame, os,random,time
WIDTH=800
HEIGHT=800
colors = {'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,225), 'purple':(150,0,150), 'white':(255,255,255),'black': (0,0,0),'yellow': (255,211,67),'orange':(255, 165, 0), 'black': (0,0,0)}
WHITE=colors.get('white')
win=pygame.display.set_mode((WIDTH,HEIGHT))
def create_NewWindow(winTitile):
    pygame.display.set_caption(winTitile)
    win.fill(WHITE)
    pygame.display.update()
create_NewWindow('Level 1')
bg=pygame.image.load('images/images copy.jpg')
win.blit(bg,(0,0))