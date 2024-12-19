# Example file showing a basic pygame "game loop"
import pygame,random

from pygame import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,400))

clock = pygame.time.Clock()
running = True
img_dino = pygame.image.load("dino.png")
img_cactus = pygame.image.load("cactus.png")
img_bird = pygame.image.load("Bird1.png")
img_dinorun = [pygame.image.load("DinoRun1.png"),pygame.image.load("DinoRun2.png")]
img_dinoduck = [pygame.image.load("DinoDuck1.png"),pygame.image.load("DinoDuck2.png")]
img_birdrun = [pygame.image.load("Bird1.png"),pygame.image.load("Bird2.png")]
cactus_rect = img_cactus.get_rect()
cactus_rect.x = 3000
cactus_rect.y = 330
dino_rect = img_dino.get_rect()
dino_rect.x = 50
dino_rect.y = 300
bird_rect = img_bird.get_rect()
bird_rect.x = 10000
bird_rect.y = 250
is_jumping = False
default_jump = 24
jump = default_jump
cactus_run=12
g = 1.5
score = 0
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
                    
                if event.key == pygame.K_r and gameover == True:
                    gameover = False
                    score = 0
                    cactus_rect.x = 3000
                    bird_rect.x = random.randint(10000,15000)
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_jumping = True
            if event.type == pygame.KEYUP:
                if isducking:
                    isducking = False
                    dino_rect.y = 300
                    
                    

    if not gameover:

        
        if is_jumping:
            
            dino_rect.y -= jump
            jump -= g
            if dino_rect.y >= 300:
                dino_rect.y   =300 
                is_jumping = False                                                               
                jump = default_jump
        cactus_run = 30#random.randint(30,50)
        
        if cactus_run > 45:
            cactus_run += 50
        cactus_rect.x-=cactus_run
        if cactus_rect.x <  0:
            cactus_rect.x = 1200
            score +=1   
        bird_rect.x -= cactus_run
        if bird_rect.x <  0:
            bird_rect.x = random.randint(3000,5000)
            score +=1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        if dino_rect.colliderect(cactus_rect):
            gameover = True
            if highscore < score:
                highscore = score
        if dino_rect.colliderect(bird_rect):
            gameover = True
            if highscore < score:
                highscore = score
        # fill the screen with a color to wipe away anything from last frame
        screen.fill((255,255,255))
        
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
        # RENDER YOUR GAME HERE
        
            
        screen.blit(score_show,(10,10))
        screen.blit(highscore_show,(10,35))
        screen.blit(img_birdrun[frame],bird_rect)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
   
        
pygame.quit()