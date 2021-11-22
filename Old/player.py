import pygame
class Player:
    def __init__(self, position):
        self.position = position
        self.velocity = pygame.Vector2(0,0)
        self.size = pygame.Vector2(16, 16)
        self.rect = pygame.Rect(self.position, self.size)
    def update(self, tiles, keys, gun_vector):
        if gun_vector == (0,0):
            player_movement = [0,0]
            if keys['right']:
                self.velocity.x += 0.25
            if keys['left']:
                self.velocity.x -= 0.25
            if keys['up']:
                self.velocity.y = -4
            player_movement[1] += self.velocity.y
            player_movement[0] += self.velocity.x

            self.velocity.x *= 0.9
            self.velocity.y += 0.5
            self.rect = self.collide(self.rect, player_movement, tiles)[0]
            self.position.x = self.rect.x
            self.position.y = self.rect.y
        else:
            player_movement = [0, 0]
            self.velocity.y = gun_vector.y * 6
            self.velocity.x = gun_vector.x * 6
            self.rect = self.collide(self.rect, player_movement, tiles)[0]
            self.position.x = self.rect.x
            self.position.y = self.rect.y

    def render(self, display, gun_vector):
        if gun_vector != (0,0):
            pygame.draw.line(display, (0, 255, 0), (300, self.rect.y), (300 + gun_vector[0] * -30, self.rect.y + gun_vector[1] * -30), 3)
        pygame.draw.rect(display, (255,255,0), (300, self.rect.y, self.rect.width, self.rect.height))

    def collision_test(self, tiles):
        hit_list = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def collide(self, rect, movement, tiles):
        collision_types = {'top': False, 'botton': False, 'right': False, 'left': False}

        rect.x += movement[0]
        hit_list = self.collision_test(tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
                movement[0] = 0
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
                movement[0] = 0

        rect.y += movement[1]
        hit_list = self.collision_test(tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
                self.velocity.y = 0
            if movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
                self.velocity.y = 0
        return rect, collision_types