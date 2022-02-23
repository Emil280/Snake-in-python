import pygame
import random
import os

WIDTH, HEIGHT = 800, 800
Win= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")
APPLE_IMAGE = pygame.image.load(os.path.join('Assets','apple.png'))
APPLE_IMAGE = pygame.transform.scale(APPLE_IMAGE, (40,40))
testing syncing to github
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
                    pygame.draw.rect(Win,GREEN,(Row_place,Column_place,50,50))
                else:
                    pygame.draw.rect(Win,DARKGREEN,(Row_place,Column_place,50,50))
            else:
                if Column % 2 == 0:
                    pygame.draw.rect(Win,DARKGREEN,(Row_place,Column_place,50,50)) 
                else:
                    pygame.draw.rect(Win,GREEN,(Row_place,Column_place,50,50))
            Row_place += 40
        Column_place += 40
    pygame.display.update()



def place_random_apples():
    Row = random.randint(0,20)*40
    Column = random.randint(0,20)*40
    Win.blit(APPLE_IMAGE,(Row+1,Column+1))
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