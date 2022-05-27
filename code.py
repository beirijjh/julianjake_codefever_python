#schip aan de rechter kant beweeg je met z boven s onder q links d rechts
#schieten met het rechter schip is met rechter control
#schip aan de linker kant beweeg je met bovenste pijl boven, onderste pijl onder, linkse pijl links, rechtse pijl rechts
#schieten met het linker schip is met linker control










from operator import truediv
import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30
VEL = 10
BULLET_VEL = 7
MAX_BULLETS = 100
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
YELLOW_SPACESHIP_IMAGE, (55, 40)), 90)
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (55, 40)), 270)
pygame.display.set_caption("fighters")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (145, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


def draw_window(red, yellow, red_bullets, yellow_bullets):
    WIN.fill((PURPLE))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)    
        
    pygame.display.update()

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
             pygame.event.post(pygame.event.Event(RED_HIT))   
             yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

def main():
    red = pygame.Rect( 700, 300, 55, 40)
    yellow = pygame.Rect(100, 300, 55, 40)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():           
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL  and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)        
                    red_bullets.append(bullet)
           
        
        
        
        
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]and red.y - VEL > 0:
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN]and red.y + VEL + yellow.height < HEIGHT - 15:
            red.y += VEL
        if keys_pressed[pygame.K_RIGHT]and red.x + VEL + yellow.width < WIDTH:
            red.x += VEL
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
            red.x -= VEL
    
        if keys_pressed[pygame.K_z] and yellow.y - VEL > 0:
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:
            yellow.y += VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
            yellow.x += VEL
        if keys_pressed[pygame.K_q] and yellow.x - VEL > 0:
            yellow.x -= VEL


        handle_bullets(yellow_bullets, red_bullets, yellow, red)    
          
        
        draw_window(red, yellow, red_bullets, yellow_bullets)         
           
    pygame.quit()

if __name__ == "__main__":
    main()
