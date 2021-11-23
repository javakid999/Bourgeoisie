import pygame

class Gun:
    def __init__(self, position):
        self.position = position
        self.gun_vector = pygame.Vector2(0,0)
    def update(self, player, mouse_pos):
        self.position = pygame.Vector2(player.rect.centerx, player.rect.centery)
        self.gun_vector = pygame.Vector2.__mul__(pygame.Vector2(player.rect.centerx - mouse_pos[0], player.rect.centery - mouse_pos[1]).normalize(), -15)
    def render(self, display):
        pygame.draw.line(display, (0,255,0), self.position, pygame.Vector2.__add__(self.gun_vector, self.position))