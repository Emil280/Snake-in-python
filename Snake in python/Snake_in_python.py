import pygame
import random
import os

WIDTH, HEIGHT = 800, 800
Win= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")
APPLE_IMAGE = pygame.image.load(os.path.join('Assets','apple.png'))
APPLE_IMAGE = pygame.transform.scale(APPLE_IMAGE, (40,40))
HEAD_UP = pygame.image.load(os.path.join('Assets','head_up.png'))
HEAD_DOWN = pygame.image.load(os.path.join('Assets','head_down.png'))
HEAD_LEFT = pygame.image.load(os.path.join('Assets','head_left.png'))
HEAD_RIGHT = pygame.image.load(os.path.join('Assets','head_right.png'))
BODY_LEFT_DOWN = pygame.image.load(os.path.join('Assets','body_bottomleft.png'))
BODY_LEFT_UP = pygame.image.load(os.path.join('Assets','body_topleft.png'))
BODY_RIGHT_DOWN = pygame.image.load(os.path.join('Assets','body_bottomright.png'))
BODY_RIGHT_UP = pygame.image.load(os.path.join('Assets','body_topright.png'))
BODY_VERTICAL = pygame.image.load(os.path.join('Assets','body_vertical.png'))
BODY_HORIZONTAL = pygame.image.load(os.path.join('Assets','body_horizontal.png'))
TAIL_UP = pygame.image.load(os.path.join('Assets','tail_up.png'))
TAIL_DOWN = pygame.image.load(os.path.join('Assets','tail_down.png'))
TAIL_RIGHT = pygame.image.load(os.path.join('Assets','tail_right.png'))
TAIL_LEFT = pygame.image.load(os.path.join('Assets','tail_left.png'))
GREEN=(46, 204, 14)
DARKGREEN=(32,135,11)

FPS=60

def draw_window():  #Makes a 20x20 board with 50x50 pixel squares
    Column_place = 0
    for Row in range(20):
        Row_place = 0
        for Column in range(20):
            if Row % 2 == 0:
                if Column % 2 == 0:
                    pygame.draw.rect(Win,GREEN,(Row_place,Column_place,40,40))
                else:
                    pygame.draw.rect(Win,DARKGREEN,(Row_place,Column_place,40,40))
            else:
                if Column % 2 == 0:
                    pygame.draw.rect(Win,DARKGREEN,(Row_place,Column_place,40,40)) 
                else:
                    pygame.draw.rect(Win,GREEN,(Row_place,Column_place,40,40))
            Row_place += 40
        Column_place += 40
    pygame.display.update()



def place_random_apples():
    Row = random.randint(0,20)*40
    Column = random.randint(0,20)*40
    Win.blit(APPLE_IMAGE,(Row-1,Column))
    pygame.display.update()

def main():
    clock=pygame.time.Clock()
    run=True
    draw_window()
    place_random_apples()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
    pygame.quit()

if __name__ == "__main__":
    main()