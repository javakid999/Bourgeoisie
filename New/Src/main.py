import pygame, sys

from pygame import mouse
from Classes.Game.player import Player
from Classes.Game.gun import Gun
from Utils.loadmap import load_map, transcribe_map, render_map, get_tiles
from Utils.ropetools import generate_rope
from Classes.Game.camera import Camera
from Classes.UI.screen import Screen
pygame.init()

clock = pygame.time.Clock()
resolution = (1280,720)
internal_resolution = (480,270)
display = pygame.Surface(internal_resolution)
camera = Camera(pygame.Vector2(100,20))
screen = pygame.display.set_mode(resolution, 0, 32)
pygame.display.set_caption('Bourgeoisie')

keys = {
    'left': False,
    'right': False,
    'up': False,
    'click': False
}

player = Player(pygame.Vector2(100,20))
gun = Gun(pygame.Vector2(100,20))
rope = generate_rope(10)
assets = {'bird': 0,}
menu = Screen(0, {}, 'd:\\Bourgeoisie\\New\\Maps\\empty')
level1 = Screen(1, {'player': player, 'gun': gun}, 'd:\\Bourgeoisie\\New\\Maps\\test')

while True:
    display.fill((200,180,255))
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = (mouse_pos[0] * (internal_resolution[0] / resolution[0]), mouse_pos[1] * (internal_resolution[1] / resolution[1]))
    level1.update(keys, mouse_pos, camera)
    level1.render(display, assets, camera)
    rope.update(player)
    rope.render(display, camera)

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