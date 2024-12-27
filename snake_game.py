#snake game

import pygame
from snake import Snake

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
    rect_width = 20
    rect_height = 20
    speed = 5

    snake = Snake(rect_x, rect_y, rect_width, rect_height, speed, screen)

    clock = pygame.time.Clock()

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

        #update the display
        pygame.display.flip()

        clock.tick(30)

    #Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()