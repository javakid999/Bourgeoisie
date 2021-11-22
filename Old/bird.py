import pygame

class Bird:
    def __init__(self, position, image):
        self.position = position
        self.image = image
    def render(self, display):
        display.blit(self.image, self.position)