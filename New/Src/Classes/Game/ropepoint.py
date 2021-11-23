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
            self.position = pygame.Vector2.__add__(self.position, pygame.Vector2(0, 0.03))
            if pygame.Rect.collidepoint(player.rect, self.position.x, self.position.y):
                if player.velocity.x > 0:
                    self.position.x = player.rect.right
                    self.position = pygame.Vector2.__add__(self.position, pygame.Vector2(0.1, 0))
                elif player.velocity.x < 0:
                    self.position.x = player.rect.left
                    self.position = pygame.Vector2.__add__(self.position, pygame.Vector2(-0.1, 0))
                self.prev_position = self.position
            else:
              self.prev_position = position_before_update
    def render(self, display):
        if self.locked:
          pygame.draw.circle(display, (255, 255, 0), self.position, 3)
        else:
          pygame.draw.circle(display, (255, 0, 0), self.position, 3)