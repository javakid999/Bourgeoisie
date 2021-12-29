import pygame

class Bird:
    def __init__(self, position):
        self.position = position
    def render(self, display, image, camera):
        pygame.draw.rect(display, (0, 100, 0), (camera.correct(self.position.x, 0)[0], camera.correct(0, self.position.y)[1], 16, 16))