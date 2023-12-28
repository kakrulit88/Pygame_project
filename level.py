import pygame
from random import choice
from levels_setting import *
from objects import Object
from player import Player
from hud import *
from enemy import *


class Level():
    def __init__(self):
        self.all_visible_sprites = SpriteGroupWithCamera()
        self.obsticles_sprites = pygame.sprite.Group()
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.surface = pygame.display.get_surface()

        self.pict_slovar = pict_items
        self.player = None

        self.create_map()

        self.hud = HUD(self.player)

    def create_map(self):
        for layout_type, layout in slovar_layouts.items():
            for row_index, row in enumerate(layout):
                for colum_index, colum in enumerate(row):
                    x = colum_index * 64
                    y = row_index * 64

                    if layout_type == 'границы':
                        if layout[row_index][colum_index] == '4':
                            Object((x, y), [self.obsticles_sprites], 'граница')
                    elif layout_type == 'трава':
                        if layout[row_index][colum_index] != '-1':
                            Object((x, y), [self.all_visible_sprites,self.obsticles_sprites, self.attackable_sprites], 'трава',
                                   choice(self.pict_slovar['трава']))
                    if layout_type == 'монстры':
                        if layout[row_index][colum_index] != '-1':
                            Enemy((x, y), [self.all_visible_sprites, self.attackable_sprites], 'bamboo', self.obsticles_sprites)

        self.player = Player((1664, 2368), [self.all_visible_sprites],
                             self.obsticles_sprites, self.all_visible_sprites, self.attack_sprites, self.attackable_sprites)

    def run(self):
        self.all_visible_sprites.custom_draw(self.player)
        self.all_visible_sprites.update_enemy(self.player)
        self.all_visible_sprites.update()

        self.hud.update()



class SpriteGroupWithCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.compensation = [0, 0]
        self.ground_surface = pygame.image.load('data/level_graphics/map.png').convert_alpha()
        self.ground_rect = self.ground_surface.get_rect(topleft=(0, 0))

        self.ground_behind_surface = pygame.image.load('data/level_graphics/map_behind.png').convert_alpha()
        self.ground_behind_rect = self.ground_surface.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.compensation[0] = player.rect.centerx - HEIGHT // 2
        self.compensation[1] = player.rect.centery - WIDTH // 2

        self.ground_rect_pos = (self.ground_rect.topleft[0] - self.compensation[0],
                                self.ground_rect.topleft[1] - self.compensation[1])

        self.ground_behind_rect_pos = (self.ground_behind_rect.topleft[0] - self.compensation[0],
                                       self.ground_behind_rect.topleft[1] - self.compensation[1])

        self.surface.blit(self.ground_surface, self.ground_rect_pos)

        for sprite in sorted(self.sprites(), key=lambda x: x.rect.centery):
            new_pos = (sprite.rect.x - self.compensation[0], sprite.rect.y - self.compensation[1])
            self.surface.blit(sprite.image, new_pos)

        self.surface.blit(self.ground_behind_surface, self.ground_behind_rect_pos)

    def update_enemy(self, player):
        for enemy in self.sprites():
            if enemy.sprite_type == 'enemy':
                enemy.enemy_update(player)
