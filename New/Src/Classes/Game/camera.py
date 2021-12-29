import pygame

class Camera:
    def __init__(self, center):
        self.position = pygame.Vector2(center.x - 240, center.y - 135)
    def update(self, player):
        self.position = pygame.Vector2(player.rect.x - 240, player.rect.y - 135)
    def correct(self, obj_x, obj_y):
        return [obj_x - self.position.x, obj_y - self.position.y]