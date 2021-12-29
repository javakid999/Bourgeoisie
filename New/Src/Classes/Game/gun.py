import pygame

class Gun:
    def __init__(self, position):
        self.position = position
        self.gun_vector = pygame.Vector2(0,0)
    def update(self, player, mouse_pos):
        self.position = pygame.Vector2(player.rect.centerx, player.rect.centery)
        self.gun_vector = pygame.Vector2.__mul__(pygame.Vector2(240 - mouse_pos[0], 135 - mouse_pos[1]).normalize(), -15)
    def render(self, display, camera):
        pygame.draw.line(display, (0,255,0), pygame.Vector2(camera.correct(self.position.x,0)[0],camera.correct(0,self.position.y)[1]), pygame.Vector2.__add__(self.gun_vector, pygame.Vector2(camera.correct(self.position.x,0)[0],camera.correct(0,self.position.y)[1])))