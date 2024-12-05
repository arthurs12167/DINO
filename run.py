# Example file showing a basic pygame "game loop"
import pygame,random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,400))

clock = pygame.time.Clock()
running = True
img_dino = pygame.image.load("dino.png")
img_cactus = pygame.image.load("cactus.png")
cactus_rect = img_cactus.get_rect()
cactus_rect.x = 2000
cactus_rect.y = 330
dino_rect = img_dino.get_rect()
dino_rect.x = 50
dino_rect.y = 300
is_jumping = False
default_jump = 24
jump = default_jump
cactus_run=12
g = 1.5
score = 0
font = pygame.font.Font(None,36)
while running:
   
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    score +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_jumping = True

    if is_jumping:
        
        dino_rect.y -= jump
        jump -= g
        if dino_rect.y >= 300:
            dino_rect.y   =300 
            is_jumping = False
            jump = default_jump
    cactus_run = random.randint(1,60)
    if cactus_run > 50:
        cactus_run += 50
    cactus_rect.x-=cactus_run
    if cactus_rect.x < 0:
        cactus_rect.x = 1200
    # fill the screen with a color to wipe away anything from last frame
    screen.fill((255,255,255))
    screen.blit(img_dino,dino_rect)
    screen.blit(img_cactus,cactus_rect)
    score_show = font.render(f"score:{score}",True,(0,0,0))
    # RENDER YOUR GAME HERE
    screen.blit(score_show,(10,10))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()