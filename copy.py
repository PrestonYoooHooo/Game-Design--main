def gobspawn():
    global gobcount
    global pl1hc
    global pl2hc
    if gobcount==0:
        gbx= random.randint(50,WIDTH-50)#randomizes thgbye lava coordds when there isn't lava already on the screen
        gby= random.randint(50,HEIGHT-50)
        gobcount+=1
    if gobcount==1:#shows the lava when the coords are found
        win.blit(gob,(gbx,gby))
    if gbx==boldx1+85 or gbx==boldx1-85 or gbx==boldx2+85 or gbx==boldx2-85 or gbx==boldx3+85 or gbx==boldx3-85 or gbx==boldx4+85 or gbx==boldx4-85 or gby==boldy1+85 or gby==boldy1-85 or gby==boldy2+85 or gby==boldy2-85 or gby==boldy3+85 or gby== boldy3-85 or gby== boldy4+85 or gby== boldy4-85:
        gbx= random.randint(50,WIDTH-50)# if the lava lands on a wall postition it will instantly randomize the coordinates so the flag isn't stuck
        gby= random.randint(50,HEIGHT-50)  
    if gbx>boldx1-30 and gbx<boldx1+30 and gby>boldx1-30 and gby<boldx1+30:
        gobcount+=1
    if gbx>boldx2-30 and gbx<boldx2+30 and gby>boldy2-30 and gby<boldy2+30:
        gobcount+=1
    if gbx>boldx3-30 and gbx<boldx3+30 and gby>boldx3-30 and gby<boldx3+30:
        gobcount+=1
    if gbx>boldx4-30 and gbx<boldx4+30 and gby>boldy4-30 and gby<boldy4+30:
        gobcount+=1
    if FIGx1>gbx-30 and FIGx1<gbx+30 and FIGy1>gbx-30 and FIGy1<gbx+30: #as with other extra numbers these gave some linency so you don't have to be right on top of it  
        gobcount-=1
        pl1hc-=1
    if FIGy1>gby-30 and FIGx1<gby+30 and FIGy1>gby-30 and FIGy1<gby+30:
        gobcount-=1
        pl1hc-=1
    if FIGx2>gbx-30 and FIGx2<gbx+30 and FIGy2>gbx-30 and FIGy2<gbx+30: #as with other extra numbers these gave some linency so you don't have to be right on top of it  
        gobcount-=1
        pl2hc-=1
    if FIGy2>gby-30 and FIGx2<gby+30 and FIGy2>gby-30 and FIGy2<gby+30:
        gobcount-=1
        pl2hc-=1

 
 