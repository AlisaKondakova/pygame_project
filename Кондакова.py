import pygame
import os
import sys
import PIL
from PIL import Image

pygame.init()

def load_image(name, width, height, color_key=None):
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

def move(name, x, y):
    ch.blit(name, (x, y))


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
widh = 180
heih = 360
widl, heil = get_scr_size('forest.png')
widl = widl // 2
speed = 6
moving = False
to_left = False
to_right = False
to_up = False
to_down = True
locX = 0
locY = 0
loc2X = 0
loc2Y = 0
fps = 40
clock = pygame.time.Clock()
ch = pygame.Surface((800, 600))
loc = load_image('forest.png', widl, h)
loc2 = load_image('forest2.png', w, h, 0)
player_image = load_image('player.png', widh, heih, -1)
player = Player(player_image, w // 6, h // 3)
player2_im = load_image('up.png', 100, 100, -1)
player2 = Player(player2_im, w // 2.5, h // 1.5)
while True:
    screen.fill((255, 255, 255))
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
                to_down = False
            if event.key == pygame.K_DOWN:
                to_down = True
                to_up = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if to_right is True and to_up is False:
        locX -= speed
    if to_left is True and to_up is False:
        locX += speed
    if to_up is True:
        if to_right is True:
            loc2Y += speed
        if to_left is True:
            loc2Y += speed
    if locX > 0 and to_up is False:
        for i in range(1, 20):
            move(loc, locX - (widl * i), locY)
    if locX < 0 and to_up is False:
        for i in range(1, 20):
            move(loc, locX + (widl * i), locY)
    if loc2Y > 0 and to_down is False:
        for i in range(1, 20):
            move(loc2, loc2X, loc2Y - (h * i))
    if not to_up:
        move(loc, locX, locY)
    if not to_down:
        move(loc2, loc2X, loc2Y)
    screen.blit(ch, (0, 0))
    sprite_group.draw(screen)
    hero_group.draw(screen)
    pygame.display.flip()