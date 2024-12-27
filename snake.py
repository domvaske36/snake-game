#snake.py

import pygame

class Snake:
    #head of the snake,
    
    def __init__(self, x_pos, y_pos, width, height, speed, screen):
        self.head_x = x_pos
        self.head_y = y_pos
        self._snake_width = width
        self._snake_height = height
        self._speed = speed
        self._color = (0, 255, 0)  # Green color for the snake
        self.current_direction = None
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self._color, (self.head_x, self.head_y, self._snake_width, self._snake_height) )

    #to be called every loop iteration
    #once current direction updated, shift current position continously
    def move(self, turn: str = None):
        # Update direction if a new direction is given
        if turn is not None:
            self.current_direction = turn

        # Move in the current direction
        if self.current_direction == "left":
            self.head_x -= self._speed
        elif self.current_direction == "right":
            self.head_x += self._speed
        elif self.current_direction == "up":
            self.head_y -= self._speed
        elif self.current_direction == "down":
            self.head_y += self._speed

        # Check boundaries
        if self.head_x < 0:
            self.head_x = 0
        if self.head_x > self.screen.get_width() - self._snake_width:
            self.head_x = self.screen.get_width() - self._snake_width
        if self.head_y < 0:
            self.head_y = 0
        if self.head_y > self.screen.get_height() - self._snake_height:
            self.head_y = self.screen.get_height() - self._snake_height
        
    def collision(self):
        pass