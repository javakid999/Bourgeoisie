import pygame

class RopeStick:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.length = pygame.Vector2.distance_to(a.position, b.position)
    def update(self):
        stick_center = pygame.Vector2.__mul__(pygame.Vector2.__add__(self.a.position, self.b.position), 0.5)
        stick_dir = pygame.Vector2.__sub__(self.a.position, self.b.position).normalize()
        if self.a.locked == False:
            self.a.position = pygame.Vector2.__add__(stick_center, pygame.Vector2.__mul__(pygame.Vector2.__mul__(stick_dir, self.length), 0.5))
        if self.b.locked == False:
            self.b.position = pygame.Vector2.__sub__(stick_center, pygame.Vector2.__mul__(pygame.Vector2.__mul__(stick_dir, self.length), 0.5))
    def render(self, display, color):
        pygame.draw.line(display, color, self.a.position, self.b.position)