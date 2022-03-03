import pygame
from pygame.image import frombuffer
from pygame.math import Vector2
import random
import os

FPS = 144   #for best performance on high refreshrate monitor xD
SPEED = 90 #the lower the speed the faster the snake 
WIDTH, HEIGHT = 800, 800
Win= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")

APPLE_IMAGE = pygame.image.load(os.path.join('Assets','apple.png'))




class SNAKE:
    def __init__(self):
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]  #starting position
        self.direction = Vector2(1,0)
        self.expand = False
        self.HEAD_UP = pygame.image.load(os.path.join('Assets','head_up.png'))
        self.HEAD_DOWN = pygame.image.load(os.path.join('Assets','head_down.png'))
        self.HEAD_LEFT = pygame.image.load(os.path.join('Assets','head_left.png'))
        self.HEAD_RIGHT = pygame.image.load(os.path.join('Assets','head_right.png'))
        self.BODY_LEFT_UP = pygame.image.load(os.path.join('Assets','body_bottomleft.png'))
        self.BODY_LEFT_DOWN = pygame.image.load(os.path.join('Assets','body_topleft.png'))
        self.BODY_RIGHT_UP = pygame.image.load(os.path.join('Assets','body_bottomright.png'))
        self.BODY_RIGHT_DOWN = pygame.image.load(os.path.join('Assets','body_topright.png'))
        self.BODY_VERTICAL = pygame.image.load(os.path.join('Assets','body_vertical.png'))
        self.BODY_HORIZONTAL = pygame.image.load(os.path.join('Assets','body_horizontal.png'))
        self.TAIL_UP = pygame.image.load(os.path.join('Assets','tail_up.png'))
        self.TAIL_DOWN = pygame.image.load(os.path.join('Assets','tail_down.png'))
        self.TAIL_RIGHT = pygame.image.load(os.path.join('Assets','tail_right.png'))
        self.TAIL_LEFT = pygame.image.load(os.path.join('Assets','tail_left.png'))

    def draw(self):
        self.head_pos()
        self.tail_pos()
        for index,block in enumerate(self.body):
            x_pos=int(block.x*40)
            y_pos=int(block.y*40)
            block_rect=pygame.Rect(x_pos,y_pos,40,40)
            if index==0:
                Win.blit(self.head,block_rect)
            elif index==len(self.body)-1:
                Win.blit(self.tail,block_rect)
            else:
                previous_block=self.body[index+1]-block #index is the current element of the body
                next_block=self.body[index-1]-block
                if previous_block.x==next_block.x:
                    Win.blit(self.BODY_VERTICAL,block_rect)
                elif previous_block.y==next_block.y:
                    Win.blit(self.BODY_HORIZONTAL,block_rect)
                else:
                    if previous_block.x==-1 and next_block.y == -1 or previous_block.y==-1 and next_block.x == -1:
                        Win.blit(self.BODY_RIGHT_UP,block_rect)
                    elif previous_block.x==-1 and next_block.y==1 or previous_block.y==1 and next_block.x==-1:
                        Win.blit(self.BODY_RIGHT_DOWN,block_rect)
                    elif previous_block.x==1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==1:
                        Win.blit(self.BODY_LEFT_UP,block_rect)
                    elif previous_block.x==1 and next_block.y==1 or previous_block.y==1 and next_block.x ==1:
                        Win.blit(self.BODY_LEFT_DOWN,block_rect)


    def move(self):
        if self.expand == True:
            body_copy = self.body[:]   #copies the snakebody
            body_copy.insert(0,body_copy[0]+self.direction) #adds an extra block
            self.body=body_copy[:] #saves the new snake body
            self.expand=False #stops extending the snake
        else:
            body_copy = self.body[:-1]   #copies the list self.body besides the last element
            body_copy.insert(0,body_copy[0]+self.direction) #adds the direction vector to the head in the copy
            self.body=body_copy[:]      #saves the copy to the main body of the snake
        
    def head_pos(self):
        relative_pos= self.body[1] - self.body[0] #subtracts first vector from second vector in body to get the position of the head relative to the rest of the body
        if relative_pos==Vector2(1,0):
            self.head=self.HEAD_LEFT
        elif relative_pos==Vector2(-1,0):
            self.head=self.HEAD_RIGHT
        elif relative_pos==Vector2(0,1):
            self.head=self.HEAD_UP
        elif relative_pos==Vector2(0,-1):
            self.head=self.HEAD_DOWN

    def tail_pos(self):
        relative_pos= self.body[-2] - self.body[-1]
        if relative_pos==Vector2(1,0):
            self.tail=self.TAIL_LEFT
        elif relative_pos==Vector2(-1,0):
            self.tail=self.TAIL_RIGHT
        elif relative_pos==Vector2(0,1):
            self.tail=self.TAIL_UP
        elif relative_pos==Vector2(0,-1):
            self.tail=self.TAIL_DOWN


    def extend_body(self):
        self.expand = True

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
            self.snake.extend_body()
        else:
            self.check_eat_apple = False
        return self.check_eat_apple

    def check_die(self):
        die = False
        if self.snake.body[0].x not in range (0,20) or self.snake.body[0].y not in range (0,20):
            die = True
        return die


def Display_message(text):
    pygame.font.init()
    White = (255,255,255)
    Grey = (169,169,169)
    font = pygame.font.Font('freesansbold.ttf', 60)
    Text = font.render(text, True, White)
    Shadow = font.render(text, True, Grey)
    Win.blit(Shadow, (120,202))
    Win.blit(Text, (118,200))
    pygame.display.update()

main_game = MAIN()
snake = SNAKE()

def main():
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,SPEED)
    clock=pygame.time.Clock()
    run=True
    main_game.print_assets()
    snake.draw()
    score = 0
    Start = False
    Die = False
    Display_message('Press Space To Start')
    pygame.display.update()
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
                if event.key == pygame.K_SPACE:
                    Start = True
            if event.type == SCREEN_UPDATE and not Die and Start:          #every SPEED ms the snake will move 
                main_game.update_assets()
                main_game.update_snake()
                check_eat_apple = main_game.eat_apple()
                check_die = main_game.check_die()
                if check_die:
                    Die = True
                if check_eat_apple:
                    score = score + 1
                    print(f'score:{score}')
                pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()