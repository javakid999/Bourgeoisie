import pygame
from bird import Bird

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

def get_tiles(map, display, player):
    tile_rects = []

    for i, row in enumerate(map):
        for j, tile in enumerate(row):
            if map[i][j] == '1':
                tile_rects.append(pygame.Rect(j * 16, i * 16, 16, 16))
                pygame.draw.rect(display, (0,0,0), pygame.Rect((j * 16) - player.position.x + 300, i * 16, 16, 16))
            if map[i][j] == 'b':
                display.blit(pygame.image.load('Assets/bird.png'), ((j * 16) - player.position.x + 300, i * 16))
    return tile_rects