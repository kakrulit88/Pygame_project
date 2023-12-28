import pygame
from levels_setting import *
from weapon import *
from level import *
from entity import *


class Player(Entity):
    def __init__(self, pos, group, obstical_sprites, all_visible_sprites, attack_sprites, attackable_sprites):
        super().__init__(group)
        self.sprite_type = 'player'

        self.image = pygame.image.load(player_animation['down_idle']).convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos))
        self.hitbox = self.rect.inflate(-10, -5)

        self.stats = {'health': 100, 'speed': 5, 'energy': 75}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.energycooldown = 1500
        self.not_energy_time = 0
        self.energy_heal = False

        self.obstical_sprites = obstical_sprites
        self.all_visible_sprites = all_visible_sprites
        self.attack_sprites = attack_sprites
        self.attackable_sprites = attackable_sprites

        self.attacking = False
        self.attack_cooldown_time = 300
        self.attack_time = pygame.time.get_ticks()
        self.weapon = None

        self.direction = [0, 0]
        self.speed = self.stats['speed']
        self.animation_speed = 0.15
        self.frame_time = 0
        self.animation_direction = player_animation['down_idle']
        self.last_direction = 'down'

    def new_direction(self):
        keys = pygame.key.get_pressed()
        if not self.attacking:
            if keys[pygame.K_w]:
                self.direction[1] = -1
                self.animation_direction = player_animation['up']
                self.last_direction = 'up'
            elif keys[pygame.K_s]:
                self.direction[1] = 1
                self.animation_direction = player_animation['down']
                self.last_direction = 'down'
            else:
                self.direction[1] = 0
                self.animation_direction = player_animation['down_idle']

            if keys[pygame.K_d]:
                self.direction[0] = 1
                self.animation_direction = player_animation['right']
                self.last_direction = 'right'
            elif keys[pygame.K_a]:
                self.direction[0] = -1
                self.animation_direction = player_animation['left']
                self.last_direction = 'left'
            else:
                self.direction[0] = 0

            if (self.direction == [-1, -1] or self.direction == [1, -1]
                    or self.direction == [1, 1] or self.direction == [-1, 1]):
                self.direction = [self.direction[0] * 0.707, self.direction[1] * 0.707]

            self.move(self.speed)

    def animation(self):
        self.frame_time += self.animation_speed
        if self.frame_time > len(self.animation_direction):
            self.frame_time = 0

        if self.animation_direction != player_animation['down_idle']:
            self.image = pygame.image.load(self.animation_direction[int(self.frame_time)]).convert_alpha()
        else:
            self.image = pygame.image.load(player_animation[self.last_direction + '_idle']).convert_alpha()
        self.rect = self.image.get_rect(center=(self.hitbox.center))

    def create_attack(self, keys):
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.weapon = Weapon(self.last_direction, [self.all_visible_sprites, self.attack_sprites], self, 'lance')

        self.attack_cooldown()

    def destroy_attack(self):
        if self.weapon:
            self.weapon.kill()
            self.weapon = None

    def attack_cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown_time:
                self.attacking = False
                self.destroy_attack()

    def energy_cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.energy_heal:
            if current_time - self.not_energy_time >= self.energycooldown:
                self.energy += 0.15
            if self.energy >= self.stats['energy']:
                self.energy_heal = False

    def energy_consumption(self, keys):
        if keys[pygame.K_LSHIFT]:
            if self.energy > 0:
                self.energy -= 0.45
                self.speed = self.stats['speed'] + 1.5
                self.not_energy_time = pygame.time.get_ticks()
            else:
                self.speed = self.stats['speed']
        elif not keys[pygame.K_LSHIFT]:
            self.speed = self.stats['speed']

        if not keys[pygame.K_LSHIFT] and not self.energy_heal:
            self.energy_heal = True
            self.not_energy_time = pygame.time.get_ticks()

        self.energy_cooldown()

    def sprites_attack_interaction(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                spisok_collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if spisok_collision_sprites:
                    for sprite in spisok_collision_sprites:
                        if sprite.sprite_type == 'трава':
                            sprite.kill()
                        else:
                            sprite.get_damage(self)




    def update(self):
        self.new_direction()
        self.create_attack(pygame.key.get_pressed())
        self.sprites_attack_interaction()
        self.energy_consumption(pygame.key.get_pressed())
        self.animation()

