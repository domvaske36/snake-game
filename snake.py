#snake.py

import pygame

class Snake:
    #head of the snake,
    
    def __init__(self, x_pos, y_pos, width, height, screen):
        self.body = [(x_pos, y_pos), (x_pos - width, y_pos), (x_pos - 2*width, y_pos)]
        self.initial_posiition = True
        self._snake_width = width
        self._snake_height = height
        self._speed = width
        self._color = (0, 255, 0)  # Green color for the snake
        self.current_direction = None
        self.screen = screen

    def draw(self):
        for i in range(len(self.body)):
            pygame.draw.rect(self.screen, self._color, (self.body[i][0], self.body[i][1], self._snake_width, self._snake_height) )

    #to be called every loop iteration
    #once current direction updated, shift current position continously
    def move(self, turn: str = None):
        # Update direction if a new direction is given
        if turn is not None:
            self.initial_posiition = False
            self.current_direction = turn

        #update snake body starting from tail
        if (len(self.body) > 1 and not self.initial_posiition):
            for i in range(len(self.body)-1, 0, -1):
                self.body[i] = self.body[i - 1]

        # update the head
        if self.current_direction == "left":
            self.body[0] = (self.body[0][0] - self._speed, self.body[0][1])
        elif self.current_direction == "right":
            self.body[0] = (self.body[0][0] + self._speed, self.body[0][1])
        elif self.current_direction == "up":
            self.body[0] = (self.body[0][0], self.body[0][1] - self._speed)
        elif self.current_direction == "down":
            self.body[0] = (self.body[0][0], self.body[0][1] + self._speed)

        # Check boundaries
        if self.body[0][0] < 0:
            self.body[0] = (0, self.body[0][1])
        if self.body[0][0] > self.screen.get_width() - self._snake_width:
            self.body[0] = (self.screen.get_width() - self._snake_width, self.body[0][1])
        if self.body[0][1] < 0:
            self.body[0] = (self.body[0][0], 0)
        if self.body[0][1] > self.screen.get_height() - self._snake_height:
            self.body[0] = (self.body[0][0], self.screen.get_height() - self._snake_height)
        
    def grow(self):
        self.body.append(self.body[-1])

    def get_current_direction(self):
        return self.current_direction
    
    #return position of snake head as a tuple
    def get_Position(self) -> tuple:
        return self.body[0]