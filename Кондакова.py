import pygame
import os
import sys
import PIL
from PIL import Image

pygame.init()

def for_moving_scr(name):
    fullname = os.path.join('data', name)
    try:
        location = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    wid, hei = get_scr_size(name)
    location = pygame.transform.scale(location, (wid // 2, h))
    location = location.convert()
    return location

def load_character_image(name, width, height, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    wid = width
    hei = height
    image = pygame.transform.scale(image, (wid, hei))
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image

def get_scr_size(name):
    loc = Image.open('data/' + name)
    wloc, hloc = loc.size
    return wloc, hloc

class SpriteGroup(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def get_event(self, event):
        for inet in self:
            inet.get_event(event)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.rect = None

    def get_event(self, event):
        pass

class Player(Sprite):
    def __init__(self, name, pos_x, pos_y):
        super().__init__(hero_group)
        self.image = name
        self.rect = self.image.get_rect().move(pos_x, pos_y)


sprite_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
running = True
locX = 0
locY = 0
widh = 180
heih = 360
widl, heil = get_scr_size('forest.png')
widl = widl // 2
speed = 6
moving = False
to_left = False
to_right = False
loc = for_moving_scr('forest.png')
while True:
    screen.fill((255, 255, 255))
    player_image = load_character_image('player.png', widh, heih, -1)
    owl = Player(player_image, w // 6, h // 3)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if to_right is True:
        locX -= speed
    if to_left is True:
        locX += speed
    if locX > 0:
        for i in range(1, 10):
            screen.blit(loc, (locX - (widl * i), locY))
    if locX < 0:
        for i in range(1, 10):
            screen.blit(loc, (locX + (widl * i), locY))
    screen.blit(loc, (locX, locY))
    sprite_group.draw(screen)
    hero_group.draw(screen)
    pygame.display.update()