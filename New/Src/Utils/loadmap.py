import pygame
from Classes.Game.bird import Bird

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

def transcribe_map(map):
    transcribed_map = map
    for i, row in enumerate(map):
        for j, tile in enumerate(row):
            if map[i][j] == '1':
                transcribed_map[i][j] = '1'
            if map[i][j] == 'b':
                transcribed_map[i][j] = Bird(pygame.Vector2(j * 16, i * 16))
    return transcribed_map

def render_map(display, tmap, assets):
    for i, row in enumerate(tmap):
        for j, tile in enumerate(row):
            if tmap[i][j] == '1':
                pygame.draw.rect(display, (0,0,0), pygame.Rect(j * 16, i * 16, 16, 16))
            if isinstance(tmap[i][j], Bird):
                tmap[i][j].render(display, assets['bird'])

def get_tiles(map):
    tile_rects = []

    for i, row in enumerate(map):
        for j, tile in enumerate(row):
            if map[i][j] == '1':
                tile_rects.append(pygame.Rect(j * 16, i * 16, 16, 16))
    return tile_rects