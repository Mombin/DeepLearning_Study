import pygame
import time
from datetime import datetime
from pytz import timezone
from datetime import timedelta

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
PURPLE = 127, 0, 127
BLACK = 0, 0, 0
GRAY = 127, 127, 127
WHITE = 255, 255, 255

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

class Snake:
    """class Snake"""
    color = BLUE

    def __init__(self):
        self.positions = [(9,6), (9,7),(9,8),(9,9)]
        self.direction = 'north'

    def draw(self, screen):
        """draw snake in Board"""
        for position in self.positions:
            draw_block(screen, self.color, position)


class Apple:
    """class Apple"""
    color = RED
    def __init__(self, position=(5,5)):
        self.position = position

    def draw(self, screen):
        """draw Apple in Boared"""
        draw_block(screen, self.color, self.position)

class GameBoard:
    """Board for Snake World"""
    width = 20
    height = 20
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()

    def draw(self, screen):
        self.apple.draw(screen)
        self.snake.draw(screen)



def draw_background(screen):
    """draw background"""
    background = pygame.Rect((0,0),(SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)

def draw_block(screen, color, position):
    """draw block on position"""
    block = pygame.Rect((position[1]*BLOCK_SIZE, position[0]*BLOCK_SIZE),
                        (BLOCK_SIZE,BLOCK_SIZE))
    pygame.draw.rect(screen,color,block)

DIRECTION_ON_KEY = {
    pygame.K_UP: 'north',
    pygame.K_DOWN: 'south',
    pygame.K_LEFT: 'west',
    pygame.K_RIGHT: 'east',
}
block_direction = 'east'
block_position = [0, 0]
last_moved_time = datetime.now()


#start game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# draw_background(screen)
# draw_block(screen, BLUE, block_position)

game_board = GameBoard()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    #     if event.type == pygame.KEYDOWN:
    #         block_direction = DIRECTION_ON_KEY[event.key]
    # if timedelta(seconds=1) <= datetime.now() - last_moved_time:
    #     if block_direction == 'north':
    #         block_position[0] -= 1
    #     elif block_direction == 'south':
    #         block_position[0] += 1
    #     elif block_direction == 'west':
    #         block_position[1] -= 1
    #     elif block_direction == 'east':
    #         block_position[1] += 1
    #     last_moved_time = datetime.now()


    draw_background(screen)
    game_board.draw(screen)
    pygame.display.update()