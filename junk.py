  # win.blit(eibg(0,0))
                            # win.blit(StR1(FIGx1,FIGy1))
                            # win.blit(StL2,FIGx2,FIGy2)
                            # pygame.display.flip()
                            # if keyPressed[pygame.K_SLASH]:
                            #     if lastr2==True and p2pjcon>0:
                            #         if p2pjcon==4:
                            #             win.blit(proj21,(pjxr21,pjy11))
                            #             p2pjcon-=1
                            #             pj21=True
                            #         if p2pjcon==3:
                            #             win.blit(proj22,(pjxr22,pjy12))
                            #             p2pjcon-=1 
                            #             pj22=True    
                                    # if p2pjcon==2:
                                    #     win.blit(proj23,(pjxr23,pjy13))
                                    #     p2pjcon-=1 
                                    #     pj23=True
                                    # if p2pjcon==1:
                                    #     win.blit(proj24,(pjxr24,pjy14))
                                    #     p2pjcon-=1
                                    #     pj24=True 
                                # if lastl2==True and p2pjcon>0:
                                #     if p2pjcon==4:
                                #         win.blit(proj21,(pjxr21,pjy21))
                                #         p2pjcon-=1
                                #         pj21=True
                                #     if p2pjcon==3:
                                #         win.blit(proj22,(pjxr22,pjy22))
                                #         p2pjcon-=1  
                                #         pj22=True   
                                    # if p2pjcon==2:
                                    #     win.blit(proj23,(pjxr23,pjy23))
                                    #     p2pjcon-=1 
                                    #     pj23=True
                                    # if p2pjcon==1:
                                    #     win.blit(proj24,(pjxr24,pjy24))
                                    #     p2pjcon-=1 
                                    #     pj24=True
                #         if pj11==True and projcount11>0 and lastl1==True:#for every second the projectile is one screen it will travel depending on direction of shot and will only stop whe its counter reaches 0 causing it to disaapear or when it hits a playerer or a wall, all of these reset the counter and allow for anohter projectile to be fired
                #             pjxl11+=20
                #             projcount11-=1
                #             if pjxl11 == boldx1+80 or pjxl11 ==boldx2+80 or pjxl11 ==boldx3+80 or pjxl11 ==boldx4+80:#These are for the coords of the wall and will delete the projectiels if the touch them
                #                 pj11=False
                #                 projcount11=30
                #                 pjxl11=FIGx1-40
                #                 pjy11=FIGy1
                #             if pjy11 == boldy1+80 or pjy11 ==boldy2+80 or pjy11 ==boldy3+80 or pjy11 ==boldy4+80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxl11=FIGx1-40  
                #                 pjy11=FIGy1  
                #             if pjxl11 == boldx1-80 or pjxl11 ==boldx2-80 or pjxl11 ==boldx3-80 or pjxl11 ==boldx4-80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxl11=FIGx1-40
                #                 pjy11=FIGy1
                #             if pjy11 == boldy1-80 or pjy11 ==boldy2-80 or pjy11 ==boldy3-80 or pjy11 ==boldy4-80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxl11=FIGx1-40  
                #                 pjy11=FIGy1  
                #             if pjxl11==10:
                #                 pjxl11=WIDTH-10
                #             if pjxl11==WIDTH-10:
                #                 pjxl11=10
                #             if pjy11==10:
                #                 pjyl1=HEIGHT-10
                #             if pjy11==HEIGHT-10:
                #                 pjy11=10  
                #         elif pj11==False or projcount11<1:#this kills the projecile and resets the coordinates for the projectile after it disappears
                #             pj11=False
                #             projcount11=30
                #             pjxl11=FIGx1-40  
                #             pjy11=FIGy1 
                #         if pj12==True and projcount12>0 and lastl1==True:
                #             pjxl12+=20
                #             projcount12-=1
                #             if pjxl12 == boldx1+80 or pjxl12 ==boldx2+80 or pjxl12 ==boldx3+80 or pjxl12 ==boldx4+80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxl12=FIGx1-40
                #                 pjy12=FIGy1
                #             if pjy12 == boldy1+80 or pjy12 ==boldy2+80 or pjy12 ==boldy3+80 or pjxl12 ==boldy4+80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxl12=FIGx1-40  
                #                 pjy12=FIGy1  
                #             if pjxl12 == boldx1-80 or pjxl12 == boldx2-80 or pjxl12 == boldx3-80 or pjxl12 == boldx4-80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxl12=FIGx1-40
                #                 pjy12=FIGy1
                #             if pjy12 == boldy1-80 or pjy12 == boldy2-80 or pjy12 == boldy3-80 or pjy12 == boldy4-80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxl12=FIGx1-40  
                #                 pjy12=FIGy1  
                #             if pjxl12==10:
                #                 pjxl12=WIDTH-10
                #             if pjxl12==WIDTH-10:
                #                 pjxl12=10
                #             if pjy12==10:
                #                 pjyl2=HEIGHT-10
                #             if pjy12==HEIGHT-10:
                #                 pjy12=10  
                #         elif pj12==False or projcount12<1:
                #             pj12=False
                #             projcount12=30
                #             pjxl12=FIGx1-40  
                #             pjy12=FIGy1
                #         # if pj13==True and projcount13>0 and lastl1==True:
                #         #     pjxl13+=20
                #         #     projcount13-=1
                #         #     if pjxl13 == boldx1+80 or pjxl13 == +80 or pjxl13 == boldx3+80 or pjxl13 == boldx4+80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxl13=FIGx1-40
                #         #         pjy13=FIGy1
                #         #     if pjy13 == boldy1+80 or pjy13 == boldy2+80 or pjy13 == boldy3+80 or pjy13 == boldy4+80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxl13=FIGx1-40  
                #         #         pjy13=FIGy1  
                #         #     if pjxl13 == boldx1-80 or pjxl13 == boldx2-80 or pjxl13 == boldx3-80 or pjxl13 == boldx4-80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxl13=FIGx1-40
                #         #         pjy13=FIGy1
                #         #     if pjy13 == boldy1-80 or pjy13 == boldy2-80 or pjy13 == boldy3-80 or pjy13 == boldy4-80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxl13=FIGx1-40  
                #         #         pjy13=FIGy1 
                #         #     if pjxl13==10:
                #         #         pjxl13=WIDTH-10
                #         #     if pjxl13==WIDTH-10:
                #         #         pjxl13=10
                #         #     if pjy13==10:
                #         #         pjyl3=HEIGHT-10
                #         #     if pjy13==HEIGHT-10:
                #         #         pjy13=10
                #         # elif pj13==False or projcount13<1:
                #         #     pj13=False
                #         #     projcount13=30
                #         #     pjxl13=FIGx1-40  
                #         #     pjy13=FIGy1
                #         # if pj14==True and projcount13>0 and lastl1==True:
                #         #     pjxl14+=20
                #         #     projcount14-=1
                #         #     if pjxl14 == boldx1+80 or pjxl14 == boldx2+80 or pjxl14 == boldx3+80 or pjxl14 == boldx4+80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxl14=FIGx1-40
                #         #         pjy14=FIGy1
                #         #     if pjy14 == boldy1+80 or pjy14 == boldy2+80 or pjy14 == boldy3+80 or pjy14 == boldy4+80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxl14=FIGx1-40  
                #         #         pjy14=FIGy1  
                #         #     if pjxl14 == boldx1-80 or pjxl14 == boldx2-80 or pjxl14 == boldx3-80 or pjxl14 == boldx4-80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxl14=FIGx1-40
                #         #         pjy14=FIGy1
                #         #     if pjy14 == boldy1-80 or pjy14 == boldy2-80 or pjy14 == boldy3-80 or pjy14 == boldy4-80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxl14=FIGx1-40  
                #         #         pjy14=FIGy1  
                #         #     if pjxl14==10:
                #         #         pjxl14=WIDTH-10
                #         #     if pjxl14==WIDTH-10:
                #         #         pjxl14=10
                #         #     if pjy14==10:
                #         #         pjyl4=HEIGHT-10
                #         #     if pjy14==HEIGHT-10:
                #         #         pjy14=10
                #         # elif pj14==False or projcount14<1:
                #         #     pj14=False
                #         #     projcount14=30
                #         #     pjxl14=FIGx1-40  
                #         #     pjy14=FIGy1
                #         if pj21==True and projcount21>0 and lastl2==True:
                #             pjxl21+=20
                #             projcount21-=1
                #             if pjxl21 == boldx1+80 or pjxl21 == boldx2+80 or pjxl21 == boldx3+80 or pjxl21 == boldx4+80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxl21=FIGx2-40
                #                 pjy21=FIGy2
                #             if pjy21 == boldy1+80 or pjy21 == boldy2+80 or pjy21 == boldy3+80 or pjy21 == boldy4+80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxl21=FIGx2-40  
                #                 pjy21=FIGy2  
                #             if pjxl21 == boldx1-80 or pjxl21 == boldx2-80 or pjxl21 == boldx3-80 or pjxl21 == boldx4-80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxl21=FIGx2-40
                #                 pjy21=FIGy2
                #             if pjy21 == boldy1-80 or pjy21 == boldy2-80 or pjy21 == boldy3-80 or pjy21 == boldy4-80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxl21=FIGx2-40  
                #                 pjy21=FIGy2
                #             if pjxl21==10:
                #                 pjxl21=WIDTH-10
                #             if pjxl21==WIDTH-10:
                #                 pjxl21=10
                #             if pjy21==10:
                #                 pjy21=HEIGHT-10
                #             if pjy21==HEIGHT-10:
                #                 pjy21=10  
                #         elif pj21==False or projcount21<1:
                #             pj21=False
                #             projcount21=30
                #             pjxl21=FIGx2-40  
                #             pjy21=FIGy2 
                #         if pj22==True and projcount22>0 and lastl2==True:
                #             pjxl22+=20
                #             projcount22-=1
                #             if pjxl22 == boldx1+80 or pjxl22 == boldx2+80 or pjxl22 == boldx3+80 or pjxl22 == boldx4+80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxl22=FIGx2-40
                #                 pjy22=FIGy2
                #             if pjy22 == boldy1+80 or pjy22 == boldy2+80 or pjy22 == boldy3+80 or pjy22 == boldy4+80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxl22=FIGx2-40  
                #                 pjy22=FIGy2  
                #             if pjxl22 == boldx1-80 or pjxl22 == boldx2-80 or pjxl22 == boldx3-80 or pjxl22 == boldx4-80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxl22=FIGx2-40
                #                 pjy22=FIGy2
                #             if pjy22 == boldy1-80 or pjy22 == boldy2-80 or pjy22 == boldy3-80 or pjy22 == boldy4-80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxl22=FIGx2-40  
                #                 pjy22=FIGy2  
                #             if pjxl22==10:
                #                 pjxl22=WIDTH-10
                #             if pjxl22==WIDTH-10:
                #                 pjxl22=10
                #             if pjy22==10:
                #                 pjy22=HEIGHT-10
                #             if pjy22==HEIGHT-10:
                #                 pjy22=10  
                #         elif pj22==False or projcount22<1:
                #             pj22=False
                #             projcount22=30
                #             pjxl22=FIGx2-40  
                #             pjy22=FIGy2 
                #         # if pj23==True and projcount23>0 and lastl2==True:
                #         #     pjxl23+=20
                #         #     projcount23-=1
                #         #     if pjxl23 == boldx1+80 or pjxl23 == boldx2+80 or pjxl23 == boldx3+80 or pjxl23 == boldx4+80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxl23=FIGx2-40
                #         #         pjy23=FIGy2
                #         #     if pjy23 == boldy1+80 or pjy23 == boldy2+80 or pjy23 == boldy3+80 or pjy23 == boldy4+80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxl23=FIGx2-40  
                #         #         pjy23=FIGy2  
                #         #     if pjxl23 == boldx1-80 or pjxl23 == boldx2-80 or pjxl23 == boldx3-80 or pjxl23 == boldx4-80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxl23=FIGx2-40
                #         #         pjy23=FIGy2
                #         #     if pjy23 == boldy1-80 or pjy23 == boldy2-80 or pjy23 == boldy3-80 or pjy23 == boldy4-80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxl23=FIGx2-40  
                #         #         pjy23=FIGy2  
                #         #     if pjxl23==10:
                #         #         pjxl23=WIDTH-10
                #         #     if pjxl23==WIDTH-10:
                #         #         pjxl23=10
                #         #     if pjy23==10:
                #         #         pjy23=HEIGHT-10
                #         #     if pjy23==HEIGHT-10:
                #         #         pjy23=10  
                #         # elif pj23==False or projcount23<1:
                #         #     pj23=False
                #         #     projcount23=30
                #         #     pjxl23=FIGx2-40  
                #         #     pjy23=FIGy2 
                #         # if pj24==True and projcount24>0 and lastl2==True:
                #         #     pjxl24+=20
                #         #     projcount24-=1
                #         #     if pjxl24 == boldx1+80 or pjxl24 == boldx2+80 or pjxl24 == boldx3+80 or pjxl24 == boldx4+80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxl24=FIGx2-40
                #         #         pjy24=FIGy2
                #         #     if pjy24 == boldy1+80 or pjy24 == boldy2+80 or pjy24 == boldy3+80 or pjy24 == boldy4+80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxl24=FIGx2-40  
                #         #         pjy24=FIGy2  
                #         #     if pjxl24 == boldx1-80 or pjxl24 == boldx2-80 or pjxl24 == boldx3-80 or pjxl24 == boldx4-80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxl24=FIGx2-40
                #         #         pjy24=FIGy2
                #         #     if pjy24 == boldy1-80 or pjy24 == boldy2-80 or pjy24 == boldy3-80 or pjy24 == boldy4-80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxl24=FIGx2-40  
                #         #         pjy24=FIGy2 
                #         #     if pjxl24==10:
                #         #         pjxl24=WIDTH-10
                #         #     if pjxl24==WIDTH-10:
                #         #         pjxl24=10
                #         #     if pjy24==10:
                #         #         pjy24=HEIGHT-10
                #         #     if pjy24==HEIGHT-10:
                #         #         pjy24=10   
                #         # elif pj24==False or projcount24<1:
                #         #     pj24=False
                #         #     projcount24=30
                #         #     pjxl24=FIGx2-40  
                #         #     pjy24=FIGy2 
                #         if pj11==True and projcount11>0 and lastr1==True:
                #             pjxr11+=20
                #             projcount11-=1
                #             if pjxr11 == boldx1+80 or pjxr11 == boldx2+80 or pjxr11 == boldx3+80 or pjxr11 == boldx4+80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxr11=FIGx1+40
                #                 pjy11=FIGy1
                #             if pjy11 == boldy1+80 or pjy11 == boldy2+80 or pjy11 == boldy3+80 or pjy11 == boldy4+80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxr11=FIGx1+40  
                #                 pjy11=FIGy1  
                #             if pjxr11 == boldx1-80 or pjxr11 == boldx2-80 or pjxr11 == boldx3-80 or pjxr11 == boldx4-80:
                #                 pj11==False
                #                 projcount11=30
                #                 pjxr11=FIGx1+40
                #                 pjy11=FIGy1
                #             if pjy11 == boldy1-80 or pjy11 == boldy2-80 or pjy11 == boldy3-80 or pjy11 == boldy4-80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxr11=FIGx1+40  
                #                 pjy11=FIGy1 
                #             if pjxr11==10:
                #                 pjxr11=WIDTH-10
                #             if pjxr11==WIDTH-10:
                #                 pjxr11=10
                #             if pjy11==10:
                #                 pjy11=HEIGHT-10
                #             if pjy11==HEIGHT-10:
                #                 pjy11=10 
                #         elif pj11==False or projcount11<1:
                #             pj11=False
                #             projcount11=30
                #             pjxr11=FIGx1+40  
                #             pjy11=FIGy1 
                #         if pj12==True and projcount12>0 and lastr1==True:
                #             pjxr12+=20
                #             projcount12-=1
                #             if pjxr12 == boldx1+80 or pjxr12 == boldx2+80 or pjxr12 == boldx3+80 or pjxr12 == boldx4+80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxr12=FIGx1+40
                #                 pjy12=FIGy1
                #             if pjy12 == boldy1+80 or pjy12 == boldy2+80 or pjy12 == boldy3+80 or pjy12 == boldy4+80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxr12=FIGx1+40  
                #                 pjy12=FIGy1  
                #             if pjxr12 == boldx1-80 or pjxr12 == boldx2-80 or pjxr12 == boldx3-80 or pjxr12 == boldx4-80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxr12=FIGx1+40
                #                 pjy12=FIGy1
                #             if pjy12 == boldy1-80 or pjy12 == boldy2-80 or pjy12 == boldy3-80 or pjy12 == boldy4-80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxr12=FIGx1+40  
                #                 pjy12=FIGy1
                #             if pjxr12==10:
                #                 pjxr12=WIDTH-10
                #             if pjxr12==WIDTH-10:
                #                 pjxr12=10
                #             if pjy12==10:
                #                 pjy12=HEIGHT-10
                #             if pjy12==HEIGHT-10:
                #                 pjy12=10 
                #         elif pj12==False or projcount12<1:
                #             pj12=False
                #             projcount12=30
                #             pjxr12=FIGx1+40  
                #             pjy12=FIGy1
                #         # if pj13==True and projcount13>0 and lastr1==True:
                #         #     pjxr13+=20
                #         #     projcount13-=1
                #         #     if pjxr13 == boldx1+80 or pjxr13 ==boldx2+80 or pjxr13 ==boldx3+80 or pjxr13 ==boldx4+80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxr13=FIGx1+40
                #         #         pjy13=FIGy1
                #         #     if pjy13 == boldy1+80 or pjy13 == boldy2+80 or pjy13 == boldy3+80 or pjy13 == boldy4+80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxr13=FIGx1-40  
                #         #         pjy13=FIGy1  
                #         #     if pjxr13 == boldx1-80 or pjxr13 ==boldx2-80 or pjxr13 ==boldx3-80 or pjxr13 ==boldx4-80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxr13=FIGx1-40
                #         #         pjy13=FIGy1
                #         #     if pjy13 == boldy1-80 or pjy13 == boldy2-80 or pjy13 == boldy3-80 or pjy13 == boldy4-80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxr13=FIGx1-40  
                #         #         pjy13=FIGy1 
                #         #     if pjxr13==10:
                #         #         pjxr13==WIDTH-10
                #         #     if pjxr13==WIDTH-10:
                #         #         pjxr13==10
                #         #     if pjy13==10:
                #         #         pjy13=HEIGHT-10
                #         #     if pjy13==HEIGHT-10:
                #         #         pjy13==10 
                #         # elif pj13==False or projcount13<1:
                #         #     pj13=False
                #         #     projcount13=30
                #         #     pjxr13=FIGx1-40  
                #         #     pjy13=FIGy1
                #         # if pj14==True and projcount13>0 and lastr1==True:
                #         #     pjxr14+=20
                #         #     projcount14-=1
                #         #     if pjxr14 == boldx1+80 or pjxr14 == boldx2+80 or pjxr14 == boldx3+80 or pjxr14 == boldx4+80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxr14=FIGx1+40
                #         #         pjy14=FIGy1
                #         #     if pjy14 == boldy1+80 or pjy14 == boldy2+80 or pjy14 == boldy3+80 or pjy14 == boldy4+80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxr14=FIGx1+40  
                #         #         pjy14=FIGy1  
                #         #     if pjxr14 == boldx1-80 or pjxr14 == boldx2-80 or pjxr14 == boldx3-80 or pjxr14 == boldx4-80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxr14=FIGx1+40
                #         #         pjy14=FIGy1
                #         #     if pjy14 == boldy1-80 or pjy14 == boldy2-80 or pjy14 == boldy3-80 or pjy14 == boldy4-80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxr14=FIGx1+40  
                #         #         pjy14=FIGy1
                #         #     if pjxr14==10:
                #         #         pjxr14=WIDTH-10
                #         #     if pjxr14==WIDTH-10:
                #         #         pjxr14=10
                #         #     if pjy14==10:
                #         #         pjy14=HEIGHT-10
                #         #     if pjy14==HEIGHT-10:
                #         #         pjy14=10   
                #         # elif pj14==False or projcount14<1:
                #         #     pj14=False
                #         #     projcount14=30
                #         #     pjxr14=FIGx1+40  
                #         #     pjy14=FIGy1
                #         if pj21==True and projcount21>0 and lastr2==True:
                #             pjxr21+=20
                #             projcount21-=1
                #             if pjxr21 == boldx1+80 or pjxr21 == boldx2+80 or pjxr21 == boldx3+80 or pjxr21 == boldx4+80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxr21=FIGx2+40
                #                 pjy21=FIGy2
                #             if pjy21 == boldy1+80 or pjy21 == boldy2+80 or pjy21 == boldy3+80 or pjy21 == boldy4+80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxr21=FIGx2+40  
                #                 pjy21=FIGy2  
                #             if pjxr21 == boldx1-80 or pjxr21 == boldx2-80 or pjxr21 == boldx3-80 or pjxr21 == boldx4-80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxr21=FIGx2+40
                #                 pjy21=FIGy2
                #             if pjy21 == boldy1-80 or pjy21 == boldy2-80 or pjy21 == boldy3-80 or pjy21 == boldy4-80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxr21=FIGx2+40  
                #                 pjy21=FIGy2  
                #             if pjxr21==10:
                #                 pjxr21=WIDTH-10
                #             if pjxr21==WIDTH-10:
                #                 pjxr21=10
                #             if pjy21==10:
                #                 pjy21=HEIGHT-10
                #             if pjy21==HEIGHT-10:
                #                 pjy21=10 
                #         elif pj21==False or projcount21<1:
                #             pj21=False
                #             projcount21=30
                #             pjxr21=FIGx2-40  
                #             pjy21=FIGy2 
                #         # if pj22==True and projcount22>0 and lastr2==True:
                #         #     pjxr22+=20
                #         #     projcount22-=1
                #         #     if pjxr22 == boldx1+80 or pjxr22 == boldx2+80 or pjxr22 == boldx3+80 or pjxr22 == boldx4+80:
                #         #         pj22=False
                #         #         projcount22=30
                #         #         pjxr22=FIGx2+40
                #         #         pjy22=FIGy2
                #         #     if pjy22 == boldy1+80 or pjy22 == boldy2+80 or pjy22 == boldy3+80 or pjy22 == boldy4+80:
                #         #         pj22=False
                #         #         projcount22=30
                #         #         pjxr22=FIGx2+40  
                #         #         pjy22=FIGy2  
                #         #     if pjxr22 == boldx1-80 or pjxr22 == boldx2-80 or pjxr22 == boldx3-80 or pjxr22 == boldx4-80:
                #         #         pj22=False
                #         #         projcount22=30
                #         #         pjxr22=FIGx2+40
                #         #         pjy22=FIGy2
                #         #     if pjy22 == boldy1-80 or pjy22 == boldy2-80 or pjy22 == boldy3-80 or pjy22 == boldy4-80:
                #         #         pj22=False
                #         #         projcount22=30
                #         #         pjxr22=FIGx2+40  
                #         #         pjy22=FIGy2  
                #         #     if pjxr22==10:
                #         #         pjxr22=WIDTH-10
                #         #     if pjxr22==WIDTH-10:
                #         #         pjxr22=10
                #         #     if pjy22==10:
                #         #         pjy22=HEIGHT-10
                #         #     if pjy22==HEIGHT-10:
                #         #         pjy21=10 
                #         # elif pj22==False or projcount22<1:
                #         #     pj22=False
                #         #     projcount22=30
                #         #     pjxr22=FIGx2+40  
                #         #     pjy22=FIGy2 
                #         # if pj23==True and projcount23>0 and lastr2==True:
                #         #     pjxr23+=20
                #         #     projcount23-=1
                #         #     if pjxr23 == boldx1+80 or pjxr23 == boldx2+80 or pjxr23 == boldx3+80 or pjxr23 == boldx4+80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxr23=FIGx2+40
                #         #         pjy23=FIGy2
                #         #     if pjy23 == boldy1+80 or pjy23 == boldy2+80 or pjy23 == boldy3+80 or pjy23 == boldy4+80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxr23=FIGx2+40  
                #         #         pjy23=FIGy2  
                #         #     if pjxr23 == boldx1-80 or pjxr23 == boldx2-80 or pjxr23 == boldx3-80 or pjxr23 == boldx4-80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxr23=FIGx2+40
                #         #         pjy23=FIGy2
                #         #     if pjy23 == boldy1-80 or pjy23 == boldy2-80 or pjy23 == boldy3-80 or pjy23 == boldy4-80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxr23=FIGx2+40  
                #         #         pjy23=FIGy2  
                #         #     if pjxr23==10:
                #         #         pjxr23=WIDTH-10
                #         #     if pjxr23==WIDTH-10:
                #         #         pjxr23=10
                #         #     if pjy23==10:
                #         #         pjy23=HEIGHT-10
                #         #     if pjy23==HEIGHT-10:
                #         #         pjy23=10 
                #         # elif pj23==False or projcount23<1:
                #         #     pj23=False
                #         #     projcount23=30
                #         #     pjxr23=FIGx2+40  
                #         #     pjy23=FIGy2 
                #         # if pj24==True and projcount24>0 and lastr2==True:
                #         #     pjxr24+=20
                #         #     projcount24-=1
                #         #     if pjxr24 == boldx1+80 or pjxr24 == boldx2+80 or pjxr24 == boldx3+80 or pjxr24 == boldx4+80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxr24=FIGx2+40
                #         #         pjy24=FIGy2
                #         #     if pjy24 == boldy1+80 or pjy24 == boldy2+80 or pjy24 == boldy3+80 or pjy24 == boldy4+80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxr24=FIGx2+40  
                #         #         pjy24=FIGy2  
                #         #     if pjxr24 == boldx1-80 or pjxr24 == boldx2-80 or pjxr24 == boldx3-80 or pjxr24 == boldx4-80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxr24=FIGx2+40
                #         #         pjy24=FIGy2
                #         #     if pjy24 == boldy1-80 or pjy24 == boldy2-80 or pjy24 == boldy3-80 or pjy24 == boldy4-80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxr24=FIGx2+40  
                #         #         pjy24=FIGy2  
                #         #     if pjxr24==10:
                #         #         pjxr24=WIDTH-10
                #         #     if pjxr24==WIDTH-10:
                #         #         pjxr24=10
                #         #     if pjy24==10:
                #         #         pjy24=HEIGHT-10
                #         #     if pjy24==HEIGHT-10:
                #         #         pjy24=10 
                #         # elif pj24==False or projcount24<1:
                #         #     pj24=False
                #         #     projcount24=30
                #         #     pjxr24=FIGx2+40  
                #         #     pjy24=FIGy2 
                #         if pjxr11==FIGx1 or pjxr12==FIGx1 or pjxr21==FIGx1 or pjxr22==FIGx1 or pjxl11==FIGx1 or pjxl12==FIGx1 or pjxl21==FIGx1 or pjxl22==FIGx1 or pjy11==FIGy1 or pjy12==FIGy1 or pjy21==FIGy1 or pjy22==FIGy1:
                #             spped1=False#the projectiles pierce players but will still leave them stunned if they score a direct hit
                #             pl1hc+=1
                #             pygame.time.delay(5000)
                #             spped1=True
                #         if pjxr11==FIGx2 or pjxr12==FIGx2 or pjxr21==FIGx2 or pjxr22==FIGx2 or pjxl11==FIGx2 or pjxl12==FIGx2 or pjxl21==FIGx2 or pjxl22==FIGx2 or pjy11==FIGy2 or pjy12==FIGy2 or pjy21==FIGy2 or pjy22==FIGy2:
                #             spped2=False
                #             pl2hc+=1
                #             pygame.time.delay(5000)
                #             spped=True
                #         if FIGx1==boldx1+85 or FIGx1==boldx2+85 or FIGx1== boldx3+85 or FIGx1==boldx4+85:#These sets of commands will cause a player to reocil back and be stunned if they run into a wall
                #             spped1=False
                #             FIGx1+=50
                #             pygame.time.delay(3000)
                #             spped1=True
                #         if FIGx1==boldx1-85 or FIGx1==boldx2-85 or FIGx1==boldx3-85 or FIGx1==boldx4-85:
                #             spped1=False
                #             FIGx1-=50
                #             pygame.time.delay(3000)
                #             spped1=True
                #         if FIGy1==boldy1+85 or FIGy1==boldy2+85 or FIGy1==boldy3+85 or FIGy1==boldy4+85:
                #             spped1=False
                #             FIGy1+=50
                #             pygame.time.delay(3000)
                #             spped1=True
                #         if FIGy1==boldy1-85 or FIGy1==boldy2-85 or FIGy1==boldy3-85 or FIGy1==boldy4-85:
                #             spped1=False
                #             FIGy1-=50
                #             pygame.time.delay(3000)
                #             spped1=True
                #         if FIGx2==boldx1+85 or FIGx2==boldx2+85 or FIGx2==boldx3+85 or FIGx2==boldx4+85:
                #             spped2=False
                #             FIGx2+=50
                #             pygame.time.delay(3000)
                #             spped2=True
                #         if FIGx2==boldx1-85 or FIGx2==boldx2-85 or FIGx2==boldx3-85 or FIGx2==boldx4-85:
                #             spped2=False
                #             FIGx2-=50
                #             pygame.time.delay(3000)
                #             spped2=True
                #         if FIGy2==boldy1+85 or FIGy2==boldy2+85 or FIGy2==boldy3+85 or FIGy2==boldy4+85:
                #             spped2=False
                #             FIGy2+=50
                #             pygame.time.delay(3000)
                #             spped2=True
                #         if FIGy2==boldy1-85 or FIGy2==boldy2-85 or FIGy2==boldy3-85 or FIGy2==boldy4-85:
                #             spped2=False
                #             FIGy2-=50
                #             pygame.time.delay(3000)
                #             spped2=True
                #         if pl2hc==5:#this ends the game whenever a player has collected 5 flags
                #             play=False
                #             # scorepen=my_timer.get_seconds 
                #             score=pl2hc*2000-(pl1hc*200)#scores based on number of times you got hit
                #             end=True
                #         if pl1hc==5:
                #             play=False
                #             # scorepen=my_timer.get_seconds
                #             score=pl1hc*2000-(pl2hc*200)
                #             end=True
                #         redrawGameWindowforp1()
                #         # if HEIGHT==700:
                #         #     win.blit(sebg,(0,0))
                #         # if HEIGHT==800:
                #         #     win.blit(eibg,(0,0))
                #         # if HEIGHT==900:
                #         #     win.blit(nibg,(0,0))
                #         # if HEIGHT==1000:#bases type of background needed on height
                #         #     win.blit(tebg,(0,0))
                #         pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
                #         pygame.draw.rect(win,ORANGE,bolder2)     
                #         pygame.draw.rect(win,ORANGE,bolder3)  
                #         pygame.draw.rect(win,ORANGE,bolder4)
                #         pygame.display.update()
                #         pygame.display.flip()
                # if end==True:
                #     create_NewWindow("Good Game")#creates a endgame window
                #     win.fill(WHITE)
                #     display_Title("Good Game",40)#
                #     Menu_function(EndMessages,150)#ssame as the other menus but also with the score thing and it allows us to travel to other parts of the game like hte menu
                #     pygame.time.delay(100)
                #     counter+=1#actiates the endgame if statments
                
                # if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 8:
                #     newgame1=True
                #     newgame2=False
                #     counter-=1
                # if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 8:
                #     newgame1=False
                #     newgame2=True
                #     counter-=1
                # if xp>x and xp<x+wbox and yp>y and yp<445 and yp>545 and counter is 8:
                #     newgame1=False 
                #     newgame2=False
                #     display_Title("TestyGame",y)
                #     Menu_function(gameMessages,150)
                #     counter -=8
                # if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 7 or newgame2==True:
                #     walkCount1= 0
                #     walkCount2= 0
                #     play=True
                #     left1=False
                #     right1=False
                #     left2=False
                #     Right2=False
                #     hitstun=False 
                #     lastr1= True
                #     lastl1= False 
                #     lastr2= False
                #     lastl2= True
                #     lastw1=False
                #     lastw2=False
                #     lastd1=False
                #     lastd2=False
                #     pj11=False
                #     pj12=False
                #     pj13=False
                #     pj14=False
                #     pj21=False
                #     pj22=False
                #     pj23=False
                #     pj24=False
                #     escape2=True
                #     fl1count=0
                #     end=True
                #     FIGx1=50
                #     FIGy1=HEIGHT-50
                #     FIGx2=WIDTH-50
                #     FIGy2= HEIGHT-50
                #     fl2count=0
                #     pjxr11=FIGx1+40
                #     pjy11=FIGy1
                #     pjxl11=FIGx1-40
                #     pjxr21=FIGx2+0
                #     pjy21=FIGy2
                #     pjxl21=FIGx2-40
                #     pjxr12=FIGx1+40
                #     pjy12=FIGy1
                #     pjxl12=FIGx1-40
                #     pjxr22=FIGx2+40
                #     pjy22=FIGy2
                #     pjxl22=FIGx2-40
                #     pjxr13=FIGx1+40
                #     pjy13=FIGy1
                #     pjxl13=FIGx1-40
                #     pjxr23=FIGx2+40
                #     pjy23=FIGy2
                #     pjxl23=FIGx2-40
                #     pjxr14=FIGx1+40
                #     pjy14=FIGy1
                #     pjxl14=FIGx1-40
                #     pjxr24=FIGx2+40
                #     pjy24=FIGy2
                #     pjxl24=FIGx2-40
                #     lavacount=0
                #     pl1hc=0
                #     pl2hc=0
                #     boldx1=200
                #     boldy1=200
                #     boldx2=WIDTH-200
                #     boldy2=200
                #     boldy3=HEIGHT-200
                #     boldx3=200
                #     boldx4=WIDTH-200
                #     boldy4=HEIGHT-200
                #     flgcount=0
                #     score=0
                #     # my_timer.reset()
                #     # my_timer = Stopwatch()
                #     flgx= random.randint(50,WIDTH-50)
                #     flgx= random.randint(50, HEIGHT-50)
                #     P1x=FIGx1
                #     P2x=FIGx2
                #     P1y=FIGy1-75
                #     P2y=FIGy2-75
                #     create_NewgWindow('Level 2')
                #     # if HEIGHT==700:
                #     #     win.blit(sebg2,(0,0))
                #     # if HEIGHT==800:
                #     #     win.blit(eibg2(0,0))
                #     # if HEIGHT==900:
                #     #     win.blit(nibg2(0,0))
                #     # if HEIGHT==1000:
                #     #     win.blit(tebg2 (0,0))
                #     # win.blit(StR1,(FIGx1,FIGy1))
                #     # win.blit(StL2,(FIGx2, FIGy2)) 
                #     # win.blit(p1,(P1x,P1y))
                #     # win.blit(p2,(P2x,P2y))
                #     # pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
                #     # pygame.draw.rect(win,ORANGE,bolder2)     
                #     # pygame.draw.rect(win,ORANGE,bolder3)  
                #     # pygame.draw.rect(win,ORANGE,bolder4)
                #     while play:
                #         pygame.time.delay(100) #milliseconds 
                #         for anyThing in pygame.event.get(): #variable for anytrhing that happneds in py to listen to keyboard and mouse
                #             if anyThing.type ==pygame.QUIT: #says if Quit is typed something happends
                #                 run =False
                #         keyPressed= pygame.key.get_pressed()#records keyboard movement
                #         speedx=10
                #         speedy=10 
                #         P1y=FIGy1-75
                #         P2y=FIGy2-75
                #         if spped1==True:
                #             if keyPressed[pygame.K_RIGHT]:  
                #                 FIGx1 +=speedx 
                #                 right1=True
                #                 left1=False
                #                 lastr1=True
                #                 lastl1=False 
                #                 lastd1=False
                #                 lastw1=False
                #             if keyPressed[pygame.K_LEFT]:  
                #                 FIGx1 -=speedx 
                #                 right1=False
                #                 left1=True
                #                 lastr1=False
                #                 lastl1=True
                #                 lastd1=False
                #                 lastw1=False
                #             if keyPressed[pygame.K_UP]:  
                #                 FIGy1-=speedx
                #                 lastr1=False
                #                 lastl1=False
                #                 lastd1=False
                #                 lastw1=True
                #             if keyPressed [pygame.K_DOWN]:
                #                 FIGy1 +=speedx
                #                 lastr1=False
                #                 lastl1=False
                #                 lastd1=True
                #                 lastw1=False
                #             if FIGx1==10:
                #                 FIGx1=WIDTH-10
                #             if FIGx1==WIDTH-10:
                #                 FIGx1=10
                #             if FIGy1==10:
                #                 FIGy1=HEIGHT-10
                #             if FIGy1==HEIGHT-10:
                #                 FIGy1=10
                #             if keyPressed[pygame.K_f]:
                #                 if lastr1==True and p1pjcon>0:
                #                     if p1pjcon==4:
                #                         win.blit(proj11,(pjxr11,FIGy1))
                #                         p1pjcon-=1
                #                         pj11=True
                #                     if p1pjcon==3:
                #                         win.blit(proj12,(pjxr12,FIGy1))
                #                         p1pjcon-=1  
                #                         pj12=True   
                #                     # if p1pjcon==2:
                #                     #     win.blit(proj13,(pjxr13,FIGy1))
                #                     #     p1pjcon-=1
                #                     #     pj13=True 
                #                     # if p1pjcon==1:
                #                     #     win.blit(proj14,(pjxr14,FIGy1))
                #                     #     p1pjcon-=1
                #                     #     pj14=True 
                #                 if lastl1==True and p1pjcon>0:
                #                     if p1pjcon==4:
                #                         win.blit(proj11,(pjxl11,FIGy1))
                #                         p1pjcon-=1
                #                         pj11=True
                #                     if p1pjcon==3:
                #                         win.blit(proj12,(pjxl12,FIGy1))
                #                         p1pjcon-=1 
                #                         pj12=True    
                #                     if p1pjcon==4:
                #                         win.blit(proj11,(pjxl11,FIGy1))
                #                         p1pjcon-=1 
                #                         pj11=True
                #                     if p1pjcon==3:
                #                         win.blit(proj12,(pjxl12,FIGy1))
                #                         p1pjcon-=1 
                #                         pj12=True          
                #         if spped2==True:
                #             if keyPressed[pygame.K_d]:  
                #                 FIGx2 +=speedy 
                #                 righ2=True
                #                 left2=False
                #                 lastr2=True
                #                 lastl2=False
                #                 lastd2=False
                #                 lastw2=False 
                #             if keyPressed[pygame.K_a]:  
                #                 FIGx2-=speedy
                #                 right2=False
                #                 left2=True
                #                 lastr2=False
                #                 lastl2=True
                #                 lastd2=False
                #                 lastw2=False
                #             if keyPressed[pygame.K_w]:  
                #                 FIGy2-=speedy
                #                 lastr2=False
                #                 lastl2=False
                #                 lastd2=False
                #                 lastw2=True
                #             if keyPressed [pygame.K_s]:
                #                 FIGy2 +=speedy
                #                 lastr2=False
                #                 lastl2=False
                #                 lastd2=True
                #                 lastw2=False
                #             if FIGx2==10:
                #                 FIGx2=WIDTH-10
                #             if FIGx2==WIDTH-10:
                #                 FIGx2=10
                #             if FIGy2==10:
                #                 FIGy2=HEIGHT-10
                #             if FIGy2==HEIGHT-10:
                #                 FIGy2=10
                #         if keyPressed[pygame.K_SLASH]:
                #             if lastr2==True and p2pjcon>0:
                #                 if p2pjcon==4:
                #                     win.blit(proj21,(pjxr21,FIGy2))
                #                     p2pjcon-=1
                #                     pj21=True
                #                 if p2pjcon==3:
                #                     win.blit(proj22,(pjxr22,FIGy2))
                #                     p2pjcon-=1 
                #                     pj22=True    
                #                 # if p2pjcon==2:
                #                 #     win.blit(proj23,(pjxr23,FIGy2))
                #                 #     p2pjcon-=1 
                #                 #     pj23=True
                #                 # if p2pjcon==1:
                #                 #     win.blit(proj24,(pjxr24,FIGy2))
                #                 #     p2pjcon-=1 
                #                 #     pj24=True
                #             if lastl2==True and p2pjcon>0:
                #                 if p2pjcon==4:
                #                     win.blit(proj21,(pjxr21,FIGy2))
                #                     p2pjcon-=1
                #                     pj21=True
                #                 if p2pjcon==3:
                #                     win.blit(proj22,(pjxr22,FIGy2))
                #                     p2pjcon-=1 
                #                     pj22=True    
                #                 # if p2pjcon==2:
                #                 #     win.blit(proj23,(pjxr23,FIGy2))
                #                 #     p2pjcon-=1 
                #                 #     pj23=True
                #                 # if p2pjcon==1:
                #                 #     win.blit(proj24,(pjxr24,FIGy2))
                #                 #     p2pjcon-=1 
                #                 #     pj24=True   
                #         if pj11==True and projcount11>0 and lastl1==True:
                #             pjxl11+=20
                #             projcount11-=1
                #             if pjxl11 == boldx1+80 or pjxl11 ==boldx2+80 or pjxl11 ==boldx3+80 or pjxl11 ==boldx4+80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxl11=FIGx1-40
                #                 pjy11=FIGy1
                #             if pjy11 == boldy1+80 or pjy11 ==boldy2+80 or pjy11 ==boldy3+80 or pjy11 ==boldy4+80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxl11=FIGx1-40  
                #                 pjy11=FIGy1  
                #             if pjxl11 == boldx1-80 or pjxl11 ==boldx2-80 or pjxl11 == boldx3-80 or pjxl11 ==boldx4-80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxl11=FIGx1-40
                #                 pjy11=FIGy1
                #             if pjy11 == boldy1-80 or pjy11 ==boldy2-80 or pjy11 ==boldy3-80 or pjy11 ==boldy4-80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxl11=FIGx1-40  
                #                 pjy11=FIGy1 
                #             if pjxl11==10:
                #                 pjxl11=WIDTH-10
                #             if pjxl11==WIDTH-10:
                #                 pjxl11=10
                #             if pjy11==10:
                #                 pjy11=HEIGHT-10
                #             if pjy11==HEIGHT-10:
                #                 pjy11=10 
                #         elif pj11==False or projcount11<1:
                #             pj11=False
                #             projcount11=30
                #             pjxl11=FIGx1-40  
                #             pjy11=FIGy1 
                #         if pj12==True and projcount12>0 and lastl1==True:
                #             pjxl12+=20
                #             projcount12-=1
                #             if pjxl12 == boldx1+80 or pjxl12 ==boldx2+80 or pjxl12 ==boldx3+80 or pjxl12 ==boldx4+80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxl12=FIGx1-40
                #                 pjy12=FIGy1
                #             if pjy12 == boldy1+80 or pjy12 ==boldy2+80 or pjy12 ==boldy3+80 or pjy12 ==boldy4+80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxl12=FIGx1-40  
                #                 pjy12=FIGy1  
                #             if pjxl12 == boldx1-80 or pjxl12 ==boldx2-80 or pjxl12 ==boldx3-80 or pjxl12 ==boldx4-80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxl12=FIGx1-40
                #                 pjy12=FIGy1
                #             if pjy12 == boldy1-80 or pjy12 ==boldy2-80 or pjy12 ==boldy3-80 or pjy12 == boldy4-80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxl12=FIGx1-40  
                #                 pjy12=FIGy1 
                #             if pjxl12==10:
                #                 pjxl12=WIDTH-10
                #             if pjxl12==WIDTH-10:
                #                 pjxl12=10
                #             if pjy12==10:
                #                 pjy12=HEIGHT-10
                #             if pjy12==HEIGHT-10:
                #                 pjy12=10  
                #         elif pj12==False or projcount12<1:
                #             pj12=False
                #             projcount12=30
                #             pjxl12=FIGx1-40  
                #             pjy12=FIGy1
                #         # if pj13==True and projcount13>0 and lastl1==True:
                #         #     pjxl13+=20
                #         #     projcount13-=1
                #         #     if pjxl13 == boldx1+80 or pjxl13 ==boldx2+80 or pjxl13 ==boldx3+80 or pjxl13 ==boldx4+80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxl13=FIGx1-40
                #         #         pjy13=FIGy1
                #         #     if pjy13 == boldy1+80 or pjy13 ==boldy2+80 or pjy13 ==boldy3+80 or pjy13 ==boldy4+80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxl13=FIGx1-40  
                #         #         pjy13=FIGy1  
                #         #     if pjxl13 == boldx1-80 or pjxl13 ==boldx2-80 or pjxl13 ==boldx3-80 or pjxl13 ==boldx4-80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxl13=FIGx1-40
                #         #         pjy13=FIGy1
                #         #     if pjy13 == boldy1-80 or pjy13 ==boldy2-80 or pjy13 ==boldy3-80 or pjy13 ==boldy4-80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxl13=FIGx1-40  
                #         #         pjy13=FIGy1 
                #         #     if pjxl13==10:
                #         #         pjxl13=WIDTH-10
                #         #     if pjxl13==WIDTH-10:
                #         #         pjxl13=10
                #         #     if pjy13==10:
                #         #         pjy13=HEIGHT-10
                #         #     if pjy13==HEIGHT-10:
                #         #         pjy13=10 
                #         # elif pj13==False or projcount13<1:
                #         #     pj13=False
                #         #     projcount13=30
                #         #     pjxl13=FIGx1-40  
                #         #     pjy13=FIGy1
                #         # if pj14==True and projcount13>0 and lastl1==True:
                #         #     pjxl14+=20
                #         #     projcount14-=1
                #         #     if pjxl14 == boldx1+80 or pjxl14 ==boldx2+80 or pjxl14 ==boldx3+80 or pjxl14 ==boldx4+80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxl14=FIGx1-40
                #         #         pjy14=FIGy1
                #         #     if pjy14 == boldy1+80 or pjy14 ==boldy2+80 or pjy14 ==boldy3+80 or pjy14 ==boldy4+80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxl14=FIGx1-40  
                #         #         pjy14=FIGy1  
                #         #     if pjxl14 == boldx1-80 or pjxl14 ==boldx2-80 or pjxl14 ==boldx3-80 or pjxl14 ==boldx4-80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxl14=FIGx1-40
                #         #         pjy14=FIGy1
                #         #     if pjy14 == boldy1-80 or pjy14 ==boldy2-80 or pjy14 ==boldy3-80 or pjy14 ==boldy4-80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxl14=FIGx1-40  
                #         #         pjy14=FIGy1  
                #         #     if pjxl14==10:
                #         #         pjxl14=WIDTH-10
                #         #     if pjxl14==WIDTH-10:
                #         #         pjxl14=10
                #         #     if pjy14==10:
                #         #         pjy14=HEIGHT-10
                #         #     if pjy14==HEIGHT-10:
                #         #         pjy14=10 
                #         # elif pj14==False or projcount14<1:
                #         #     pj14=False
                #         #     projcount14=30
                #         #     pjxl14=FIGx1-40  
                #         #     pjy14=FIGy1
                #         if pj21==True and projcount21>0 and lastl2==True:
                #             pjxl21+=20
                #             projcount21-=1
                #             if pjxl21 == boldx1+80 or pjxl21 ==boldx2+80 or pjxl21 ==boldx3+80 or pjxl21 ==boldx4+80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxl21=FIGx2-40
                #                 pjy21=FIGy2
                #             if pjy21 == boldy1+80 or pjy21 ==boldy2+80 or pjy21 == boldy3+80 or pjy21 ==boldy4+80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxl21=FIGx2-40  
                #                 pjy21=FIGy2  
                #             if pjxl21 == boldx1-80 or pjxl21 ==boldx2-80 or pjxl21 ==boldx3-80 or pjxl21 ==boldx4-80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxl21=FIGx2-40
                #                 pjy21=FIGy2
                #             if pjy21 == boldy1-80 or pjy21 ==boldy2-80 or pjy21 ==boldy3-80 or pjy21 ==boldy4-80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxl21=FIGx2-40  
                #                 pjy21=FIGy2 
                #             if pjxl21==10:
                #                 pjxl21=WIDTH-10
                #             if pjxl21==WIDTH-10:
                #                 pjxl21=10
                #             if pjy21==10:
                #                 pjy21=HEIGHT-10
                #             if pjy21==HEIGHT-10:
                #                 pjy21=10  
                #         elif pj21==False or projcount21<1:
                #             pj21=False
                #             projcount21=30
                #             pjxl21=FIGx2-40  
                #             pjy21=FIGy2 
                #         if pj22==True and projcount22>0 and lastl2==True:
                #             pjxl22+=20
                #             projcount22-=1
                #             if pjxl22 == boldx1+80 or pjxl22 ==boldx2+80 or pjxl22 ==boldx3+80 or pjxl22 ==boldx4+80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxl22=FIGx2-40
                #                 pjy22=FIGy2
                #             if pjy22 == boldy1+80 or pjy22 == boldy2+80 or pjy22 == boldy3+80 or pjy22 == boldy4+80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxl22=FIGx2-40  
                #                 pjy22=FIGy2  
                #             if pjxl22 == boldx1-80 or pjxl22 == boldx2-80 or pjxl22 == boldx3-80 or pjxl22 == boldx4-80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxl22=FIGx2-40
                #                 pjy22=FIGy2
                #             if pjy22 == boldy1-80 or pjy22 == boldy2-80 or pjy22 == boldy3-80 or pjy22 == boldy4-80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxl22=FIGx2-40  
                #                 pjy22=FIGy2  
                #             if pjxl22==10:
                #                 pjxl22=WIDTH-10
                #             if pjxl22==WIDTH-10:
                #                 pjxl22=10
                #             if pjy22==10:
                #                 pjy22=HEIGHT-10
                #             if pjy22==HEIGHT-10:
                #                 pjy22=10
                #         elif pj22==False or projcount22<1:
                #             pj22=False
                #             projcount22=30
                #             pjxl22=FIGx2-40  
                #             pjy22=FIGy2 
                #         # if pj23==True and projcount23>0 and lastl2==True:
                #         #     pjxl23+=20
                #         #     projcount23-=1
                #         #     if pjxl23 == boldx1+80 or pjxl23 == boldx2+80 or pjxl23 == boldx3+80 or pjxl23 == boldx4+80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxl23=FIGx2-40
                #         #         pjy23=FIGy2
                #         #     if pjy23 == boldy1+80 or pjy23 == boldy2+80 or pjy23 == boldy3+80 or pjy23 == boldy4+80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxl23=FIGx2-40  
                #         #         pjy23=FIGy2  
                #         #     if pjxl23 == boldx1-80 or pjxl23 == boldx2-80 or pjxl23 == boldx3-80 or pjxl23 == boldx4-80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxl23=FIGx2-40
                #         #         pjy23=FIGy2
                #         #     if pjy23 == boldy1-80 or pjy23 == boldy2-80 or pjy23 == boldy3-80 or pjy23 == boldy4-80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxl23=FIGx2-40  
                #         #         pjy23=FIGy2  
                #         #     if pjxl23==10:
                #         #         pjxl23=WIDTH-10
                #         #     if pjxl23==WIDTH-10:
                #         #         pjxl23=10
                #         #     if pjy23==10:
                #         #         pjy23=HEIGHT-10
                #         #     if pjy23==HEIGHT-10:
                #         #         pjy23=10
                #         # elif pj23==False or projcount23<1:
                #         #     pj23=False
                #         #     projcount23=30
                #         #     pjxl23=FIGx2-40  
                #         #     pjy23=FIGy2 
                #         # if pj24==True and projcount24>0 and lastl2==True:
                #         #     pjxl24+=20
                #         #     projcount24-=1
                #         #     if pjxl24 == boldx1+80 or pjxl24 == boldx2+80 or pjxl24 == boldx3+80 or pjxl24 == boldx4+80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxl24=FIGx2-40
                #         #         pjy24=FIGy2
                #         #     if pjy24 == boldy1+80 or pjy24 == boldy2+80 or pjy24 == boldy3+80 or pjy24 == boldy4+80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxl24=FIGx2-40  
                #         #         pjy24=FIGy2  
                #         #     if pjxl24 == boldx1-80 or pjxl24 == boldx2-80 or pjxl24 == boldx3-80 or pjxl24 == boldx4-80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxl24=FIGx2-40
                #         #         pjy24=FIGy2
                #         #     if pjy24 == boldy1-80 or pjy24 == boldy2-80 or pjy24 == boldy3-80 or pjy24 == boldy4-80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxl24=FIGx2-40  
                #         #         pjy24=FIGy2  
                #         #     if pjxl24==10:
                #         #         pjxl24=WIDTH-10
                #         #     if pjxl24==WIDTH-10:
                #         #         pjxl24=10
                #         #     if pjy24==10:
                #         #         pjy24=HEIGHT-10
                #         #     if pjy24==HEIGHT-10:
                #         #         pjy24=10
                #         # elif pj24==False or projcount24<1:
                #         #     pj24=False
                #         #     projcount24=30
                #         #     pjxl24=FIGx2-40  
                #         #     pjy24=FIGy2 
                #         if pj11==True and projcount11>0 and lastr1==True:
                #             pjxr11+=20
                #             projcount11-=1
                #             if pjxr11 == boldx1+80 or pjxr11 == boldx2+80 or pjxr11 == boldx3+80 or pjxr11 == boldx4+80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxr11=FIGx1+40
                #                 pjy11=FIGy1
                #             if pjy11 == boldy1+80 or pjy11 == boldy2+80 or pjy11 == boldy3+80 or pjy11 == boldy4+80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxr11=FIGx1+40  
                #                 pjy11=FIGy1  
                #             if pjxr11 == boldx1-80 or pjxr11 == boldx2-80 or pjxr11 == boldx3-80 or pjxr11 == boldx4-80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxr11=FIGx1+40
                #                 pjy11=FIGy1
                #             if pjy11 == boldy1-80 or pjy11 == boldy2-80 or pjy11 == boldy3-80 or pjy11 == boldy4-80:
                #                 pj11=False
                #                 projcount11=30
                #                 pjxr11=FIGx1+40  
                #                 pjy11=FIGy1  
                #             if pjxr11==10:
                #                 pjxr11=WIDTH-10
                #             if pjxr11==WIDTH-10:
                #                 pjxr11=10
                #             if pjy11==10:
                #                 pjy11=HEIGHT-10
                #             if pjy11==HEIGHT-10:
                #                 pjy11=10
                #         elif pj11==False or projcount11<1:
                #             pj11=False
                #             projcount11=30
                #             pjxr11=FIGx1+40  
                #             pjy11=FIGy1 
                #         if pj12==True and projcount12>0 and lastr1==True:
                #             pjxr12+=20
                #             projcount12-=1
                #             if pjxr12 == boldx1+80 or pjxr12 == boldx2+80 or pjxr12 == boldx3+80 or pjxr12 == boldx4+80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxr12=FIGx1+40
                #                 pjy12=FIGy1
                #             if pjy12 == boldy1+80 or pjy12 == boldy2+80 or pjy12 == boldy3+80 or pjy12 == boldy4+80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxr12=FIGx1+40  
                #                 pjy12=FIGy1  
                #             if pjxr12 == boldx1-80 or pjxr12 == boldx2-80 or pjxr12 == boldx3-80 or pjxr12 == boldx4-80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxr12=FIGx1+40
                #                 pjy12=FIGy1
                #             if pjy12 == boldy1-80 or pjy12 == boldy2-80 or pjy12 == boldy3-80 or pjy12 == boldy4-80:
                #                 pj12=False
                #                 projcount12=30
                #                 pjxr12=FIGx1+40  
                #                 pjy12=FIGy1  
                #             if pjxr12==10:
                #                 pjxr12=WIDTH-10
                #             if pjxr12==WIDTH-10:
                #                 pjxr12=10
                #             if pjy12==10:
                #                 pjy12=HEIGHT-10
                #             if pjy12==HEIGHT-10:
                #                 pjy12=10
                #         elif pj12==False or projcount12<1:
                #             pj12=False
                #             projcount12=30
                #             pjxr12=FIGx1+40  
                #             pjy12=FIGy1
                #         # if pj13==True and projcount13>0 and lastr1==True:
                #         #     pjxr13+=20
                #         #     projcount13-=1
                #         #     if pjxr13 == boldx1+80 or pjxr13 == boldx2+80 or pjxr13 == boldx3+80 or pjxr13 == boldx4+80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxr13=FIGx1+40
                #         #         pjy13=FIGy1
                #         #     if pjy13 == boldy1+80 or pjy13 == boldy2+80 or pjy13 == boldy3+80 or pjy13 == boldy4+80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxr13=FIGx1-40  
                #         #         pjy13=FIGy1  
                #         #     if pjxr13 == boldx1-80 or pjxr13 == boldx2-80 or pjxr13 == boldx3-80 or pjxr13 == boldx4-80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxr13=FIGx1-40
                #         #         pjy13=FIGy1
                #         #     if pjy13 == boldy1-80 or pjy13 == boldy2-80 or pjy13 == boldy3-80 or pjy13 == boldy4-80:
                #         #         pj13=False
                #         #         projcount13=30
                #         #         pjxr13=FIGx1-40  
                #         #         pjy13=FIGy1 
                #         #     if pjxr13==10:
                #         #         pjxr13=WIDTH-10
                #         #     if pjxr13==WIDTH-10:
                #         #         pjxr13=10
                #         #     if pjy13==10:
                #         #         pjy13=HEIGHT-10
                #         #     if pjy13==HEIGHT-10:
                #         #         pjy13=10
                #         # elif pj13==False or projcount13<1:
                #         #     pj13=False
                #         #     projcount13=30
                #         #     pjxr13=FIGx1-40  
                #         #     pjy13=FIGy1
                #         # if pj14==True and projcount13>0 and lastr1==True:
                #         #     pjxr14+=20
                #         #     projcount14-=1
                #         #     if pjxr14 == boldx1+80 or pjxr14 == boldx2+80 or pjxr14 == boldx3+80 or bpjxr14 == oldx4+80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxr14=FIGx1+40
                #         #         pjy14=FIGy1
                #         #     if pjy14 == boldy1+80 or pjy14 == boldy2+80 or pjy14 == boldy3+80 or pjy14 == boldy4+80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxr14=FIGx1+40  
                #         #         pjy14=FIGy1  
                #         #     if pjxr14 == boldx1-80 or pjxr14 == boldx2-80 or pjxr14 ==  boldx3-80 or pjxr14 == boldx4-80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxr14=FIGx1+40
                #         #         pjy14=FIGy1
                #         #     if pjy14 == boldy1-80 or pjy14 == boldy2-80 or pjy14 == boldy3-80 or pjy14 == boldy4-80:
                #         #         pj14=False
                #         #         projcount14=30
                #         #         pjxr14=FIGx1+40  
                #         #         pjy14=FIGy1
                #         #     if pjxr14==10:
                #         #         pjxr14=WIDTH-10
                #         #     if pjxr14==WIDTH-10:
                #         #         pjxr14=10
                #         #     if pjy14==10:
                #         #         pjy14=HEIGHT-10
                #         #     if pjy14==HEIGHT-10:
                #         #         pjy14=10  
                #         # elif pj14==False or projcount14<1:
                #         #     pj14=False
                #         #     projcount14=30
                #         #     pjxr14=FIGx1+40  
                #         #     pjy14=FIGy1
                #         if pj21==True and projcount21>0 and lastr2==True:
                #             pjxr21+=20
                #             projcount21-=1
                #             if pjxr21 == boldx1+80 or pjxr21 == boldx2+80 or pjxr21 == boldx3+80 or pjxr21 == boldx4+80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxr21=FIGx2+40
                #                 pjy21=FIGy2
                #             if pjy21 == boldy1+80 or pjy21 == boldy2+80 or pjy21 == boldy3+80 or pjy21 == boldy4+80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxr21=FIGx2+40  
                #                 pjy21=FIGy2  
                #             if pjxr21 == boldx1-80 or pjxr21 == boldx2-80 or pjxr21 == boldx3-80 or pjxr21 == boldx4-80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxr21=FIGx2+40
                #                 pjy21=FIGy2
                #             if pjy21 == boldy1-80 or pjy21 == boldy2-80 or pjy21 == boldy3-80 or pjy21 == boldy4-80:
                #                 pj21=False
                #                 projcount21=30
                #                 pjxr21=FIGx2+40  
                #                 pjy21=FIGy2  
                #             if pjxr21==10:
                #                 pjxr21=WIDTH-10
                #             if pjxr21==WIDTH-10:
                #                 pjxr21=10
                #             if pjy21==10:
                #                 pjy21=HEIGHT-10
                #             if pjy21==HEIGHT-10:
                #                 pjy21=10
                #         elif pj21==False or projcount21<1:
                #             pj21=False
                #             projcount21=30
                #             pjxr21=FIGx2-40  
                #             pjy21=FIGy2 
                #         if pj22==True and projcount22>0 and lastr2==True:
                #             pjxr22+=20
                #             projcount22-=1
                #             if pjxr22 == boldx1+80 or pjxr22 == boldx2+80 or pjxr22 == boldx3+80 or pjxr22 == boldx4+80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxr22=FIGx2+40
                #                 pjy22=FIGy2
                #             if pjy22 == boldy1+80 or pjy22 == boldy2+80 or pjy22 == boldy3+80 or pjy22 == boldy4+80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxr22=FIGx2+40  
                #                 pjy22=FIGy2  
                #             if pjxr22 == boldx1-80 or pjxr22 == boldx2-80 or pjxr22 == boldx3-80 or pjxr22 == boldx4-80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxr22=FIGx2+40
                #                 pjy22=FIGy2
                #             if pjy22 == boldy1-80 or pjy22 == boldy2-80 or pjy22 == boldy3-80 or pjy22 == boldy4-80:
                #                 pj22=False
                #                 projcount22=30
                #                 pjxr22=FIGx2+40  
                #                 pjy22=FIGy2  
                #             if pjxr22==10:
                #                 pjxr22=WIDTH-10
                #             if pjxr22==WIDTH-10:
                #                 pjxr22=10
                #             if pjy22==10:
                #                 pjy22=HEIGHT-10
                #             if pjy22==HEIGHT-10:
                #                 pjy22=10
                #         elif pj22==False or projcount22<1:
                #             pj22=False
                #             projcount22=30
                #             pjxr22=FIGx2+40  
                #             pjy22=FIGy2 
                #         # if pj23==True and projcount23>0 and lastr2==True:
                #         #     pjxr23+=20
                #         #     projcount23-=1
                #         #     if pjxr23 == boldx1+80 or pjxr23 == boldx2+80 or pjxr23 == boldx3+80 or pjxr23 == boldx4+80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxr23=FIGx2+40
                #         #         pjy23=FIGy2
                #         #     if pjy23 == boldy1+80 or pjy23 == boldy2+80 or pjy23 == boldy3+80 or pjy23 == boldy4+80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxr23=FIGx2+40  
                #         #         pjy23=FIGy2  
                #         #     if pjxr23 == boldx1-80 or pjxr23 == boldx2-80 or pjxr23 == boldx3-80 or pjxr23 == boldx4-80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxr23=FIGx2+40
                #         #         pjy23=FIGy2
                #         #     if pjy23 == boldy1-80 or pjy23 == boldy2-80 or pjy23 == boldy3-80 or pjy23 == boldy4-80:
                #         #         pj23=False
                #         #         projcount23=30
                #         #         pjxr23=FIGx2+40  
                #         #         pjy23=FIGy2 
                #         #     if pjxr23==10:
                #         #         pjxr23=WIDTH-10
                #         #     if pjxr23==WIDTH-10:
                #         #         pjxr23=10
                #         #     if pjy23==10:
                #         #         pjy23=HEIGHT-10
                #         #     if pjy23==HEIGHT-10:
                #         #         pjy23=10 
                #         # elif pj23==False or projcount23<1:
                #         #     pj23=False
                #         #     projcount23=30
                #         #     pjxr23=FIGx2+40  
                #         #     pjy23=FIGy2 
                #         # if pj24==True and projcount24>0 and lastr2==True:
                #         #     pjxr24+=20
                #         #     projcount24-=1
                #         #     if pjxr24 == boldx1+80 or pjxr24 == boldx2+80 or pjxr24 == boldx3+80 or pjxr24 == boldx4+80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxr24=FIGx2+40
                #         #         pjy24=FIGy2
                #         #     if pjy24 == boldy1+80 or pjy24 == boldy2+80 or pjy24 == boldy3+80 or pjy24 == boldy4+80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxr24=FIGx2+40  
                #         #         pjy24=FIGy2  
                #         #     if pjxr24 == boldx1-80 or pjxr24 == boldx2-80 or pjxr24 == boldx3-80 or pjxr24 == boldx4-80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxr24=FIGx2+40
                #         #         pjy24=FIGy2
                #         #     if pjy24 == boldy1-80 or pjy24 == boldy2-80 or pjy24 == boldy3-80 or pjy24 == boldy4-80:
                #         #         pj24=False
                #         #         projcount24=30
                #         #         pjxr24=FIGx2+40  
                #         #         pjy24=FIGy2 
                #         #     if pjxr24==10:
                #         #         pjxr24=WIDTH-10
                #         #     if pjxr24==WIDTH-10:
                #         #         pjxr24=10
                #         #     if pjy24==10:
                #         #         pjy24=HEIGHT-10
                #         #     if pjy24==HEIGHT-10:
                #         #         pjy24=10 
                #         # elif pj24==False or projcount24<1:
                #         #     pj24=False
                #         #     projcount24=30
                #         #     pjxr24=FIGx2+40  
                #         #     pjy24=FIGy2      
                #         if pjxr11==FIGx1 or pjxr12==FIGx1 or pjxr21==FIGx1 or pjxr22==FIGx1 or pjxl11==FIGx1 or pjxl12==FIGx1 or pjxl21==FIGx1 or pjxl22==FIGx1 or pjy11==FIGy1 or pjy12==FIGy1 or pjy21==FIGy1 or pjy22==FIGy1:
                #             spped1=False
                #             pl1hc+=1
                #             pygame.time.delay(5000)
                #             spped1=True
                #         if pjxr11==FIGx2 or pjxr12==FIGx2 or pjxr21==FIGx2 or pjxr22==FIGx2 or pjxl11==FIGx2 or pjxl12==FIGx2 or pjxl21==FIGx2 or pjxl22==FIGx2 or pjy11==FIGy2 or pjy12==FIGy2 or pjy21==FIGy2 or pjy22==FIGy2:
                #             spped2=False
                #             pl2hc+=1
                #             pygame.time.delay(5000)
                #             spped2=True  
                #         if FIGx1==boldx1+85 or FIGx1==boldx2+85 or FIGx1==boldx3+85 or FIGx1==boldx4+85:
                #             spped1=False
                #             FIGx1+=50
                #             pygame.time.delay(3000)
                #             spped1=True
                #         if FIGx1==boldx1-85 or FIGx1==boldx2-85 or FIGx1==boldx3-85 or FIGx1==boldx4-85:
                #             spped1=False
                #             FIGx1+=50
                #             pygame.time.delay(3000)
                #             spped1=True
                #         if FIGy1==boldy1+85 or FIGy1==boldy2+85 or FIGy1==boldy3+85 or FIGy1==boldy4+85: 
                #             spped1=False
                #             FIGy1+=50
                #             pygame.time.delay(3000)
                #             spped1=True
                #         if FIGy1==boldy1-85 or FIGy1==boldy2-85 or FIGy1==boldy3-85 or FIGy1==boldy4-85:
                #             spped1=False
                #             FIGy1-=50
                #             pygame.time.delay(3000)
                #             spped1=True
                #         if FIGx2==boldx1+85 or FIGx2==boldx2+85 or FIGx2==boldx3+85 or FIGx2==boldx4+85:
                #             spped2=False
                #             FIGx2+=50
                #             pygame.time.delay(3000)
                #             spped2=True
                #         if FIGx2==boldx1-85 or FIGx2==boldx2-85 or FIGx2==boldx3-85 or FIGx2==boldx4-85:
                #             spped2=False
                #             FIGx2-=50
                #             pygame.time.delay(3000)
                #             spped2=True
                #         if FIGy2==boldy1+85 or FIGy2== boldy2+85 or FIGy2==boldy3+85 or FIGy2==boldy4+85:
                #             spped2=False
                #             FIGy2-=50
                #             pygame.time.delay(3000)
                #             spped2=True
                #         if FIGy2==boldy1-85 or FIGy2==boldy2-85 or FIGy2==boldy3-85 or FIGy2==boldy4-85:
                #             spped2=False
                #             FIGy2-=50
                #             pygame.time.delay(3000)
                #             spped2=True
                #         if pl2hc==5:
                #             play=False
                #             # scorepen=my_timer.get_seconds()
                #             score=pl2hc*2000-(pl1hc*200)
                #             end=True
                #         if pl1hc==5:
                #             play=False
                #             # scorepen=my_timer.get_seconds()
                #             score=pl1hc*2000-(pl2hc*200)
                #             end=True
                #         redrawGameWindowforp1()
                #         lavspawn()
                #         # if HEIGHT==700:
                #         #     win.blit(sebg,(0,0))
                #         # if HEIGHT==800:
                #         #     win.blit(eibg,(0,0))
                #         # if HEIGHT==900:
                #         #     win.blit(nibg,(0,0))
                #         # if HEIGHT==1000:#bases type of background needed on height
                #         #     win.blit(tebg,(0,0))
                #         pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
                #         pygame.draw.rect(win,ORANGE,bolder2)     
                #         pygame.draw.rect(win,ORANGE,bolder3)  
                #         pygame.draw.rect(win,ORANGE,bolder4)
                #         pygame.display.update()
                #         pygame.display.flip()
                # if end==True:
                #     create_NewWindow("Good Game")
                #     win.fill(WHITE)
                #     display_Title("Good Game",40)
                #     Menu_function(EndMessages,150)
                #     pygame.time.delay(100)
                #     score+=1000
                #     counter+=1
                #     if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 8:
                #         newgame1=True
                #         newgame2=False
                #         escape2=False
                #         counter-=1
                #     if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 8:
                #         newgame1=False
                #         newgame2=True
                #         escape2=False
                #         counter-=1
                #     if xp>x and xp<x+wbox and yp>y and yp<445 and yp>545 and counter is 8:
                #         newgame1=False 
                #         newgame2=False
                #         escape2=False
                #         display_Title("TestyGame",y)
                #         Menu_function(gameMessages,150)
                #         counter -=8
                # if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 7:
                #     xp=0
                #     yp=0 
                #     win.fill(WHITE)
                #     display_Title("Testy Game",y)
                #     Menu_function(gameMessages,150)
                #     counter-=7 