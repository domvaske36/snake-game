#snake game

import pygame
import random
from snake import Snake

class Apple:

    def __init__(self, screen, GRID_SIZE):
        self.GRID_SIZE = GRID_SIZE
        self.screen = screen
        screen_width, screen_height = screen.get_size()
        apple_x = self.snap_to_grid(random.randint(0, screen_width - GRID_SIZE), GRID_SIZE)
        apple_y = self.snap_to_grid(random.randint(0, screen_height - GRID_SIZE), GRID_SIZE)
        self.apple_position = (apple_x, apple_y)

    def snap_to_grid(self, value, grid_size):
        return (value // grid_size) * grid_size

    def get_Position(self) -> tuple:
        return self.apple_position
                
    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), (self.apple_position[0], self.apple_position[1], 20, 20) )

    #needs to erase if snake collides with
    def respawn(self):
        apple_x = self.snap_to_grid(random.randint(0, self.screen.get_width() - self.GRID_SIZE), self.GRID_SIZE)
        apple_y = self.snap_to_grid(random.randint(0, self.screen.get_height() - self.GRID_SIZE), self.GRID_SIZE)
        self.apple_position = (apple_x, apple_y)


def main():
    #Initialize pygame
    pygame.init()
    pygame.key.set_repeat(0)

    #Set up game window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My First Game")

    #Define game variables
    running = True #Game loop condition
    black = (0,0,0)
    white = (255, 255, 255)

    #snake head - Rectangle variables
    rect_x = 400
    rect_y = 300
    rect_width, rect_height = 20, 20
    GRID_SIZE = rect_width

    snake = Snake(rect_x, rect_y, rect_width, rect_height, screen)

    clock = pygame.time.Clock()

    apple = Apple(screen, GRID_SIZE)

    #Game loop
    while running:
        #Handle events (e.g. keypress, mouse click, quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Quit event
                running = False

        #Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: # Move left
            snake.move("left")
        elif keys[pygame.K_RIGHT]: # Move right
            snake.move("right")
        elif keys[pygame.K_UP]: # Move up
            snake.move("up")
        elif keys[pygame.K_DOWN]: #Move down
            snake.move("down")
        else:
            snake.move()

        #Clear screen with a color (RGB format)
        screen.fill(black) #black background

        #draw snake
        snake.draw()

        #create new apple object
        apple.draw()
        
        #check collision event
        if apple.get_Position() == snake.get_Position():
            apple.respawn()
            snake.grow()

        #update the display
        pygame.display.flip()

        clock.tick(15)

    #Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()