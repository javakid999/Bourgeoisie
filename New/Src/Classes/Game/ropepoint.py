import pygame

class RopePoint:
    def __init__(self, position, locked = False):
        self.position = position
        self.locked = locked
        self.prev_position = position
    def update(self, player):
        if self.locked == False:
            position_before_update = self.position
            self.position = pygame.Vector2.__add__(self.position, pygame.Vector2.__sub__(self.position, self.prev_position))
            self.position = pygame.Vector2.__add__(self.position, pygame.Vector2(0, 0.2))
            if pygame.Rect.collidepoint(player.rect, self.position.x, self.position.y):
                if player.vecocity.x > 1:
                    self.position.x = player.rect.right
                    self.position = pygame.Vector2.__add__(self.position, pygame.Vector2(0.1, 0))
                elif player.velocity.x < 1:
                    self.position.x = player.rect.left
                    self.position = pygame.Vector2.__add__(self.position, pygame.Vector2(-0.1, 0))
            self.prev_position = position_before_update
    def render():
        pass