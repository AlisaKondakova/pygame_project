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
        super().__init__(first_g)
        self.image = name
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def move(self, x, y):
        self.rect = self.image.get_rect().move(x, y)


class PlayerAn(Sprite):
    def __init__(self, size, center):
        super().__init__(first_g)
        self.anim = list()
        for i in range(1, 9):
            self.anim.append(load_image(('0' + str(i) + '.png'), widh, heih))
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.fr = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 200

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.fr += 1
            if self.fr == len(self.anim):
                self.fr = 0
            self.image = self.anim[self.fr]

    def rev(self):
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.flip(self.image, False, True)



sprite_group = pygame.sprite.Group()
first_g = pygame.sprite.Group()
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
player_image = load_image('01.png', widh, heih, -1)
player = PlayerAn((180, 360), (w // 5, h // 1.5))
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
    if to_down is True:
        if to_right or to_left:
            player.update()
        p2x = w // 2
        p2y = h // 1.5
        player2.move(p2x, p2y)
        if to_right is True:
            mov = 1
            locX -= speed
        if to_left is True:
            locX += speed
    if to_up is True:
        if to_right is True:
            loc2Y += speed
            if p2x <= 500:
                p2x += speed
                player2.move(p2x, p2y)
        if to_left is True:
            loc2Y += speed
            if p2x >= 200:
                p2x -= speed
                player2.move(p2x, p2y)
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
        player2.remove(first_g)
        player.add(first_g)
        move(loc, locX, locY)
    if not to_down:
        player.remove(first_g)
        player2.add(first_g)
        move(loc2, loc2X, loc2Y)
    screen.blit(ch, (0, 0))
    sprite_group.draw(screen)
    first_g.draw(screen)
    pygame.display.flip()