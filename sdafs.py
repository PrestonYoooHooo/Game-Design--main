#Preston Yoo
#10-28-21
#window ssettings for a game

import pygame, os,random,time

os.system('cls')
pygame.init()
#list fot menu Messages
fl1count=0
fl2count=0
gameMessages= ["Play Game","Settings","Instructions","Scoreboard","Exit"]
settingMessages=["Screen Size","Background Colors", "Object Colors", "Sounds On\Off","Back"]#can use same logic for main menu
sizeMessages=["700*700", "800*800", "900*900", "1000*1000","Back"]
BacoMessages=["Red","Blue","White","Orange","Back"]
CoMessages=['Orange','Red','White','Blue','Back']
ScMessages=['Score 1','Score 2','Score 3', 'Score 4', 'Back']
InMessages= ['Get a friend', 'Gather 3 flags before them', 'Push them back with your laser', 'Enjoy your ruined friendship', 'Back']
PlMessages= ['Level 1', 'Level 2', 'Back']
EndMessages=['The top Score was', 'Play Level 1','Play Level 2', 'Back to Menu']
walkRight1 = [pygame.image.load('images/Pygame-Tutorials-master/Game/R1.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R2.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R3.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R4.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R5.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R6.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R7.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R8.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R9.png')]
walkLeft1 = [pygame.image.load('images/Pygame-Tutorials-master/Game/L1.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L2.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L3.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L4.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L5.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L6.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L7.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L8.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L9.png')]
walkRigh2 = [pygame.image.load('images/Pygame-Tutorials-master/Game/R1 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R2 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R3 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R4 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R5 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R6 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R7 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R8 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R9 - Copy.png')]
walkLeft2 = [pygame.image.load('images\Pygame-Tutorials-master\Game\L1 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L2 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L3 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L4 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L5 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L6 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L7 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L8 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L9 - Copy.png')]
StL1 = pygame.image.load('images\Pygame-Tutorials-master\Game\R1.png')
StR1 = pygame.image.load('images\Pygame-Tutorials-master\Game\L1.png')
StL2 = pygame.image.load('images\Pygame-Tutorials-master\Game\R1 - Copy.png')
StR2 = pygame.image.load('images\Pygame-Tutorials-master\Game\L1 - Copy.png')
sebg = pygame.image.load('images\images copy.jpg')
eibg = pygame.image.load('images\images copy 2.jpg')
nibg = pygame.image.load('images\images copy 3.jpg')
tebg = pygame.image.load('images\images.jpg')
sebg2 = pygame.image.load('images\lava-lake-active-valcano-rj-2560x1700.jpg')
eibg2 = pygame.image.load('images\lava-lake-active-valcano-rj-2560x1700 copy.jpg')
nibg2 = pygame.image.load('images\lava-lake-active-valcano-rj-2560x1700 copy 2.jpg')
tebg2 = pygame.image.load('images\lava-lake-active-valcano-rj-2560x1700 copy 3.jpg')
lamon = pygame.image.load('images\95-957201_lava-muk-pokemon-lava.jpg')
p1=pygame.image.load('images\pngtree-battle-player-1-vs-2-logo-versus-png-image_2899070.jpeg')
p2 = pygame.image.load('images\pngtree-battle-player-1-vs-2-logo-versus-png-image_2899070.jpeg')
fl = pygame.image.load('images\\Unknown.png') 
proj11 = pygame.image.load('images\\untitled folder\explosion01_128 copy.jpeg')
proj12 = pygame.image.load('images\\untitled folder\explosion01_128 copy 2.jpeg')
proj13 = pygame.image.load('images\\untitled folder\explosion01_128 copy 3.jpeg')
proj14 = pygame.image.load('images\\untitled folder\explosion01_128 copy 4.jpeg')
proj21 = pygame.image.load("images\\untitled folder\explosion01_128 copy 5.jpeg")
proj22 = pygame.image.load('images\\untitled folder\explosion01_128 copy 6.jpeg')
proj23 = pygame.image.load('images\\untitled folder\explosion01_128 copy 7.jpeg')
proj24 = pygame.image.load('images\\untitled folder\explosion01_128 copy 8.jpeg')
p1pjcon=4
p2pjcon=4
projcount11=30
projcount12=30
projcount13=30
projcount14=30
projcount21=30
projcount22=30
projcount23=30
projcount24=30
#global variables: they work anywhere in the program
colors = {'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,225), 'purple':(150,0,150), 'white':(255,255,255),'black': (0,0,0),'yellow': (255,211,67),'orange':(255, 165, 0), 'black': (0,0,0)}
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
RED=colors.get('red')
PURPLE=colors.get('purple')
BLUE=colors.get('blue')
WIDTH=800
HEIGHT=800
wbox=25
hbox=30
x=70
y=150
spped1=True
spped2=True
boldx1=200
boldy1=200
boldx2=WIDTH-200
boldy2=200
boldy3=HEIGHT-200
boldx3=200
boldx4=WIDTH-200
boldy4=HEIGHT-200
bolder1=pygame.Rect(boldx1,boldy1,75,75)
bolder2=pygame.Rect(boldx2,boldy2,75,75)
bolder3=pygame.Rect(boldx3,boldy3,75,75)
bolder4=pygame.Rect(boldx4,boldy4,75,75)# the cords for the wall that change depending on the height of the screen 
newgame1=False
newgame2=False
end=False
play=True
porjsped= 15
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Setting Window')
square=pygame.Rect(x,y,wbox,hbox)
#Declare FONTS
TITLE_FONT=pygame.font.SysFont('comicsans',80)
SubTitle=pygame.font.SysFont('comicsans', 40, italic=True)
MENU_FONT=pygame.font.SysFont('comicsans',40)
INSTUR_FONT=pygame.font.SysFont('comicsans',30)
text=TITLE_FONT.render('message',1,BLACK)
pj11=False
pj12=False
pj13=False
pj14=False
pj21=False
pj22=False
pj23=False
pj24=False
counter=0
walkCount1= 0
walkCount2= 0
lavacount=0
left1=False
right1=False
left2=False
right2=False
hitstun=False 
lastr1= False
lastl1= False 
lastr2= False
lastl2= False#used to determine the last dircetion each of them faced 
flgcount=0#counts number of flags on screen
FIGx1=50
FIGy1=HEIGHT-50
FIGx2=WIDTH-50
FIGy2= HEIGHT-50
walkCount1= 0
walkCount2= 0
boldx1=200
boldy1=200
boldx2=WIDTH-200
boldy2=200
escape1=True
score=0
boldy3=HEIGHT-200
boldx3=200
boldx4=WIDTH-200
boldy4=HEIGHT-200
fl1count=0
fl2count=0
left1=False
right1=False
left2=False
Right2=False
hitstun=False 
lastr1= True
lastl1= False 
lastr2= False
lastl2= True
lastw1=False
lastw2=False
lastd1=False
lastd2=False
FIGx1=50
FIGy1=HEIGHT-50
FIGx2=WIDTH-50
FIGy2= HEIGHT-50
end=False
lavacount=0
P1x=FIGx1
P2x=FIGx2
P1y=FIGy1-45
P2y=FIGy2-45
def create_NewWindow(winTitile):
    pygame.display.set_caption(winTitile)
    pygame.display.update()
def redrawGameWindowforp1():
    global walkCount1 
    if walkCount1 + 1 >= 27:
        walkCount1 = 0
    if left1==True and right1==False:  #for every time they take a step the walkcount is moved up by one and their image is changed constanly to make it look like they are moving in a certian direction
        win.blit(walkLeft1[walkCount1//3], (FIGx1,FIGy1))
        walkCount1 += 1                          
    elif right1==True and left1 ==False:
        win.blit(walkRight1[walkCount1//3], (FIGx1,FIGy1))
        walkCount1 += 1
    elif lastr1== True and lastl1 == False:#when they stop depending on their last motions it will have an idle motion in the last direction it was in
        win.blit(StR1, (FIGx1, FIGy1))
        walkCount1 = 0
    else:
        win.blit(StL1,FIGx1,FIGy1)#
        walkCoun1t=0
    if pj11==True:#just redraws the projectiles
        win.blit(proj11,pjxl11,pjy11)
    if pj12==True:
        win.blit(proj12,pjxl12,pjy12)
    if pj13==True:
        win.blit(proj13,pjxl13,pjy13)
    if pj14==True:
        win.blit(proj14,pjxl14,pjy14)
    if pj21==True:
        win.blit(proj21,pjxl21,pjy21)
    if pj22==True:
        win.blit(proj22,pjxl22,pjy22)
    if pj23==True:
        win.blit(proj23,pjxl23,pjy23)
    if pj24==True:
        win.blit(proj24,pjxl24,pjy24)
def redrawGameWindowforp2():
    global walkCount2
    if walkCount2 + 1 >= 27:
        walkCount2 = 0 
    if left2==True and right2==False:  
        win.blit(walkLeft2[walkCount2//3], (FIGx2,FIGy2))
        walkCount += 1                          
    elif right2==True and left2 ==False:
        win.blit(walkRight2[walkCount2//3], (FIGx2,FIGy2))
        walkCount2 += 1
    elif lastr2== True and lastl2 == False:
        win.blit(StR2, (FIGx2, FIGy2))
        walkCount2 = 0
    else:
        win.blit(StL2,FIGx2,FIGy2)
        walkCoun2t=0
    if pj11==True:
        win.blit(proj11,pjxl11,pjy11)
    if pj12==True:
        win.blit(proj12,pjxl12,pjy12)
    if pj13==True:
        win.blit(proj13,pjxl13,pjy13)
    if pj14==True:
        win.blit(proj14,pjxl14,pjy14)
    if pj21==True:
        win.blit(proj21,pjxl21,pjy21)
    if pj22==True:
        win.blit(proj22,pjxl22,pjy22)
    if pj23==True:
        win.blit(proj23,pjxl23,pjy23)
    if pj24==True:
        win.blit(proj24,pjxl24,pjy24)
pjxr11=FIGx1-40#all of these pj variables represent the projeciles and the diffrent positions I should spawn them dpending on the direction the player is facing when firing
pjy11=FIGy1
pjxl11=FIGx1+40
pjxr21=FIGx2-40
pjy21=FIGy2
pjxl21=FIGx2+40
pjxr12=FIGx1-40
pjy12=FIGy1
play=True
pjxl12=FIGx1+40
pjxr22=FIGx2-40
pjy22=FIGy2
pjxl22=FIGx2+40
pjxr13=FIGx1-40
pjy13=FIGy1
pjxl13=FIGx1+40
pjxr23=FIGx2-40
pjy23=FIGy2
pjxl23=FIGx2+40
pjxr14=FIGx1-40
pjy14=FIGy1
pjxl14=FIGx1+40
pjxr24=FIGx2-40
pjy24=FIGy2
pjxl24=FIGx2+40
pjyw11=FIGy1-40
pjyw12=FIGy1-40
pjyw13=FIGy1-40
pjyw14=FIGy1-40
pjyw21=FIGy2-40
pjyw22=FIGy2-40
pjyw23=FIGy2-40
pjyw24=FIGy2-40
pjyd11=FIGy1+40
pjyd11=FIGy1+40
pjyd12=FIGy1+40
pjyd13=FIGy1+40
pjyd14=FIGy1+40
pjyd21=FIGy2+40
pjyd22=FIGy2+40
pjyd23=FIGy2+40
pjyd24=FIGy2+40
flgcount=0
P1y=FIGy1-75#shows which player is which by stayign directicly above them
P2y=FIGy2-75
Flgx=random.randint(50,WIDTH-50)#
flgy=random.randint(50,HEIGHT-50)
create_NewWindow('Level 1')
win.blit(eibg,(0,0))
win.blit(StR1,(FIGx1,FIGy1))
win.blit(StL2,(FIGx2, FIGy2))
win.blit(p1,(P1x,P1y))
win.blit(p2,(P2x,P2y))
pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
pygame.draw.rect(win,ORANGE,bolder2)     
pygame.draw.rect(win,ORANGE,bolder3)  
pygame.draw.rect(win,ORANGE,bolder4)
while play:
    pygame.time.delay(100) #milliseconds 
    for anyThing in pygame.event.get(): #variable for anytrhing that happneds in py to listen to keyboard and mouse
        if anyThing.type ==pygame.QUIT: #says if Quit something happends
            play =False 
    win.blit(eibg,(0,0))
    win.blit(StR1,(FIGx1,FIGy1))
    win.blit(StL2,(FIGx2, FIGy2))
    win.blit(p1,(P1x,P1y))
    win.blit(p2,(P2x,P2y))
    pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
    pygame.draw.rect(win,ORANGE,bolder2)     
    pygame.draw.rect(win,ORANGE,bolder3)  
    pygame.draw.rect(win,ORANGE,bolder4)