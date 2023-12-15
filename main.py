import os
import sys

import pygame


class GameOver(pygame.sprite.Sprite):
    def __init__(self, *group, size=(600, 300), fps=60):
        super().__init__(*group)
        self.image = load_image('gameover.png', -1)
        self.rect = self.image.get_rect()
        self.rect.x = -1200
        self.rect.y = 0
        self.n = 1000
        self.fps = fps
        self.step = self.n / fps
        self.size = size

    def update_pos(self):
        if self.rect.x < -self.step:
            self.rect.x += self.step
        else:
            self.rect.x = 0


class MyGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update_position(self):
        for sprite in self.sprites():
            sprite.update_pos()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


screen = pygame.display.set_mode((600, 300))
running = True
my_group = MyGroup()
GameOver(my_group)
clock = pygame.time.Clock()
FPS = 60
while running:
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    my_group.update_position()
    my_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
