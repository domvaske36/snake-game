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

    #adjust apple position to grid size
    def snap_to_grid(self, value, grid_size):
        return (value // grid_size) * grid_size

    def get_Position(self) -> tuple:
        return self.apple_position
                
    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), (self.apple_position[0], self.apple_position[1], self.GRID_SIZE, self.GRID_SIZE) )

    #redraw apple when snake collides
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
    #starting position
    rect_x = 400
    rect_y = 300
    #size of snake
    rect_width, rect_height = 20, 20
    GRID_SIZE = rect_width

    score = 0

    snake = Snake(rect_x, rect_y, rect_width, rect_height, screen)

    clock = pygame.time.Clock()
    # Set up snake movement timer
    move_snake_event = pygame.USEREVENT + 1  # Custom event for snake movement
    pygame.time.set_timer(move_snake_event, 100)  # Trigger event every 200ms
    apple = Apple(screen, GRID_SIZE)

    #Game loop
    while running:
        #Handle events (e.g. keypress, mouse click, quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Quit event
                running = False
            elif event.type == move_snake_event:  # Triggered every 200ms
                snake.move()  # Move the snake
            elif event.type == pygame.KEYDOWN:  # Handle directional changes
                if (event.key == pygame.K_LEFT) and snake.get_current_direction() != "right":
                    snake.move("left")
                elif event.key == pygame.K_RIGHT and snake.get_current_direction() != "left":
                    snake.move("right")
                elif event.key == pygame.K_UP and snake.get_current_direction() != "down":
                    snake.move("up")
                elif event.key == pygame.K_DOWN and snake.get_current_direction() != "up":
                    snake.move("down")
        # #Get keys pressed
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]: # Move left
        #     snake.move("left")
        # elif keys[pygame.K_RIGHT]: # Move right
        #     snake.move("right")
        # elif keys[pygame.K_UP]: # Move up
        #     snake.move("up")
        # elif keys[pygame.K_DOWN]: #Move down
        #     snake.move("down")
        # else:
        #     snake.move()

        #Clear screen with a color (RGB format)
        screen.fill(black) #black background

        #draw snake
        snake.draw()

        #create new apple object
        apple.draw()
        
        #check collision event
        if apple.get_Position() == snake.get_Position():
            score += 1
            apple.respawn()
            snake.grow()

        #check if snake collides with itself
        if snake.self_collision() is True:
            font = pygame.font.Font(None, 74)
            text = font.render(f"Game Over, Score: {score}", True, (255, 0, 0))
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
            pygame.display.flip()  # Update the display
            pygame.time.wait(2000)  # Pause for 2 seconds before quitting
            running = False

        #update the display
        pygame.display.flip()

        clock.tick(60)

    #Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()