import pygame, sys
from player import Player
from utils import load_map, get_tiles
pygame.init()

clock = pygame.time.Clock()
resolution = (1280,720)
display = pygame.Surface((480,270))
screen = pygame.display.set_mode(resolution, 0, 32)
pygame.display.set_caption('Bourgeoisie')

keys = {
    'left': False,
    'right': False,
    'up': False,
    'click': False
}

game_map = load_map('Maps/test')
player = Player(pygame.Vector2(135,40))

while True:
    display.fill((200,180,255))

    gun_vector = pygame.Vector2(0,0)
    if keys['click'] == True:
        m_position = pygame.mouse.get_pos()
        m_position = (m_position[0] * 0.375, m_position[1] * 0.375)
        gun_vector = pygame.Vector2(m_position[0] - 300, m_position[1] - player.rect.centery).normalize().__mul__(-1)
        keys['click'] = False

    tiles = get_tiles(game_map, display, player)
    player.update(tiles, keys, gun_vector)
    player.render(display, gun_vector)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys['up'] = True
            if event.key == pygame.K_a:
                keys['left'] = True
            if event.key == pygame.K_d:
                keys['right'] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys['up'] = False
            if event.key == pygame.K_a:
                keys['left'] = False
            if event.key == pygame.K_d:
                keys['right'] = False
        if pygame.mouse.get_pressed(num_buttons=3)[0] == True and event.type == pygame.MOUSEBUTTONDOWN:
            keys['click'] = True

    screen.blit(pygame.transform.scale(display, resolution), (0,0))
    pygame.display.flip()
    clock.tick(60)