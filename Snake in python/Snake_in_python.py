import pygame
from pygame.image import frombuffer
from pygame.math import Vector2
import random
import os

FPS = 144   #for best performance on high refreshrate monitor xD
SPEED = 100 #the lower the speed the faster the snake 
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



class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]  #starting position
        self.direction = Vector2(1,0)

    def draw(self):
        for block in self.body:
            x_position = int(block.x * 40)
            y_position = int(block.y * 40)
            block_rect = pygame.Rect(x_position, y_position,40,40)
            pygame.draw.rect(Win,(100,100,100),block_rect)

    def move(self):
        body_copy = self.body[:-1]   #copies the list self.body besides the last element
        body_copy.insert(0,body_copy[0]+self.direction) #adds the direction vector to the head in the copy
        self.body=body_copy[:]      #saves the copy to the main body of the snake

class FRUIT():
    def __init__(self):
        x_pos = random.randint(0,19)
        y_pos = random.randint(0,19)
        self.fruit_position = Vector2(x_pos,y_pos)
    
    def place_random_apple(self):
        fruit_rect = pygame.Rect(int(self.fruit_position.x*40),int(self.fruit_position.y*40),40,40)
        Win.blit(APPLE_IMAGE,fruit_rect)
    
    def draw_window(self):  #Makes a 20x20 board with 50x50 pixel squares
        Column_place = 0
        GREEN=(123, 222, 62)
        DARKGREEN=(84, 171, 31)
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

class MAIN():
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()     #joining both classes togather into the main class
        self.check_eat_apple = False
    def update_snake(self):
        self.snake.move()
        self.snake.draw()


    def print_assets(self):              #prints the board and chooses the first place for the apple
        self.fruit.draw_window()
        self.fruit.place_random_apple()

    def update_assets(self):
        self.fruit.draw_window()
        if self.check_eat_apple:  #if apple has been eaten it randomly chooses new coordinates
            self.fruit.x_pos = random.randint(0,19)
            self.fruit.y_pos = random.randint(0,19)
            self.fruit.fruit_position = Vector2(self.fruit.x_pos,self.fruit.y_pos)
        else:
         self.fruit.place_random_apple()

    def eat_apple(self):
        if self.fruit.fruit_position == self.snake.body[0]:  #if coordinate of head and apple the same it do the thingy
            self.fruit.place_random_apple()
            self.check_eat_apple = True
        else:
            self.check_eat_apple = False
        return self.check_eat_apple

    def check_die(self):
        die = False
        if self.snake.body[0].x not in range (0,20) or self.snake.body[0].y not in range (0,20):
            die = True
        return die



main_game = MAIN()

def main():
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,SPEED)
    clock=pygame.time.Clock()
    run=True
    main_game.print_assets()
    score = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:         #change direction vector dependant on key pressed
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    main_game.snake.direction = Vector2(-1,0)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    main_game.snake.direction = Vector2(1,0)
            if event.type == SCREEN_UPDATE:          #every SPEED ms the snake will move 
                main_game.update_assets()
                main_game.update_snake()
                check_eat_apple = main_game.eat_apple()
                check_die = main_game.check_die()
                if check_die:
                    print('ok this die thing works i expand later')
                if check_eat_apple:
                    score = score + 1
                    print(f'score:{score}')
                pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()