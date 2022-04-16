from matplotlib.pyplot import draw
import pygame, random

from LinkedList import Node, LinkedList
from Point import Point


class Snake:
    def __init__(self, screen, width, height, color):
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color
        self.speed = 4
        self.direction = 'right'
        self.score = 0
        self.tile_size = 30
        self.snake = LinkedList()
        self.snake.AddLast(Node(Point((width // 2), height // 2)))
        self.snake.AddLast(Node(Point((width // 2) - self.tile_size, height // 2)))
        self.snake.AddLast(Node(Point((width // 2) - self.tile_size * 2, height // 2)))
    
    def draw(self):
        for node in self.snake:
            pygame.draw.rect(self.screen, self.color, (node.data.x+1, node.data.y+1, self.tile_size-2, self.tile_size-2))
            
    def move(self):
        if self.direction == 'right':
            self.snake.AddFirst(Node(Point(self.snake.head.data.x + self.tile_size, self.snake.head.data.y)))
        elif self.direction == 'left':
            self.snake.AddFirst(Node(Point(self.snake.head.data.x - self.tile_size, self.snake.head.data.y)))
        elif self.direction == 'up':
            self.snake.AddFirst(Node(Point(self.snake.head.data.x, self.snake.head.data.y - self.tile_size)))
        elif self.direction == 'down':
            self.snake.AddFirst(Node(Point(self.snake.head.data.x, self.snake.head.data.y + self.tile_size)))
        self.snake.RemoveLast()
        
    def change_direction(self, direction):
        if direction == 'right' and self.direction != 'left':
            self.direction = direction
        elif direction == 'left' and self.direction != 'right':
            self.direction = direction
        elif direction == 'up' and self.direction != 'down':
            self.direction = direction
        elif direction == 'down' and self.direction != 'up':
            self.direction = direction  
            
    def check_collision(self):
        if self.snake.head.data.x < 0 or self.snake.head.data.x > self.width - self.tile_size or self.snake.head.data.y < 0 or self.snake.head.data.y > self.height - self.tile_size:
            return True
        return False
    
    def get_speed(self):
        match self.speed:
            case 1:
                return 40
            case 2:
                return 30
            case 3:
                return 20
            case 4:
                return 10
            case 5:
                return 5
            
    def increase_speed(self):
        if self.speed < 5:
            self.speed += 1
            
    def grow(self):
        self.snake.AddLast(Node(Point(self.snake.tail.data.x, self.snake.tail.data.y)))
    
def random_food(snake, width, height):
    random_x = random.randint(0, (width - 30) // 30) * 30
    random_y = random.randint(0, (height - 30) // 30) * 30
    food =  Point(random_x, random_y)
    for node in snake.snake:
        if node.data.x == food.x and node.data.y == food.y:
            food = random_food(snake, width, height)
    return food

def draw_food(screen, food):
    pygame.draw.rect(screen, (255, 0, 0), (food.x, food.y, 30, 30))
            
def main():
    pygame.init()
    width = 900
    height = 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    timer = 0
    color = (0, 255, 0)
    snake = Snake(screen, width, height, color)
    food = random_food(snake, width, height)
    while True:
        timer += clock.get_rawtime()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.change_direction('right')
                elif event.key == pygame.K_LEFT:
                    snake.change_direction('left')
                elif event.key == pygame.K_UP:
                    snake.change_direction('up')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('down')
        screen.fill((0, 0, 0))
        snake.draw()
        draw_food(screen, food)
        if timer >= snake.get_speed():
            snake.move()
            timer = 0
        if snake.check_collision():
            pygame.quit()
            quit()
        headRect = pygame.Rect(snake.snake.head.data.x, snake.snake.head.data.y, 30, 30)
        foodRect = pygame.Rect(food.x, food.y, 30, 30)
        if headRect.colliderect(foodRect):
            snake.score += 1
            snake.grow()
            food = random_food(snake, width, height)
        pygame.display.update()
        clock.tick(100)
        
if __name__ == '__main__':
    main()