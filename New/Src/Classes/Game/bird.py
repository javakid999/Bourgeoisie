import pygame

class Bird:
    def __init__(self, position):
        self.position = position
    def render(self, display, image):
        pygame.draw.rect(display, (0, 100, 0), (self.position.x, self.position.y, 16, 16))