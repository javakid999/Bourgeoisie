import pygame

class Player:
    def __init__(self, position):
        size = pygame.Vector2(16,16)
        self.rect = pygame.Rect(position, size)
        self.velocity = pygame.Vector2(0,0)
        self.movement = [0,0]
        self.air_time = 0

    def collide_tiles(self, tiles):
        hit_list = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hit_list.append(tile)
        return [hit_list, hit_list == []]

    def render(self, display, camera):
        pygame.draw.rect(display, (255,0,0), (camera.correct(self.rect.left, self.rect.top)[0], camera.correct(self.rect.left, self.rect.top)[1], 16, 16))

    def collide(self, tiles):
        collision_types = {'left': False, 'right': False, 'top': False, 'bottom': False}
        rect = self.rect

        rect.x += self.movement[0]
        hit_list = self.collide_tiles(tiles)[0]
        for tile in hit_list:
            if self.movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
            elif self.movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True

        rect.y += self.movement[1]
        hit_list = self.collide_tiles(tiles)[0]
        for tile in hit_list:
            if self.movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
                self.velocity.y = 0
                self.air_time = 0
            elif self.movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
                self.velocity.y = 0
                self.air_time = 0
                
        return collision_types, rect

    def update(self, keys, tiles):
        self.movement = [0.0, 0.0]
        if keys['left']:
            self.velocity.x -= 0.2
        if keys['right']:
            self.velocity.x += 0.2
        if keys['up'] and self.air_time < 5:
            self.velocity.y = -4
        self.movement = [self.movement[0] + self.velocity.x, self.movement[1] + self.velocity.y]
        
        if self.collide_tiles(tiles)[1]:
            self.air_time += 1

        self.velocity.y += 0.5
        self.velocity.x *= 0.9
        self.movement[0] = round(self.movement[0])
        self.velocity.x = round(self.velocity.x * 100) / 100
        self.rect = self.collide(tiles)[1]