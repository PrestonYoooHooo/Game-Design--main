#Preston Yoo
#10-28-21
#window ssettings for a game

import pygame, os,random,time

from pygame.display import flip

os.system('cls')
pygame.init()
#list fot menu Messages
fl1count=0
fl2count=0
hecount=2
gameMessages= ["Play Game","Settings","Instructions","Scoreboard","Exit"]
settingMessages=["Screen Size","Background Colors", "Object Colors", "Sounds On\Off","Back"]#can use same logic for main menu
sizeMessages=["700*700", "800*800", "900*900", "1000*1000","Back"]
BacoMessages=["Red","Blue","White","Orange","Back"]
CoMessages=['Orange','Red','White','Blue','Back']
ScMessages=['The Top Score is:','Back']
InMessages= ['Get a friend', 'collect 5 coins first', 'more coins=speed', 'monsters=-coins', 'Back']
PlMessages= ['Level 1', 'Level 2', 'Back']
EndMessages=['Play Level 1','Play Level 2', 'Back to Menu']
walkRight1 = [pygame.image.load('images\Pygame-Tutorials-master\Game\R1.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R2.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R3.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R4.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R5.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R6.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R7.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R8.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R9.png')]
walkLeft1 = [pygame.image.load('images\Pygame-Tutorials-master\Game\L1.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L2.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L3.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L4.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L5.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L6.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L7.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L8.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L9.png')]
walkRight2 = [pygame.image.load('images\Pygame-Tutorials-master\Game\R1 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R2 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R3 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R4 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R5 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R6 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R7 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R8 - Copy.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R9 - Copy.png')]
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
p2 = pygame.image.load('images\pngtree-battle-player-1-vs-2-logo-versus-png-image_2899070 copy.jpeg')
fl = pygame.image.load('images\\Unknown.png') 
gob = pygame.image.load('images\Pygame-Tutorials-master\Game\L1E.png')
# proj11 = pygame.image.load('images\\untitled folder\explosion01_128 copy.jpeg')
# proj12 = pygame.image.load('images\\untitled folder\explosion01_128 copy 2.jpeg')
# # proj13 = pygame.image.load('images\\untitled folder\explosion01_128 copy 3.jpeg')
# # proj14 = pygame.image.load('images\\untitled folder\explosion01_128 copy 4.jpeg')
# proj21 = pygame.image.load("images\\untitled folder\explosion01_128 copy 5.jpeg")
# proj22 = pygame.image.load('images\\untitled folder\explosion01_128 copy 6.jpeg')
# # proj23 = pygame.image.load('images\\untitled folder\explosion01_128 copy 7.jpeg')
# # proj24 = pygame.image.load('images\\untitled folder\explosion01_128 copy 8.jpeg')
coin= pygame.image.load('images\OIP.jpg')
p1pjcon=4
p2pjcon=4
projcount11=30
projcount12=30
# projcount13=30
# projcount14=30
projcount21=30
gm2=False
stgm=True
projcount22=30
# projcount23=30
# projcount24=30
lavacount=0
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
cointcount=1
gbx= random.randint(50,WIDTH-50)
gby= random.randint(50,HEIGHT-50)
cx=random.randint(50,WIDTH-50)
cy=100
wbox=25
hbox=30
coincount=1
x=70
y=150
spped1=True
spped2=True
boldx1=200
boldy1=200
gobcount=0
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
# pj13=False
# pj14=False
pj21=False
pj22=False
# pj23=False
# pj24=False
counter=0
walkCount1= 0
walkCount2= 0
lavacount=0
pl1hc=0
gem=False
pl2hc=0
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
FIGx1=150
FIGy1=HEIGHT-150
FIGx2=WIDTH-150
FIGy2=HEIGHT-150#they start at oppisted sides of the screen 
def updateFile():#Thanks to Tech With Tim for this function
    f = open('scores.txt','r') # opens the file in read mode
    file = f.readlines() # reads all the lines in as a list
    last = int(file[0]) # gets the first line of the file

    if last < int(score): # sees if the current score is greater than the previous best
        f.close() # closes/saves the file
        file = open('scores.txt', 'w') # reopens it in write mode
        file.write(str(score)) # writes the best score
        file.close() # closes/saves the file

        return score
               
    return last
def lavspawn():
    global lavacount
    global pl1hc
    global pl2hc
    global lvx
    global lvy
    if lavacount==0:
        lvx= random.randint(50,WIDTH-50)#randomizes the lava coordds when there isn't lava already on the screen
        lvy= random.randint(50,HEIGHT-50)
        lavacount+=1
        win.blit(lamon,(lvx,lvy))
    if lavacount==1:#shows the lava when the coords are found
        win.blit(lamon,(lvx,lvy))
    if lvx==boldx1+85 or lvx==boldx1-85 or lvx==boldx2+85 or lvx==boldx2-85 or lvx==boldx3+85 or lvx==boldx3-85 or lvx==boldx4+85 or lvx==boldx4-85 or lvy==boldy1+85 or lvy==boldy1-85 or lvy==boldy2+85 or lvy==boldy2-85 or lvy==boldy3+85 or lvy== boldy3-85 or lvy== boldy4+85 or lvy== boldy4-85:
        lvx= random.randint(50,WIDTH-50)# if the lava lands on a wall postition it will instantly randomize the coordinates so the lava isn't stuck in one place
        lvy= random.randint(50,HEIGHT-50)  
    if lvx>boldx1-30 and lvx<boldx1+30 and lvy>boldx1-30 and lvy<boldx1+30:
        lavacount+=1
    if lvx>boldx2-30 and lvx<boldx2+30 and lvy>boldy2-30 and lvy<boldy2+30:
        lavacount+=1
    if lvx>boldx3-30 and lvx<boldx3+30 and lvy>boldx3-30 and lvy<boldx3+30:
        lavacount+=1
    if lvx>boldx4-30 and lvx<boldx4+30 and lvy>boldy4-30 and lvy<boldy4+30:
        lavacount+=1
    if FIGx1>lvx-30 and FIGx1<lvx+30 and FIGy1>lvx-30 and FIGy1<lvx+30: #as with other extra numbers these gave some linency so you don't have to be right on top of it  to trigger it
        lavacount-=1
        pl1hc-=2#lava takes away more coins than the goblin will
    if FIGy1>lvy-30 and FIGy1<lvy+30 and FIGx1>lvy-30 and FIGx1<lvy+30:
        lavacount-=1
        pl1hc-=2
    if FIGx2>lvx-30 and FIGx2<lvx+30 and FIGy2>lvx-30 and FIGy2<lvx+30: #as with other extra numbers these gave some linency so you don't have to be right on top of it  
        lavacount-=1
        pl2hc-=2
    if FIGy2>lvy-30 and FIGx2<lvy+30 and FIGx2>lvy-30 and FIGx2<lvy+30:
        lavacount-=1
        pl2hc-=2
    if lvx<50:#border controls for the goblin/lava that will make sure they stay in bounds
        lvx+=50
    if lvx>WIDTH-50:
        lvx-=50
    if lvy==50:
        lvy+=50
    if lvy==HEIGHT-50:
        lvy-=50
    pygame.display.flip()
def gobspawn():
    global gobcount
    global gbx
    global gby
    global pl1hc
    global pl2hc
    global HEIGHT
    global WIDTH
    if gobcount==0:
        gbx= random.randint(50,WIDTH-50)#randomizes thgbye goblin coordds when there isn't a goblin already on the screen
        gby= random.randint(50,HEIGHT-50)
        gobcount+=1
        win.blit(gob,(gbx,gby))
    if gobcount==1:#shows the goblin when the coords are found
        win.blit(gob,(gbx,gby)) 
    if gbx>boldx1-30 and gbx<boldx1+30 and gby>boldx1-30 and gby<boldx1+30:
        gobcount-=1
    if gbx>boldx2-30 and gbx<boldx2+30 and gby>boldy2-30 and gby<boldy2+30:
        gobcount-=1
    if gbx>boldx3-30 and gbx<boldx3+30 and gby>boldx3-30 and gby<boldx3+30:
        gobcount-=1
    if gbx>boldx4-30 and gbx<boldx4+30 and gby>boldy4-30 and gby<boldy4+30:
        gobcount-=1
    if FIGx1>gbx-30 and FIGx1<gbx+30 and FIGy1>gbx-30 and FIGy1<gbx+30: #as with other extra numbers these gave some linency so you don't have to be right on top of it  
        gobcount-=1
        pl1hc-=1#goblin takes away less coins
    if FIGy1>gby-30 and FIGx1<gby+30 and FIGy1>gby-30 and FIGy1<gby+30:
        gobcount-=1
        pl1hc-=1
    if FIGx2>gbx-30 and FIGx2<gbx+30 and FIGy2>gbx-30 and FIGy2<gbx+30: #as with other extra numbers these gave some linency so you don't have to be right on top of it  
        gobcount-=1
        pl2hc-=1
    if FIGy2>gby-30 and FIGy2<gby+30 and FIGx2>gbx-30 and FIGx2<gbx+30:
        gobcount-=1
        pl2hc-=1
    if gbx<50:#border controls for the goblin/lava that will make sure they stay in bounds
        gbx+=50
    if gbx>WIDTH-50:
        gbx-=50
    if gby==50:
        gby+=50
    if gby==HEIGHT-50:
        gby-=50
    pygame.display.flip()
def coinspawn():
    global coincount#global commands allow us to use variables difined elsewhere int he program
    global cy
    global cx
    global HEIGHT
    global FIGx1
    global FIGy1
    global FIGx2
    global FIGy2
    global pl1hc
    global pl2hc
    if coincount==1:
        cy=0
        cx=random.randint(50,WIDTH-50)#coin's x postion is random but they start at the top of the screen
        win.blit(coin,(cx,cy))
        coincount-=1
    if coincount==0:#causes it to fall
        cy+=10
        win.blit(coin,(cx,cy))
    if cy==HEIGHT-50:#if it hits the bottrom the coin respawns from the top
        coincount+=1
    if FIGx1>cx-30 and FIGx1<cx+30 and FIGy1>cy-30 and FIGy1<cy+30:#allows players to grab the coins and add to their counter
        coincount+=1
        pl1hc+=1
    if FIGx2>cx-30 and FIGx2<cx+30 and FIGy2>cy-30 and FIGy2<cy+30:
        coincount+=1
        pl2hc+=1
    pygame.display.flip()
def redrawGameWindowforp1():
    global walkCount1 
    global walkCount2
    global pjxl11
    global pjy11
    global pjxl12
    global pjy12
    global pjxl21
    global pjy21
    global pjxl22
    global pjy22
    global P1x
    global P1y
    global P2x
    global P2y
    global hecount
    global speedx
    global speedy
    global gem2
    if gem2==True:#if I am starting a level 2 game this will load a diffrent background while also loading it sepedning on the screen size
        if hecount==1:
            win.blit(sebg2,(0,0))
        if hecount==2:
            win.blit(eibg2,(0,0))
        if hecount==3:
            win.blit(nibg2,(0,0))
        if hecount==4:
            win.blit(tebg2,(0,0))
    else:
        if hecount==1:
            win.blit(sebg,(0,0))
        if hecount==2:
            win.blit(eibg,(0,0))
        if hecount==3:
            win.blit(nibg,(0,0))
        if hecount==4:
            win.blit(tebg,(0,0))
    pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
    pygame.draw.rect(win,ORANGE,bolder2)     
    pygame.draw.rect(win,ORANGE,bolder3)  
    pygame.draw.rect(win,ORANGE,bolder4)
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
        win.blit(StL1,(FIGx1,FIGy1))#
        walkCount1=0
    # if pj11==True:#just redraws the projectiles
    #     win.blit(proj11,(pjxl11,pjy11))
    # if pj12==True:
    #     win.blit(proj12,(pjxl12,pjy12))
    # # if pj13==True:
    # #     win.blit(proj13,(pjxl13,pjy13))
    # # if pj14==True:
    # #     win.blit(proj14,(pjxl14,pjy14))
    # if pj21==True:
    #     win.blit(proj21,(pjxl21,pjy21))
    # if pj22==True:
    #     win.blit(proj22,(pjxl22,pjy22))
    # if pj23==True:
    #     win.blit(proj23,(pjxl23,pjy23))
    # if pj24==True:
    #     win.blit(proj24,(pjxl24,pjy24))
    global walkCount2
    if walkCount2 + 1 >= 27:
        walkCount2 = 0 
    if left2==True and right2==False:  
        win.blit(walkLeft2[walkCount2//3], (FIGx2,FIGy2))
        walkCount2 += 1                          
    elif right2==True and left2 ==False:
        win.blit(walkRight2[walkCount2//3], (FIGx2,FIGy2))
        walkCount2 += 1
    elif lastr2== True and lastl2 == False:
        win.blit(StR2, (FIGx2, FIGy2))
        walkCount2 = 0
    elif lastl2==True and lastr2 == False:
        win.blit(StL2,(FIGx2,FIGy2))
        walkCount2=0
    # if pj11==True:
    #     win.blit(proj11,(pjxl11,pjy11))
    # if pj12==True:
    #     win.blit(proj12,(pjxl12,pjy12))
    # # if pj13==True:
    # #     win.blit(proj13,(pjxl13,pjy13))
    # # if pj14==True:
    # #     win.blit(proj14,(pjxl14,pjy14))
    # if pj21==True:
    #     win.blit(proj21,(pjxl21,pjy21))
    # if pj22==True:
    #     win.blit(proj22,(pjxl22,pjy22))
    # if pj23==True:
    #     win.blit(proj23,(pjxl23,pjy23))
    # if pj24==True:
    #     win.blit(proj24,(pjxl24,pjy24))
    pygame.display.update()
    speedx=10+(pl2hc*10)#speed based on the other players coin count so you could get an advantage or disadavnatage depdning on 
    speedy=10+(pl1hc*10)
def create_NewWindow(winTitile):
    pygame.display.set_caption(winTitile)
    win.fill(WHITE)
    pygame.display.update()
def create_NewgWindow(winTitile):
    FIGx1=50
    FIGy1=HEIGHT-50
    FIGx2=WIDTH-50
    FIGy2=HEIGHT-50#they start at oppisted sides of the screen 
    pygame.display.set_caption(winTitile)
    win.blit(eibg,(0,0))
    # win.blit(StR1,(FIGx1,FIGy1))
    #win.blit(StL2,(FIGx2, FIGy2))
    #win.blit(p1,(P1x,P1y))
    # win.blit(p2,(P2x,P2y))
    # pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
    # pygame.draw.rect(win,ORANGE,bolder2)     
    # pygame.draw.rect(win,ORANGE,bolder3)  
    # pygame.draw.rect(win,ORANGE,bolder4)
    pygame.display.update
def display_Title(message,y):#that comes with def
    win.fill(WHITE)
    pygame.time.delay(100)
    text=TITLE_FONT.render(message,1,BLACK)#message now variable
    xm=WIDTH/2-text.get_width()/2
    ym=40
    win.blit(text,(xm,ym))
    pygame.display.update()
    pygame.time.delay(100)

def Menu_function(Messages,y):
    pygame.time.delay(100)
    square.y=y
    xy=15
    ym=y-xy
    #this works because the other xm is in another function sso it is sepaerate aka a local variable
    xm=x+wbox+10

    for i in range (0,len(Messages)):
        word=Messages[i]
        pygame.draw.rect(win, ORANGE,square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm,ym))
        pygame.display.update()
        pygame.time.delay(100)
        ym+=100
        square.y=ym+15
    
display_Title("TestyGame",y)
Menu_function(gameMessages,150)
run=True
play=True
while run:
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            run=False
        if eve.type ==pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses [0]:
                mouse_pos =pygame.mouse.get_pos()
                print (mouse_pos)
                xp=mouse_pos[0]
                yp=mouse_pos[1]
                print (x,y)
                #if py.Rect.collidepoint(square,(mouse_pos)):
                if xp >x and xp<x+wbox and yp>y and yp<245 and counter is 0:
                    xp=0#this resets the mouse postion so double pressing dossen't occur
                    yp=0
                    win.fill(WHITE)#it says white but it will change to any background color you chose
                    create_NewWindow("Play Game")
                    display_Title("Play Game",40)
                    Menu_function(PlMessages,150)
                    counter+=7
                    pygame.time.delay(100)
                if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 0:# the counter system allows us to see where we are and along with mouse postion allows for smooth and clean transitions between screens
                    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
                    xp=0
                    yp=0
                    win.fill(WHITE)
                    create_NewWindow("Settings")
                    display_Title("Settings",40)
                    Menu_function(settingMessages,150)
                    counter+=1
                if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 0:
                    xp=0
                    yp=0
                    win.fill(WHITE)
                    create_NewWindow("Instructions")
                    display_Title("Instructions",40)
                    Menu_function(InMessages,150)
                    pygame.time.delay(100)
                    counter+=5
            #myFile=open ('insturctions.txt','r')
            #yi=150
            #for line in myFile.readlines():
                #text=INSTRUCTIONS_FONT.render(line, 1, BLACK)
                #win.blit(text,(40,yi))
                #pygame.display.update
                #pygame.time.delay(100)
               # yi+=50
            #myFile=close

                if xp>x and xp<x+wbox and yp>y and yp<545 and yp>445 and counter is 0:
                    xp=0
                    yp=0                  
                    win.fill(WHITE)
                    xm=WIDTH/2-text.get_width()/2+190
                    ym=150-10
                    create_NewWindow("Score Board")
                    display_Title("Top score",40)
                    Menu_function(ScMessages, 150)
                    fl = open('scores.txt','r')
                    fg = fl.readlines()
                    fls = str(fg[0])
                    flst = MENU_FONT.render(fls,1,BLACK)
                    win.blit(flst, (xm,ym))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    counter+=6
                if xp>x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 0:
                    run=False
                if xp>x and xp<x+wbox and yp>y and yp<245 and counter is 1:
                    xp=0
                    yp=0                  
                    win.fill(WHITE)
                    create_NewWindow("Screen Size")
                    display_Title("Screen Size",40)
                    Menu_function(sizeMessages,150)
                    counter+=1
                if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 1:
                    xp=0
                    yp=0                 
                    win.fill(WHITE)
                    create_NewWindow("Background Color")
                    display_Title("Background Color",40)
                    Menu_function(BacoMessages,150)
                    counter+=2
                    pygame.time.delay(100)
                if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 1:
                    xp=0
                    yp=0                 
                    win.fill(WHITE)
                    create_NewWindow("Object Color")
                    display_Title("Object Color",40)
                    Menu_function(CoMessages,150)
                    counter+=3
                    pygame.time.delay(100)
                if xp>x and xp<x+wbox and yp>y and yp<545 and yp>345 and counter is 1:
                    xp=0
                    yp=0                 
                if xp>x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 1:
                    xp=0
                    yp=0
                    win.fill(WHITE)
                    display_Title("TestyGame",y)
                    Menu_function(gameMessages,150)
                    counter-=1
                if xp >x and xp<x+wbox and yp>y and yp<245 and counter is 2:
                    xp=0
                    yp=0
                    hecount=1
                    HEIGHT=700#sets height
                    WIDTH=700
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    create_NewWindow("Screen Size")
                    display_Title("Screen Size",40)
                    Menu_function(sizeMessages,150)
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 2:
                    xp=0
                    yp=0
                    hecount=2
                    HEIGHT=800
                    WIDTH=800
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    create_NewWindow("Screen Size")
                    display_Title("Screen Size",40)
                    Menu_function(sizeMessages,150)
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 2:
                    xp=0
                    yp=0    
                    hecount=3              
                    HEIGHT=900
                    WIDTH=900
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    create_NewWindow("Screen Size")
                    display_Title("Screen Size",40)
                    Menu_function(sizeMessages,150)
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<545 and yp>445 and counter is 2:
                    xp=0 
                    yp=0
                    hecount=4
                    HEIGHT=1000
                    WIDTH=1000
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    create_NewWindow("Screen Size")
                    display_Title("Screen Size",40)
                    Menu_function(sizeMessages,150)
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 2:
                    xp=0
                    yp=0                    
                    win.fill(WHITE)
                    display_Title("Settings",y)
                    Menu_function(settingMessages,150)
                    counter-=1
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<245 and counter is 3:
                    xp=0
                    yp=0  
                    WHITE=colors.get('red')                
                    win.fill(WHITE)
                    create_NewWindow("Background Color")
                    display_Title("Background Color",40)
                    Menu_function(BacoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 3:
                    xp=0
                    yp=0  
                    WHITE=colors.get('blue')             
                    win.fill(WHITE)
                    create_NewWindow("Background Color")
                    display_Title("Background Color",40)
                    Menu_function(BacoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 3:
                    xp=0
                    yp=0  
                    WHITE=colors.get('white')            
                    win.fill(WHITE)
                    create_NewWindow("Background Color")
                    display_Title("Background Color",40)
                    Menu_function(BacoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<545 and yp>445 and counter is 3:    
                    WHITE=colors.get('orange')             
                    win.fill(ORANGE)
                    xp=0
                    yp=0
                    create_NewWindow("Background Color")
                    display_Title("Background Color",40)
                    Menu_function(BacoMessages,150)
                    pygame.display.update()
                    
                if xp >x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 3:
                    xp=0
                    yp=0                   
                    win.fill(WHITE)
                    display_Title("Settings",y)
                    Menu_function(settingMessages,150)
                    counter-=2
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<245 and counter is 4:
                    xp=0
                    yp=0  
                    ORANGE=colors.get('orange')                
                    win.fill(WHITE)
                    create_NewWindow("Object Color")
                    display_Title("ObjectColor",40)
                    Menu_function(CoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 4:
                    xp=0
                    yp=0  
                    ORANGE=colors.get('red')             
                    win.fill(ORANGE)
                    create_NewWindow("Object Color")
                    display_Title("Object Color",40)
                    Menu_function(CoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 4:
                    xp=0
                    yp=0  
                    ORANGE=colors.get('white')            
                    win.fill(ORANGE)
                    create_NewWindow("Object Color")
                    display_Title("Object Color",40)
                    Menu_function(CoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<545 and yp>445 and counter is 4:    
                    ORANGE=colors.get('blue')             
                    win.fill(ORANGE)
                    xp=0
                    yp=0
                    create_NewWindow("Object Color")
                    display_Title("Object Color",40)
                    Menu_function(CoMessages,150)
                    pygame.display.update()
                    
                if xp >x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 4:
                    xp=0
                    yp=0                   
                    win.fill(WHITE)
                    display_Title("Settings",y)
                    Menu_function(settingMessages,150)
                    counter-=3
                    pygame.time.delay(100)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 5:
                    xp=0
                    yp=0 
                    win.fill(WHITE)
                    display_Title("Testy Game",y)
                    Menu_function(gameMessages,150)
                    counter-=5
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 6:
                    xp=0
                    yp=0 
                    win.fill(WHITE)
                    display_Title("Testy Game",y)
                    Menu_function(gameMessages,150)
                    counter-=6
                    pygame.time.delay(100)
                if xp>x and xp<x+wbox and yp>y and yp<245 and counter is 7 or newgame1==True and counter is 7:
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
                    newgame2=False
                    gm2=False
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
                    FIGx1=150
                    FIGy1=HEIGHT-150
                    FIGx2=WIDTH-150
                    FIGy2= HEIGHT-150
                    end=False
                    lavacount=0
                    pl1hc=0
                    pl2hc=0
                    P1x=FIGx1
                    P2x=FIGx2
                    P1y=FIGy1-45
                    P2y=FIGy2-45
                    pjxr11=FIGx1+40#all of these pj variables represent the projeciles and the diffrent positions I should spawn them dpending on the direction the player is facing when firing
                    pjy11=FIGy1
                    pjxl11=FIGx1-40
                    pjxr21=FIGx2+40
                    pjy21=FIGy2
                    pjxl21=FIGx2-40
                    pjxr12=FIGx1+40
                    pjy12=FIGy1
                    gem2=False
                    play=True
                    pjxl12=FIGx1-40
                    pjxr22=FIGx2+40
                    pjy22=FIGy2
                    pjxl22=FIGx2-40
                    pjxr13=FIGx1+40
                    pjy13=FIGy1
                    gobcount=0
                    pjxl13=FIGx1-40
                    pjxr23=FIGx2+40
                    pjy23=FIGy2
                    pjxl23=FIGx2-40
                    pjxr14=FIGx1+40
                    pjy14=FIGy1
                    pjxl14=FIGx1-40
                    pjxr24=FIGx2+40
                    pjy24=FIGy2
                    pjxl24=FIGx2-40
                    flgcount=0
                    pj11=False
                    pj12=False
                    pj13=False
                    pj14=False
                    pj21=False
                    pj22=False
                    pj23=False
                    pj24=False
                    stgm=False
                    speedx=10
                    speedy=10
                    P1y=FIGy1-75#shows which player is which by stayign directicly above them
                    P2y=FIGy2-75
                    Flgx=random.randint(50,WIDTH-50)#
                    flgy=random.randint(50,HEIGHT-50)
                    create_NewgWindow('Level 1')
                    # if HEIGHT==700:
                    #     win.blit(sebg,(0,0))
                    # if HEIGHT==900:
                    #     win.blit(nibg,(0,0))
                    # if HEIGHT==1000:#bases type of background needed on height
                    #     win.blit(tebg,(0,0))
                    # win.blit(StR1,(FIGx1,FIGy1))
                    # win.blit(StL2,(FIGx2, FIGy2))
                    # win.blit(p1,(P1x,P1y))
                    # win.blit(p2,(P2x,P2y))
                    # pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
                    # pygame.draw.rect(win,ORANGE,bolder2)     
                    # pygame.draw.rect(win,ORANGE,bolder3)  
                    # pygame.draw.rect(win,ORANGE,bolder4)
                    # my_timer.reset()
                    # my_timer = Stopwatch()
                    while play:
                        pygame.time.delay(100) #milliseconds 
                        for anyThing in pygame.event.get(): #variable for anytrhing that happneds in py to listen to keyboard and mouse
                            if anyThing.type ==pygame.QUIT: #says if Quit something happends
                                run =False
                        keyPressed= pygame.key.get_pressed()#records keyboard movement
                        P1y=FIGy1-75
                        P2y=FIGy2-75
                        if spped1:  #this if statment allows me to disable a single players movement if they are stunned
                            if keyPressed[pygame.K_d]: 
                                FIGx1 +=speedx #negative or postive depsending on direction
                                right1=True#for direction
                                left1=False
                                lastr1=True#for the last direction if an idle pose is needed
                                lastl1=False
                                lastd1=False
                                lastw1=False
                            if keyPressed[pygame.K_a]:  
                                FIGx1 -=speedx 
                                right1=False
                                left1=True
                                lastr1=False
                                lastl1=True
                                lastd1=False
                                lastw1=False
                            if keyPressed[pygame.K_w]:  #wasn't able to get up and down sprite so reused the other walking sprites but you do still travel in that direction
                                FIGy1-=speedx
                                lastr1=False
                                lastl1=False
                                lastd1=False
                                lastw1=True      
                            if keyPressed [pygame.K_s]:
                                FIGy1 +=speedx
                                lastr1=False
                                lastl1=False
                                lastw1=False
                                lastd1=True
                            if FIGx1==10:#border controls for player 1 that buffs them back if they walk into it
                                FIGx1+=30
                            if FIGx1==WIDTH-30:
                                FIGx1-=30
                            if FIGy1==10:
                                FIGy1+=30
                            if FIGy1==HEIGHT-30:
                                FIGy1-=30
                            # if keyPressed[pygame.K_f]:#fires projectile depending on directions and limits it to only 4 projectiles per player allowed to be fired on the screen
                            #     if lastr1==True and p1pjcon>0:#you can fire left and right (not up and down becuase i could find good back sprites for facing does directions so while you can move in them you can shot in them)
                            #         if p1pjcon==4:
                            #             win.blit(proj11,(pjxr11,FIGy1))
                            #             p1pjcon-=1
                            #             pj11=True
                            #         if p1pjcon==3:
                            #             win.blit(proj12,(pjxr12,FIGy1))
                            #             p1pjcon-=1  
                            #             pj12=True  
                            #         # if p1pjcon==2:
                            #         #     win.blit(proj13,(pjxr13,FIGy1))
                            #         #     p1pjcon-=1 
                            #         #     pj13=True
                            #         # if p1pjcon==1:
                            #         #     win.blit(proj14,(pjxr14,FIGy1))
                            #         #     p1pjcon-=1 
                            #         #     pj14=True
                            #     if lastl1==True and p1pjcon>0:
                            #         if p1pjcon==4:
                            #             win.blit(proj11,(pjxl11,FIGy1))#the 4 diffrent projeciles and 4 diffrent images allowing for them to have their own coordinates
                            #             p1pjcon-=1
                            #             pj11=True
                            #         if p1pjcon==3:
                            #             win.blit(proj12,(pjxl12,FIGy1))
                            #             p1pjcon-=1 
                            #             pj12=True    
                            #         # if p1pjcon==2:
                            #         #     win.blit(proj13,(pjxl13,FIGy1))
                            #         #     p1pjcon-=1 
                            #         #     pj13=True
                            #         # if p1pjcon==1:
                            #         #     win.blit(proj14,(pjxl14,FIGy1))
                            #         #     p1pjcon-=1 
                            #         #     pj14=True 
                        if spped2==True:#all of this is the same for player one except for player2 
                            if keyPressed[pygame.K_RIGHT]:  #same thing but for player 2 
                                FIGx2 +=speedy 
                                right2=True
                                left2=False
                                lastr2=True
                                lastl2=False 
                                lastd2=False
                                lastw2=False
                            if keyPressed[pygame.K_LEFT]:  
                                FIGx2-=speedy
                                right2=False
                                left2=True
                                lastr2=False
                                lastl2=True
                                lastd2=False
                                lastw2=False
                            if keyPressed[pygame.K_UP]:  
                                FIGy2-=speedy
                                lastr2=False
                                lastl2=False
                                lastd2=False
                                lastw2=True
                            if keyPressed[pygame.K_DOWN]:
                                FIGy2 +=speedy
                                lastr2=False
                                lastl2=False
                                lastd2=True
                                lastw2=False
                            if FIGx2==10:#boder controls for player 2
                                FIGx2+=30
                            if FIGx2==WIDTH-30:
                                FIGx2-=30
                            if FIGy2==10:
                                FIGy2+=30
                            if FIGy2==HEIGHT-30:
                                FIGy2-=30
                        if FIGx1==boldx1+50 and FIGy1>boldy1-50 and FIGy1<boldy1+50:#borders for the cube as they hit you back if you walk into them
                            FIGx1+=50
                        if FIGx1==boldx1-50 and FIGy1>boldy1-50 and FIGy1<boldy1+50:
                            FIGx1-=50     
                        if FIGy1==boldy1+50 and FIGx1>boldx1-50 and FIGx1<boldx1+50:
                            FIGy1+=50   
                        if FIGy1==boldy1-50 and FIGx1>boldx1-50 and FIGx1<boldx1+50:
                            FIGy1-=50
                        if FIGx1==boldx2+50 and FIGy1>boldy2-50 and FIGy1<boldy2+50:
                            FIGx1+=50
                        if FIGx1==boldx2-50 and FIGy1>boldy2-50 and FIGy1<boldy2+50:
                            FIGx1-=50     
                        if FIGy1==boldy2+50 and FIGx1>boldx2-50 and FIGx1<boldx2+50:
                            FIGy1+=50   
                        if FIGy1==boldy2-50 and FIGx1>boldx2-50 and FIGx1<boldx2+50:
                            FIGy1-=50 
                        if FIGx1==boldx3+50 and FIGy1>boldy3-50 and FIGy1<boldy3+50:
                            FIGx1+=50
                        if FIGx1==boldx3-50 and FIGy1>boldy3-50 and FIGy1<boldy3+50:
                            FIGx1-=50     
                        if FIGy1==boldy3+50 and FIGx1>boldx3-50 and FIGx1<boldx3+50:
                            FIGy1+=50   
                        if FIGy1==boldy3-50 and FIGx1>boldx3-50 and FIGx1<boldx3+50:
                            FIGy1-=50 
                        if FIGx1==boldx4+50 and FIGy1>boldy4-50 and FIGy1<boldy4+50:
                            FIGx1+=50
                        if FIGx1==boldx4-50 and FIGy1>boldy4-50 and FIGy1<boldy4+50:
                            FIGx1-=50     
                        if FIGy1==boldy4+50 and FIGx1>boldx4-50 and FIGx1<boldx4+50:
                            FIGy1+=50   
                        if FIGy1==boldy4-50 and FIGx1>boldx4-50 and FIGx1<boldx4+50:
                            FIGy1-=50
                        if FIGx2==boldx1+50 and FIGy2>boldy1-50 and FIGy2<boldy1+50:#borders for the cube as they hit you back if you walk into them
                            FIGx2+=50
                        if FIGx2==boldx1-50 and FIGy2>boldy1-50 and FIGy2<boldy1+50:
                            FIGx2-=50     
                        if FIGy2==boldy1+50 and FIGx2>boldx1-50 and FIGx2<boldx1+50:
                            FIGy2+=50   
                        if FIGy2==boldy1-50 and FIGx2>boldx1-50 and FIGx2<boldx1+50:
                            FIGy2-=50
                        if FIGx2==boldx2+50 and FIGy2>boldy2-50 and FIGy2<boldy2+50:
                            FIGx2+=50
                        if FIGx2==boldx2-50 and FIGy2>boldy2-50 and FIGy2<boldy2+50:
                            FIGx2-=50     
                        if FIGy2==boldy2+50 and FIGx2>boldx2-50 and FIGx2<boldx2+50:
                            FIGy2+=50   
                        if FIGy2==boldy2-50 and FIGx2>boldx2-50 and FIGx2<boldx2+50:
                            FIGy2-=50 
                        if FIGx2==boldx3+50 and FIGy2>boldy3-50 and FIGy2<boldy3+50:
                            FIGx2+=50
                        if FIGx2==boldx3-50 and FIGy2>boldy3-50 and FIGy2<boldy3+50:
                            FIGx2-=50     
                        if FIGy2==boldy3+50 and FIGx2>boldx3-50 and FIGx2<boldx3+50:
                            FIGy2+=50   
                        if FIGy2==boldy3-50 and FIGx2>boldx3-50 and FIGx2<boldx3+50:
                            FIGy2-=50 
                        if FIGx2==boldx4+50 and FIGy2>boldy4-50 and FIGy2<boldy4+50:
                            FIGx2+=50
                        if FIGx2==boldx4-50 and FIGy2>boldy4-50 and FIGy2<boldy4+50:
                            FIGx2-=50     
                        if FIGy2==boldy4+50 and FIGx2>boldx4-50 and FIGx2<boldx4+50:
                            FIGy2+=50   
                        if FIGy2==boldy4-50 and FIGx2>boldx4-50 and FIGx2<boldx4+50:
                            FIGy2-=50                        
                        if pl2hc==5:#this ends the game whenever a player has collected 5 flags
                            play=False
                            score=pl2hc*2000-(pl1hc*200)#scores based on number of times you got hit
                            end=True
                            counter+=1
                        if pl1hc==5:
                            play=False
                            score=pl1hc*2000-(pl2hc*200)
                            end=True
                            counter+=1
                            pygame.time.delay(100)
                        redrawGameWindowforp1()
                        coinspawn()
                        gobspawn()  
                if end==True and  counter is 8:
                    updateFile()
                    create_NewWindow("Good Game")#creates a endgame window
                    win.fill(WHITE)
                    display_Title("Good Game",40)#
                    Menu_function(EndMessages,150)#ssame as the other menus but also with the score thing and it allows us to travel to other parts of the game like hte menu
                    #actiates the endgame if statments
                if end==True and xp >x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 8:
                    counter-=1 
                    newgame1=True
                    newgame2=False
                    gem2=False
                if end==True and xp >x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 8:
                    counter-=1 
                    newgame1=False
                    newgame2=True 
                    gem2==True
                if end==True and xp >x and xp<x+wbox and yp>y and yp<545 and yp>445 and counter is 8:
                    counter-=8
                    display_Title("TestyGame",y)
                    Menu_function(gameMessages,150)
                if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and stgm==True and counter is 7 or newgame2==True and counter is 7:#the stgm is theer because it will say if the mouse is at that position and counter is 7 level 2 will play but only if you choose it first. this is due to the fact that in other areas it would trigger level 2 without meaning too so this prevents it
                    walkCount1= 0
                    gem2=True
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
                    newgame1=False
                    gm2=False
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
                    FIGx1=150
                    FIGy1=HEIGHT-150
                    FIGx2=WIDTH-150
                    FIGy2= HEIGHT-150
                    end=False
                    lavacount=0
                    pl1hc=0
                    pl2hc=0
                    P1x=FIGx1
                    P2x=FIGx2
                    P1y=FIGy1-45
                    P2y=FIGy2-45
                    pjxr11=FIGx1+40#all of these pj variables represent the projeciles and the diffrent positions I should spawn them dpending on the direction the player is facing when firing
                    pjy11=FIGy1
                    pjxl11=FIGx1-40
                    pjxr21=FIGx2+40
                    pjy21=FIGy2
                    pjxl21=FIGx2-40
                    pjxr12=FIGx1+40
                    pjy12=FIGy1
                    play=True
                    pjxl12=FIGx1-40
                    pjxr22=FIGx2+40
                    pjy22=FIGy2
                    pjxl22=FIGx2-40
                    pjxr13=FIGx1+40
                    pjy13=FIGy1
                    pjxl13=FIGx1-40
                    pjxr23=FIGx2+40
                    pjy23=FIGy2
                    pjxl23=FIGx2-40
                    pjxr14=FIGx1+40
                    pjy14=FIGy1
                    pjxl14=FIGx1-40
                    pjxr24=FIGx2+40
                    pjy24=FIGy2
                    pjxl24=FIGx2-40
                    flgcount=0
                    pj11=False
                    pj12=False
                    pj13=False
                    pj14=False
                    pj21=False
                    pj22=False
                    pj23=False
                    pj24=False
                    speedx=10
                    speedy=10
                    P1y=FIGy1-75#shows which player is which by stayign directicly above them
                    P2y=FIGy2-75
                    Flgx=random.randint(50,WIDTH-50)#
                    flgy=random.randint(50,HEIGHT-50)
                    create_NewgWindow('Level 2')
                    # if HEIGHT==700:
                    #     win.blit(sebg,(0,0))
                    # if HEIGHT==900:
                    #     win.blit(nibg,(0,0))
                    # if HEIGHT==1000:#bases type of background needed on height
                    #     win.blit(tebg,(0,0))
                    # win.blit(StR1,(FIGx1,FIGy1))
                    # win.blit(StL2,(FIGx2, FIGy2))
                    # win.blit(p1,(P1x,P1y))
                    # win.blit(p2,(P2x,P2y))
                    # pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
                    # pygame.draw.rect(win,ORANGE,bolder2)     
                    # pygame.draw.rect(win,ORANGE,bolder3)  
                    # pygame.draw.rect(win,ORANGE,bolder4)
                    # my_timer.reset()
                    # my_timer = Stopwatch()
                    while play:
                        pygame.time.delay(100) #milliseconds 
                        for anyThing in pygame.event.get(): #variable for anytrhing that happneds in py to listen to keyboard and mouse
                            if anyThing.type ==pygame.QUIT: #says if Quit something happends
                                play = False
                                run =False
                        keyPressed= pygame.key.get_pressed()#records keyboard movement
                        P1y=FIGy1-75
                        P2y=FIGy2-75
                        if spped1:  #this if statment allows me to disable a single players movement if they are stunned
                            if keyPressed[pygame.K_d]: 
                                FIGx1 +=speedy #negative or postive depsending on direction
                                right1=True#for direction
                                left1=False
                                lastr1=True#for the last direction if an idle pose is needed
                                lastl1=False
                                lastd1=False
                                lastw1=False
                            if keyPressed[pygame.K_a]:  
                                FIGx1 -=speedy
                                right1=False
                                left1=True
                                lastr1=False
                                lastl1=True
                                lastd1=False
                                lastw1=False
                            if keyPressed[pygame.K_w]:  #wasn't able to get up and down sprite so reused the other walking sprites but you do still travel in that direction
                                FIGy1-=speedy
                                lastr1=False
                                lastl1=False
                                lastd1=False
                                lastw1=True      
                            if keyPressed [pygame.K_s]:
                                FIGy1 +=speedy
                                lastr1=False
                                lastl1=False
                                lastw1=False
                                lastd1=True
                            if FIGx1==10:#border controls for player 1 that buffs them back if they walk into it
                                FIGx1+=30
                            if FIGx1==WIDTH-30:
                                FIGx1-=30
                            if FIGy1==10:
                                FIGy1+=30
                            if FIGy1==HEIGHT-30:
                                FIGy1-=30
                            # if keyPressed[pygame.K_f]:#fires projectile depending on directions and limits it to only 4 projectiles per player allowed to be fired on the screen
                            #     if lastr1==True and p1pjcon>0:#you can fire left and right (not up and down becuase i could find good back sprites for facing does directions so while you can move in them you can shot in them)
                            #         if p1pjcon==4:
                            #             win.blit(proj11,(pjxr11,FIGy1))
                            #             p1pjcon-=1
                            #             pj11=True
                            #         if p1pjcon==3:
                            #             win.blit(proj12,(pjxr12,FIGy1))
                            #             p1pjcon-=1  
                            #             pj12=True  
                            #         # if p1pjcon==2:
                            #         #     win.blit(proj13,(pjxr13,FIGy1))
                            #         #     p1pjcon-=1 
                            #         #     pj13=True
                            #         # if p1pjcon==1:
                            #         #     win.blit(proj14,(pjxr14,FIGy1))
                            #         #     p1pjcon-=1 
                            #         #     pj14=True
                            #     if lastl1==True and p1pjcon>0:
                            #         if p1pjcon==4:
                            #             win.blit(proj11,(pjxl11,FIGy1))#the 4 diffrent projeciles and 4 diffrent images allowing for them to have their own coordinates
                            #             p1pjcon-=1
                            #             pj11=True
                            #         if p1pjcon==3:
                            #             win.blit(proj12,(pjxl12,FIGy1))
                            #             p1pjcon-=1 
                            #             pj12=True    
                            #         # if p1pjcon==2:
                            #         #     win.blit(proj13,(pjxl13,FIGy1))
                            #         #     p1pjcon-=1 
                            #         #     pj13=True
                            #         # if p1pjcon==1:
                            #         #     win.blit(proj14,(pjxl14,FIGy1))
                            #         #     p1pjcon-=1 
                            #         #     pj14=True 
                        if spped2==True:#all of this is the same for player one except for player2 
                            if keyPressed[pygame.K_RIGHT]:  #same thing but for player 2 
                                FIGx2 +=speedy 
                                right2=True
                                left2=False
                                lastr2=True
                                lastl2=False 
                                lastd2=False
                                lastw2=False
                            if keyPressed[pygame.K_LEFT]:  
                                FIGx2-=speedy
                                right2=False
                                left2=True
                                lastr2=False
                                lastl2=True
                                lastd2=False
                                lastw2=False
                            if keyPressed[pygame.K_UP]:  
                                FIGy2-=speedy
                                lastr2=False
                                lastl2=False
                                lastd2=False
                                lastw2=True
                            if keyPressed[pygame.K_DOWN]:
                                FIGy2 +=speedy
                                lastr2=False
                                lastl2=False
                                lastd2=True
                                lastw2=False
                            if FIGx2==10:#boder controls for player 2
                                FIGx2+=30
                            if FIGx2==WIDTH-30:
                                FIGx2-=30
                            if FIGy2==10:
                                FIGy2+=30
                            if FIGy2==HEIGHT-30:
                                FIGy2-=30
                        if FIGx1==boldx1+50 and FIGy1>boldy1-50 and FIGy1<boldy1+50:#borders for the cube as they hit you back if you walk into them
                            FIGx1+=50
                        if FIGx1==boldx1-50 and FIGy1>boldy1-50 and FIGy1<boldy1+50:
                            FIGx1-=50     
                        if FIGy1==boldy1+50 and FIGx1>boldx1-50 and FIGx1<boldx1+50:
                            FIGy1+=50   
                        if FIGy1==boldy1-50 and FIGx1>boldx1-50 and FIGx1<boldx1+50:
                            FIGy1-=50
                        if FIGx1==boldx2+50 and FIGy1>boldy2-50 and FIGy1<boldy2+50:
                            FIGx1+=50
                        if FIGx1==boldx2-50 and FIGy1>boldy2-50 and FIGy1<boldy2+50:
                            FIGx1-=50     
                        if FIGy1==boldy2+50 and FIGx1>boldx2-50 and FIGx1<boldx2+50:
                            FIGy1+=50   
                        if FIGy1==boldy2-50 and FIGx1>boldx2-50 and FIGx1<boldx2+50:
                            FIGy1-=50 
                        if FIGx1==boldx3+50 and FIGy1>boldy3-50 and FIGy1<boldy3+50:
                            FIGx1+=50
                        if FIGx1==boldx3-50 and FIGy1>boldy3-50 and FIGy1<boldy3+50:
                            FIGx1-=50     
                        if FIGy1==boldy3+50 and FIGx1>boldx3-50 and FIGx1<boldx3+50:
                            FIGy1+=50   
                        if FIGy1==boldy3-50 and FIGx1>boldx3-50 and FIGx1<boldx3+50:
                            FIGy1-=50 
                        if FIGx1==boldx4+50 and FIGy1>boldy4-50 and FIGy1<boldy4+50:
                            FIGx1+=50
                        if FIGx1==boldx4-50 and FIGy1>boldy4-50 and FIGy1<boldy4+50:
                            FIGx1-=50     
                        if FIGy1==boldy4+50 and FIGx1>boldx4-50 and FIGx1<boldx4+50:
                            FIGy1+=50   
                        if FIGy1==boldy4-50 and FIGx1>boldx4-50 and FIGx1<boldx4+50:
                            FIGy1-=50
                        if FIGx2==boldx1+50 and FIGy2>boldy1-50 and FIGy2<boldy1+50:#borders for the cube as they hit you back if you walk into them
                            FIGx2+=50
                        if FIGx2==boldx1-50 and FIGy2>boldy1-50 and FIGy2<boldy1+50:
                            FIGx2-=50     
                        if FIGy2==boldy1+50 and FIGx2>boldx1-50 and FIGx2<boldx1+50:
                            FIGy2+=50   
                        if FIGy2==boldy1-50 and FIGx2>boldx1-50 and FIGx2<boldx1+50:
                            FIGy2-=50
                        if FIGx2==boldx2+50 and FIGy2>boldy2-50 and FIGy2<boldy2+50:
                            FIGx2+=50
                        if FIGx2==boldx2-50 and FIGy2>boldy2-50 and FIGy2<boldy2+50:
                            FIGx2-=50     
                        if FIGy2==boldy2+50 and FIGx2>boldx2-50 and FIGx2<boldx2+50:
                            FIGy2+=50   
                        if FIGy2==boldy2-50 and FIGx2>boldx2-50 and FIGx2<boldx2+50:
                            FIGy2-=50 
                        if FIGx2==boldx3+50 and FIGy2>boldy3-50 and FIGy2<boldy3+50:
                            FIGx2+=50
                        if FIGx2==boldx3-50 and FIGy2>boldy3-50 and FIGy2<boldy3+50:
                            FIGx2-=50     
                        if FIGy2==boldy3+50 and FIGx2>boldx3-50 and FIGx2<boldx3+50:
                            FIGy2+=50   
                        if FIGy2==boldy3-50 and FIGx2>boldx3-50 and FIGx2<boldx3+50:
                            FIGy2-=50 
                        if FIGx2==boldx4+50 and FIGy2>boldy4-50 and FIGy2<boldy4+50:
                            FIGx2+=50
                        if FIGx2==boldx4-50 and FIGy2>boldy4-50 and FIGy2<boldy4+50:
                            FIGx2-=50     
                        if FIGy2==boldy4+50 and FIGx2>boldx4-50 and FIGx2<boldx4+50:
                            FIGy2+=50   
                        if FIGy2==boldy4-50 and FIGx2>boldx4-50 and FIGx2<boldx4+50:
                            FIGy2-=50                        
                        if pl2hc==5:#this ends the game whenever a player has collected 5 flags
                            play=False
                            score=pl2hc*2000-(pl1hc*200)+1000#scores based on number of times you got hit
                            end=True
                            counter+=1
                        if pl1hc==5:
                            play=False
                            score=pl1hc*2000-(pl2hc*200)+1000
                            end=True
                            counter+=1
                            pygame.time.delay(100)
                        redrawGameWindowforp1()
                        coinspawn()  
                        lavspawn()
                # if end==True and  counter is 8:
                #     create_NewWindow("Good Game")#creates a endgame window
                #     win.fill(WHITE)
                #     display_Title("Good Game",40)#
                #     Menu_function(EndMessages,150)#ssame as the other menus but also with the score thing and it allows us to travel to other parts of the game like hte menu
                #     #actiates the endgame if statments
                # if end==True and xp >x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 8:
                #     counter-=1 
                #     newgame1=True
                #     newgame2=False
                # if end==True and xp >x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 8:
                #     counter-=1 
                #     newgame1=False
                #     newgame2=True    
                if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 7:
                    xp=0
                    yp=0 
                    win.fill(WHITE)
                    display_Title("Testy Game",y)
                    Menu_function(gameMessages,150)
                    counter-=7
                    pygame.time.delay(100)
pygame.quit()
