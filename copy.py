        if lavacount==0:
        pygame.time.delay(5000)
        lvx= random.randint(50,WIDTH-50)#when there is no flag the count is zero which triggers the coords to randomize after a delay and adds to the count so it dosen't happen untill the flag is collected
        lvy= random.randint(50,HEIGHT-50)
        lavacount+=1
    if lavacount==1:
        win.blit(lamon,(lvx,lvy))
    if lvx==boldx1+85 or lvx==boldx1-85 or lvx==boldx2+85 or lvx==boldx2-85 or lvx==boldx3+85 or lvx==boldx3-85 or lvx==boldx4+85 or lvx==boldx4-85 or lvy==boldy1+85 or lvy==boldy1-85 or lvy==boldy2+85 or lvy==boldy2-85 or lvy==boldy3+85 or lvy== boldy3-85 or lvy== boldy4+85 or lvy== boldy4-85:
        lvx= random.randint(50,WIDTH-50)# if the flag lands on a wall postition it will instantly randomize the coordinates so the flag isn't stuck
        lvy= random.randint(50,HEIGHT-50)  
    if lvx=-FIGx1+30 or lvx==FIGx1-30 or lvy==FIGy1+30 or lvy==FIGy1-30: #as with other extra numbers these gave some linency so you don't have to be right on top of it  
        lavacount=0
        spped1=False
        pygame.time.delay(5000)
        spped1=True
    if lvx==FIGx2+30 or lvx==FIGx2-30 or lvy==FIGy2-30 or lvy==FIGy2+30
        lavacount=0
        spped2=False
        pygame.time.delay(5000)
        spped2=True
        