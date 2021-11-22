import pygame, sys

from pygame import mouse
from Classes.Game.player import Player
from Classes.Game.gun import Gun
from Utils.loadmap import load_map, transcribe_map, render_map, get_tiles
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

map = load_map('D:\Bourgeoisie\\New\Maps\\test')
tmap = transcribe_map(map)
player = Player(pygame.Vector2(100,20))
gun = Gun(pygame.Vector2(100,20))

while True:
    display.fill((200,180,255))
    tiles = get_tiles(map)
    mouse_pos = pygame.mouse.get_pos()
    render_map(display, tmap, {'bird':0})
    player.update(keys, tiles)
    gun.update(player, (mouse_pos[0], mouse_pos[1]))
    player.render(display)
    gun.render(display)

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