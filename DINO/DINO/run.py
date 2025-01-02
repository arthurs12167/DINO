# Example file showing a basic pygame "game loop"
from pickle import FALSE
import pygame,random

from pygame import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,400))
img_track = pygame.image.load("track.png")
track_rect = img_track.get_rect()
now_track_rect = 0

clock = pygame.time.Clock()
running = True
img_missile = pygame.image.load("missile.png")
img_dino = pygame.image.load("dino.png")
img_cactus = pygame.image.load("cactus.png")
img_bird = pygame.image.load("Bird1.png")
img_dinorun = [pygame.image.load("DinoRun1.png"),pygame.image.load("DinoRun2.png")]
img_dinoduck = [pygame.image.load("DinoDuck1.png"),pygame.image.load("DinoDuck2.png")]
img_birdrun = [pygame.image.load("Bird1.png"),pygame.image.load("Bird2.png")]
cactus_rect = img_cactus.get_rect()
img_missile = pygame.transform.scale(img_missile,(100,50))
cactus_rect.x = random.randint(2500,4000)
cactus_rect.y = 310
dino_rect = img_dino.get_rect()
dino_rect.x = 50
dino_rect.y = 290
bird_rect = img_bird.get_rect()
bird_rect.x = random.randint(8000,12000)
bird_rect.y = 230
is_jumping = False
default_jump = 24
jump = default_jump
initspeed= 12
cactus_run=initspeed
missile_rect = img_missile.get_rect()
missile_rect.x = dino_rect.x+10
missile_rect.y = dino_rect.y+20
attack = False
g = 1.5
score = 0
level = 0
levelspeed = [12,16,20,30,40]
highscore = 0
gameover = False
font = pygame.font.Font(None,36)
lasttime = 0
frame = 0
isducking = False

    
while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    is_jumping = True
                if event.key == pygame.K_DOWN:
                    isducking = True
                if event.key == pygame.K_v and attack == False:
                    missile_rect.y = dino_rect.y+20
                    attack=True
                    
                if event.key == pygame.K_r and gameover == True:
                    gameover = False
                    score = 0
                    cactus_rect.x = 3000
                    bird_rect.x = random.randint(8000,12000)
                    cactus_run=initspeed
                    attack = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_jumping = True
            if event.type == pygame.KEYUP:
                if isducking:
                    isducking = False
                    dino_rect.y = 300
                    
                    

    if not gameover:
        score +=1
        if score>3000:
            cactus_run = levelspeed[3]
            level = 3
        elif score >2000:
            cactus_run = levelspeed[2]
            level =2
        elif score >1000:
            cactus_run = levelspeed[1]
            level = 1
        if is_jumping:
            
            dino_rect.y -= jump
            jump -= g
            if dino_rect.y >= 290:
                dino_rect.y   =290 
                is_jumping = False                                                               
                jump = default_jump
        #random.randint(30,50)
  
        cactus_rect.x-=cactus_run
        if cactus_rect.x <  0:
            cactus_rect.x = random.randint(1280,3000)
       
        bird_rect.x -= cactus_run
        if bird_rect.x <  0:
            bird_rect.x = random.randint(10000,15000)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        if dino_rect.colliderect(cactus_rect) or dino_rect.colliderect(bird_rect):
            gameover = True
            if highscore < score:
                highscore = score
        
        # fill the screen with a color to wipe away anything from last frame
        screen.fill((255,255,255))
        
        if attack:
            missile_rect.x += 20
            
            screen.blit(img_missile,missile_rect)
            if missile_rect.colliderect(cactus_rect):
                cactus_rect.x = random.randint(1280,3000)
                missile_rect.x = dino_rect.x+10
                attack=False
            if missile_rect.colliderect(bird_rect):
                bird_rect.x = random.randint(10000,15000)
                missile_rect.x = dino_rect.x+10
                attack=False
            if missile_rect.x > 1500:
                missile_rect.x = dino_rect.x+10
                attack=False


        screen.blit(img_cactus,cactus_rect)
        if gameover:
            dino_rect.y = 300
            gameover1 = font.render(f"gameover",True,(0,0,0))
            screen.blit(gameover1,(550,35))
            screen.blit(img_dino,dino_rect)
        score_show = font.render(f"score:{score}",True,(0,0,0))
        nowtime = pygame.time.get_ticks()
        if nowtime - lasttime > 40:
            frame = (frame +1)%2
            lasttime = nowtime
            
        if not gameover:
            if isducking:
                    dino_rect.y = 340
                    screen.blit(img_dinoduck[frame],dino_rect)
            else:
                    
                    screen.blit(img_dinorun[frame],dino_rect)
        highscore_show = font.render(f"highest score:{highscore}",True,(0,0,0))
        level_show = font.render(f"Level: {level}",True, (0,0,0))
        screen.blit(level_show,(10,55))
        # RENDER YOUR GAME HERE

        screen.blit(img_track,(now_track_rect,370)) 
        now_track_rect = (now_track_rect -10)%100 -100
        screen.blit(score_show,(10,10))
        screen.blit(highscore_show,(10,35))
        screen.blit(img_birdrun[frame],bird_rect)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
   
        
pygame.quit()