import pygame
import time
import random
pygame.init()

# Setting up Game Window
disp_x=1080
disp_y=500
color=(0,255,255)
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,0)
gamedisplay=pygame.display.set_mode((disp_x,disp_y))
pygame.display.set_caption("MARTIAN")
icon_img=pygame.image.load("icon.png")
pygame.display.set_icon(icon_img)
music_sound=pygame.mixer.Sound("music.wav")
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1)
clock=pygame.time.Clock()
# Game Window set up

# First game interface
def firstUI(x,y):
   gamedisplay.blit(firstUI_img,(x,y))
def drawrectangle(i):
   pygame.draw.rect(gamedisplay,green,pygame.Rect(135,420,11+5*i,5))
   time.sleep(0.5)
   pygame.display.update()
firstUI_img=pygame.image.load("1 UI.jpg")
firstUI(0,0)
pygame.display.update()
font=pygame.font.SysFont("Tahoma",25)
text=font.render("LOADING...",True,red)
gamedisplay.blit(text,(135,380))
pygame.display.update()
i=0
while(i<=25):
   drawrectangle(i)
   i+=1.5
time.sleep(1)
# End of first game interface

# Rules interface
def rulesUI(x,y):
   gamedisplay.blit(rules_img,(x,y))
rules_img=pygame.image.load("rules.png")
rulesUI(0,0)
pygame.display.update()
time.sleep(4)
# End of rules interface
   
# Controls game interface
def controlsUI(x,y):
   gamedisplay.blit(controls_img,(x,y))
controls_img=pygame.image.load("controls.jpg")
controlsUI(50,0)
pygame.display.update()
time.sleep(2)
# End of control game interface

# Load images for game
spaceship_img=pygame.image.load("spaceship.png")
space_img=pygame.image.load("Space.jpg")
comet_img=pygame.image.load("comet.png")
comet_imgrig=pygame.image.load("comet2.png")
solarflare_img=pygame.image.load("solarflare.png")
asteroid1_img=pygame.image.load("asteroid1.png")
probe_img=pygame.image.load("probe.png")
star_img=pygame.image.load("star.png")
# Images loaded in background

# Movie for game
t_img=pygame.image.load("2.jpg")
gamedisplay.blit(t_img,(0,0))
pygame.display.update()
time.sleep(1.5)
th_img=pygame.image.load("3.jpg")
gamedisplay.blit(th_img,(0,0))
pygame.display.update()
time.sleep(2)
s_img=pygame.image.load("6.jpg")
gamedisplay.blit(s_img,(0,0))
pygame.display.update()
time.sleep(1.5)
se_img=pygame.image.load("7.jpg")
gamedisplay.blit(se_img,(0,0))
pygame.display.update()
time.sleep(2)
# Movie Complete

# Functions for Displaying Images
def spaceship(x,y):
    gamedisplay.blit(spaceship_img,(x,y))
def space(x,y):
    gamedisplay.blit(space_img,(x,y))
def comet(x,y):
    gamedisplay.blit(comet_img,(x,y))
def cometrig(x,y):
    gamedisplay.blit(comet_imgrig,(x,y))
def solarflare(x,y):
    gamedisplay.blit(solarflare_img,(x,y))
def asteroid1(x,y):
    gamedisplay.blit(asteroid1_img,(x,y))
def probe(x,y):
    gamedisplay.blit(probe_img,(x,y))
def star(x,y):
    gamedisplay.blit(star_img,(x,y))
# Functions Ended

# Setting Initial Values for Game Variables
x=(disp_x*0.45)
y=(disp_y*0.65)
xc=0
yc=0
sx=0
sy=0
ycom=-100
ycomr=-100
ysolarflare=-150
xcom=random.randrange(-250,250)
xcomr=random.randrange(750,1500)
xsolarflare=random.randrange(-200,1080)
xastds=random.randrange(-200,1080)
xprobe=1080
yprobe=random.randrange(-250,750)
if(xastds<0):
   xastds=5
if(xsolarflare<0):
   xsolarflare=5
if(xcom<0):
   xcom=-10
if(xcom>1500):
   xcom=1080
yastds=-200
xstar=random.randrange(10,1000)
ystar=random.randrange(10,500)
timevar=0
level=1
speed=0
flag=0
crashed=False
def funtime(timevar,level):
   time=int(timevar)
   levelvar=int(level)
   font=pygame.font.SysFont("Tahoma",25)
   text=font.render("SURVIVAL :: "+str(time),True,color)
   gamedisplay.blit(text,(0,0))
   pygame.display.update()
   text=font.render("LIGHT-Yrs :: "+str(levelvar),True,green)
   gamedisplay.blit(text,(0,28))
   pygame.display.update()
# Initialisation Completed

# GAME BODY
while not crashed:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
                xc=-5       
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
                xc=5
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
                yc=-5
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
                yc=+5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                xc=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                yc=0
    x+=xc
    y+=yc
    speed=level*0.5
    xcom+=3.5+speed
    xcomr-=3+speed
    ycomr+=2+speed
    ycom+=2+speed
    yastds+=4.5+speed
    xprobe-=(4+speed)
    ysolarflare+=3+speed
    timevar+=0.04
    level=timevar//8 + 1
    funtime(timevar,level)
    if x<=0:
        x=0
    if x>=980:
        x=980
    if y<=0:
        y=0
    if y>=365:
        y=365
    if(sy==150):
       sy=0
    space(sx,sy)
    count=0
    while(count<=15):
       xstar=random.randint(10,1000)
       ystar=random.randint(10,500)
       star(xstar,ystar)
       count+=4
    comet(xcom,ycom)
    cometrig(xcomr,ycomr)
    solarflare(xsolarflare,ysolarflare)
    asteroid1(xastds,yastds)
    probe(xprobe,yprobe)
    spaceship(x,y)
    if(ycom>490):
       ycom=-10
       xcom=random.randrange(-100,250)
    if(ycomr>490):
       ycomr=-10
       xcomr=random.randrange(750,1100)
    if(yastds>450):
       yastds=-200
       xastds=random.randrange(-200,1000)
       if(xastds<0):
         xastds=5
    if(ysolarflare>450):
       ysolarflare=-150
       xsolarflare=random.randrange(-200,1000)
       if(xsolarflare<0):
         xsolarflare=5     
    if(xcomr<50):
       xcomr=850
    if(xprobe<=0):
       xprobe=1080
       yprobe=random.randrange(-250,750) 
           
    # Planet BLue Crashed
    if(50<x+26 and x+26<107):
       if(190<y+21 and y+21<245):
          flag=0
          crashed=True
    if(50<x+66 and x+66<107):
       if(190<y+41 and y+41<245):
          flag=1
          crashed=True
    if(50<x+77 and x+77<107):
       if(190<y+121 and y+121<245):
          flag=2
          crashed=True
    if(50<x+4 and x+4<107):
       if(190<y+121 and y+121<245):
          flag=3
          crashed=True
    if(50<x+42 and x+42<107):
       if(190<y+166 and y+166<245):
          flag=4
          crashed=True
   # End Planet BLue crashed

   # Planet Saturn Crashed
    if(850<x+26 and x+26<995):
       if(10<y+21 and y+21<190):
          flag=0
          crashed=True
    if(850<x+66 and x+66<995):
       if(10<y+41 and y+41<190):
          flag=1
          crashed=True
    if(850<x+77 and x+77<995):
       if(10<y+121 and y+121<190):
          flag=2
          crashed=True
    if(850<x+4 and x+4<995):
       if(10<y+121 and y+121<190):
          flag=3
          crashed=True
    if(850<x+42 and x+42<995):
       if(10<y+166 and y+166<190):
          flag=4
          crashed=True
   # End Planet Saturn crashed

   # Asteroid Crashed
    if(xastds<x+26 and x+26<xastds+55):
       if(yastds+15<y+21 and y+21<yastds+50):
          flag=0
          crashed=True
    if(xastds<x+66 and x+66<xastds+55):
       if(yastds+15<y+41 and y+41<yastds+50):
          flag=1
          crashed=True
    if(xastds<x+77 and x+77<xastds+55):
       if(yastds+15<y+121 and y+121<yastds+50):
          flag=2
          crashed=True
    if(xastds<x+4 and x+4<xastds+55):
       if(yastds+15<y+121 and y+121<yastds+50):
          flag=3
          crashed=True
    if(xastds<x+42 and x+42<xastds+55):
       if(yastds+15<y+166 and y+166<yastds+50):
          flag=4
          crashed=True
   # End Asteroid crashed

   # Solar Flare Crashed
    if(xsolarflare+6<x+26 and x+26<xsolarflare+34):
       if(ysolarflare+27<y+21 and y+21<ysolarflare+65):
          flag=0
          crashed=True
    if(xsolarflare+6<x+66 and x+66<xsolarflare+34):
       if(ysolarflare+27<y+41 and y+41<ysolarflare+65):
          flag=1
          crashed=True
    if(xsolarflare+6<x+77 and x+77<xsolarflare+34):
       if(ysolarflare+27<y+121 and y+121<ysolarflare+65):
          flag=2
          crashed=True
    if(xsolarflare+6<x+4 and x+4<xsolarflare+34):
       if(ysolarflare+27<y+121 and y+121<ysolarflare+65):
          flag=3
          crashed=True
    if(xsolarflare+6<x+42 and x+42<xsolarflare+34):
       if(ysolarflare+27<y+166 and y+166<ysolarflare+65):
          flag=4
          crashed=True
    if(xsolarflare<x+45 and x+45<xsolarflare+40):
       if(ysolarflare+40<y+85 and y+85<ysolarflare+75):
          flag=5
          crashed=True
   # End of SolarFlare
       
   # Comet left Crashed
    if(xcom+35<x+26 and x+26<xcom+75):
       if(ycom+35<y+21 and y+21<ycom+65):
          flag=0
          crashed=True
    if(xcom+35<x+66 and x+66<xcom+75):
       if(ycom+35<y+41 and y+41<ycom+65):
          flag=1
          crashed=True
    if(xcom+35<x+77 and x+77<xcom+75):
       if(ycom+35<y+121 and y+121<ycom+65):
          flag=2
          crashed=True
    if(xcom+35<x+4 and x+4<xcom+75):
       if(ycom+35<y+121 and y+121<ycom+65):
          flag=3
          crashed=True
    if(xcom+35<x+42 and x+42<xcom+75):
       if(ycom+35<y+166 and y+166<ycom+65):
          flag=4
          crashed=True
    if(xcom+35<x+45 and x+45<xcom+75):
       if(ycom+35<y+85 and y+85<ycom+65):
          flag=5
          crashed=True
   # End of Comet left
          
   # Comet Right Crashed
    if(xcomr+10<x+26 and x+26<xcomr+40):
       if(ycomr+40<y+21 and y+21<ycomr+75):
          flag=0
          crashed=True
    if(xcomr+10<x+66 and x+66<xcomr+40):
       if(ycomr+40<y+41 and y+41<ycomr+75):
          flag=1
          crashed=True
    if(xcomr+10<x+77 and x+77<xcomr+40):
       if(ycomr+40<y+121 and y+121<ycomr+75):
          flag=2
          crashed=True
    if(xcomr+10<x+4 and x+4<xcomr+40):
       if(ycomr+40<y+121 and y+121<ycomr+75):
          flag=3
          crashed=True
    if(xcomr+10<x+42 and x+42<xcomr+40):
       if(ycomr+40<y+166 and y+166<ycomr+75):
          flag=4
          crashed=True
    if(xcomr+10<x+45 and x+45<xcomr+40):
       if(ycomr+40<y+85 and y+85<ycomr+75):
          flag=5
          crashed=True
   # End of Comet Right

   # Probe Crashed
    if(xprobe<x+26 and x+26<xprobe+55):
       if(yprobe+15<y+21 and y+21<yprobe+50):
          flag=0
          crashed=True
    if(xprobe<x+66 and x+66<xprobe+55):
       if(yprobe+15<y+41 and y+41<yprobe+50):
          flag=1
          crashed=True
    if(xprobe<x+77 and x+77<xprobe+55):
       if(yprobe+15<y+121 and y+121<yprobe+50):
          flag=2
          crashed=True
    if(xprobe<x+4 and x+4<xprobe+55):
       if(yprobe+15<y+121 and y+121<yprobe+50):
          flag=3
          crashed=True
    if(xprobe<x+42 and x+42<xprobe+55):
       if(yprobe+15<y+166 and y+166<yprobe+50):
          flag=4
          crashed=True
    if(xprobe<x+45 and x+45<xprobe+55):
       if(yprobe+15<y+85 and y+85<yprobe+50):
          flag=5
          crashed=True
   # End Probe crashed

    pygame.display.update()
    clock.tick(40)
# GAME BODY END

# Explode SpaceShip
def explodeUI(x,y):
   gamedisplay.blit(explode_img,(x,y))
explode_img=pygame.image.load("explode.png")
music_s=pygame.mixer.Sound("boom.wav")
pygame.mixer.music.load("boom.wav")
pygame.mixer.music.play(2)
if (flag==0):
   explodeUI(x+26-33,y+21-28)
elif (flag==1):
   explodeUI(x+66-33,y+41-28)
elif (flag==2):
   explodeUI(x+77-33,y+121-28)
elif (flag==3):
   explodeUI(x+4-33,y+121-28)
elif (flag==4):
   explodeUI(x+42-33,y+166-28)
elif (flag==5):
   explodeUI(x+45-33,y+85-28)
pygame.display.update()
time.sleep(3)
# End  of Explode SpaceShip

# Last game interface
def lastUI(x,y):
   gamedisplay.blit(lastUI_img,(x,y))
pygame.mixer.music.stop()
lastUI_img=pygame.image.load("last UI.jpg")
lastUI(0,0)
font=pygame.font.SysFont("Tahoma",35)
text=font.render("SURVIVAL TIME :: "+str(int(timevar)),True,red)
gamedisplay.blit(text,(365,400))
pygame.display.update()
text=font.render("LIGHT YRS :: "+str(int(level)),True,yellow)
gamedisplay.blit(text,(365,355))
pygame.display.update()
time.sleep(3.5)
# End of last game interface

pygame.quit()
