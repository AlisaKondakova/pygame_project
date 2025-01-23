import pygame
import PIL
from PIL import Image

pygame.init()
w, h = 800, 500
screen = pygame.display.set_mode((w, h))
running = True
loc = pygame.image.load('data/first.png')
im = Image.open('data/first.png')
widloc, heiloc = im.size
loc = pygame.transform.scale(loc, (widloc, h))
loc.convert()
locX = 0
locY = 0
flipX = 0
flip1X = -(widloc-w)
speed = 8
moving = False
to_left = False
to_right = False

while True:
    screen.fill((255, 255, 255))
    pygame.time.delay(30)
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
        flipX += speed
        if locX < -(widloc - w):
            flip1X -= speed
    if to_left is True:
        locX += speed
        flipX -= speed
        flip1X += speed
    if locX > 0:
        screen.blit(loc, (locX - widloc, locY))
    if locX < 0:
        screen.blit(loc, (locX + widloc, locY))
    print(locX)
    screen.blit(loc, (locX, locY))
    pygame.display.update()