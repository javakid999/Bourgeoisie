import pygame
from Classes.Game.rope import Rope
from Classes.Game.ropepoint import RopePoint
from Classes.Game.ropestick import RopeStick

def generate_rope(length):
    rope = Rope([], [], (0, 150, 0))
    for i in range(length):
      point = RopePoint(pygame.Vector2(100, 40 + i * 10), i == 0)
      rope.points.append(point)
      if i > 0:
        rope.sticks.append(RopeStick(point, rope.points[i - 1]))
    return rope