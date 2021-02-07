#Innocent children getting hit by lasers!
import pygame,sys,random,pyautogui
pygame.init()

name='Innocent children getting hit by cannons!'

w=315
h=560
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption(name)
time=-1
points=0

qwirle_x=w//2
qwirle_x_change=0
qwirle_y=h-30
qwirle_rad=13
qwirle_color=(166,16,30)
qwirle_socs=True#increbidley Inportant
qwirle=pygame.image.load('rocket.png')
qwirle=pygame.transform.scale(qwirle,(24,24))
galaxy_note_qwirle_ultra=qwirle.get_rect(center=(qwirle_x,qwirle_y))

inkilt_rad=13
innkilt_x=random.randint(inkilt_rad,w-inkilt_rad)
innkilt_y=-1
innkilt_color=(0,255,255)

iKilt=pygame.image.load('iKilt.png')
iKilt=pygame.transform.scale(iKilt,(24,24))
iKilt_pro=iKilt.get_rect(center=(innkilt_x,innkilt_y))

connins=[]

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
    if time%2==0:
        for i in range(0,random.randint(50,75)):
            pygame.draw.circle(screen,(255,255,255),(random.randint(0,w),random.randint(0,h)),random.randint(2,5))
    
    connins.append({'x':qwirle_x,'y':qwirle_y,'radius':4,'type':0})
    connins.append({'x':qwirle_x,'y':qwirle_y,'radius':2,'type':1})
    
    for i in connins:
        if not i['type']:
            i['y']-=1
            pygame.draw.circle(screen,(0,255,0),(i['x'],i['y']),i['radius'])
            if pygame.draw.circle(screen,innkilt_color,(innkilt_x,innkilt_y),inkilt_rad).colliderect(pygame.draw.circle(screen,(0,255,0),(i['x'],i['y']),i['radius'])):
                points+=1
                innkilt_y=-1
                innkilt_x=random.randint(inkilt_rad,w-inkilt_rad)
                

        else:
            i['y']+=1
            pygame.draw.circle(screen,qwirle_color,(i['x'],i['y']),i['radius'])
          
    qwirle_x+=qwirle_x_change
    if qwirle_x+qwirle_rad>=w:
        qwirle_x_change=-1
    elif qwirle_x-qwirle_rad<=0:qwirle_x_change=1
    
    if innkilt_y>=h-25:
        innkilt_y=-1
        innkilt_x=random.randint(inkilt_rad,w-inkilt_rad)
        points-=1
    
    innkilt_y+=2
    
    _3030_iKilt_pro_max_m1100_100G_iIlXl_35hb_version_verizon_1265k_1000ppi=pygame.draw.circle(screen,innkilt_color,(innkilt_x,innkilt_y),inkilt_rad)#aldo increbidley inportant
    iKilt_pro=iKilt.get_rect(center=(innkilt_x,innkilt_y))
    screen.blit(iKilt,iKilt_pro)
    
    galaxy_note_qwirle_ultra=qwirle.get_rect(center=(qwirle_x,qwirle_y))
    screen.blit(qwirle,galaxy_note_qwirle_ultra)
    
    text=font.render(str(points),True,(255,0,204))
    textRect=text.get_rect(topleft=(20,20))
    screen.blit(text,textRect)
    
    pygame.display.update()