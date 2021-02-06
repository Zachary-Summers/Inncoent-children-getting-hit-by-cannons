#Innocent children getting hit by cannons!
import pygame,sys,random,pyautogui
pygame.init()

name='Innocent children getting hit by cannons!'

w=315
h=560
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption(name)
time=-1
points=-1

qwirle_x=w//2
qwirle_x_change=0
qwirle_y=h-30
qwirle_rad=10
qwirle_color=(166,16,30)
qwirle_socs=True#increbidley Inportant
qwirle=pygame.draw.circle(screen,qwirle_color,(qwirle_x,qwirle_y),qwirle_rad)

inkilt_rad=10
innkilt_x=random.randint(inkilt_rad,w-inkilt_rad)
innkilt_y=-1
innkilt_color=(229, 186, 189)

font=pygame.font.SysFont('comicsansms',25)
text=font.render(str(points),True,(255,0,204))

while True:
    time+=1
    pygame.time.wait(5)
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RALT:
                    qwirle_x_change=-1
                elif event.key==pygame.K_LALT:
                    qwirle_x_change=1
            elif event.type==pygame.KEYUP:
                qwirle_x_change=0
                
    screen.fill((0,0,0))
    if time==0 or time%3000==0:
        points+=1
    
    qwirle_x+=qwirle_x_change
    if qwirle_x+qwirle_rad>=w:
        qwirle_x_change=-1
    elif qwirle_x-qwirle_rad<=0:qwirle_x_change=1
    
    if innkilt_y>=h-25:
        innkilt_y=-1
    
    innkilt_y+=1
    
    iKilt=pygame.draw.circle(screen,innkilt_color,(innkilt_x,innkilt_y),inkilt_rad)
    
    qwirle=pygame.draw.circle(screen,qwirle_color,(qwirle_x,qwirle_y),qwirle_rad)
    
    
    text=font.render(str(points),True,(255,0,204))
    textRect=text.get_rect(topleft=(20,20))
    screen.blit(text,textRect)
    
    pygame.display.update()