import pygame
from levels_setting import *
from entity import *


class Enemy(Entity):
    def __init__(self, pos, groups, monster_name, obstical_sprites):
        super().__init__(groups)
        self.monster_name = monster_name
        self.sprite_type = 'enemy'

        self.image = pygame.image.load(monsters[self.monster_name]['idle'][0])
        self.rect = self.image.get_rect(topleft=(pos))
        self.hitbox = self.rect.inflate(-20, -20)

        self.obstical_sprites = obstical_sprites

        self.health = monsters[self.monster_name]['health']
        self.damage = monsters[self.monster_name]['damage']
        self.speed = monsters[self.monster_name]['speed']
        self.resistance = monsters[self.monster_name]['resistance']
        self.type_attack = monsters[self.monster_name]['type_attack']
        self.attack_radius = monsters[self.monster_name]['attack_radius']
        self.notice_radius = monsters[self.monster_name]['notice_radius']
        self.enemy_attack_cooldown = monsters[self.monster_name]['attack_cooldown']

        self.collision_timer = True
        self.collision_timer_cooldown = 300
        self.hit_time = 0

        self.frame_time = 0
        self.animation_speed = 0.10

        self.attack_possible = True
        self.attack_time = None
        self.direction = None
        self.distance = None

    def enemy_update(self, player):
        enemy_vect = pygame.math.Vector2(self.rect.center)
        player_vect = pygame.math.Vector2(player.rect.center)
        self.distance = (player_vect - enemy_vect).magnitude()

        if self.distance > 0:
            self.direction = (player_vect - enemy_vect).normalize()
        else:
            self.direction = pygame.math.Vector2()

        if self.distance <= self.attack_radius and self.attack_possible:
            self.action = 'attack'
            self.attack_possible = False
            self.attack_time = pygame.time.get_ticks()


        elif self.distance <= self.notice_radius:
            self.action = 'move_to_player'
        else:
            self.action = 'idle'
            self.direction = pygame.math.Vector2()

    def animate(self):
        self.frame_time += self.animation_speed
        if self.frame_time >= len(monsters[self.monster_name]['idle']):
            self.frame_time = 0

        self.image = pygame.image.load(monsters[self.monster_name]['idle'][int(self.frame_time)]).convert_alpha()
        self.rect = self.image.get_rect(center=(self.hitbox.center))

    def attack_cooldown(self):
        if not self.attack_possible:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.enemy_attack_cooldown:
                self.attack_possible = True

    def colusion_cooldown(self, hit_time):
        if not self.collision_timer:
            current_time = pygame.time.get_ticks()
            if current_time - hit_time >= self.collision_timer_cooldown:
                self.collision_timer = True

    def repulsion(self):
        if not self.collision_timer:
            self.direction *= -self.resistance

    def get_damage(self, player):
        if self.collision_timer:
            self.health -= player.weapon.damage

            self.hit_time = pygame.time.get_ticks()
            self.collision_timer = False
        print(self.health)

    def check_death(self):
        if self.health <= 0:
            self.kill()

    def update(self):
        self.check_death()
        self.repulsion()
        self.move(self.speed)
        self.animate()
        self.attack_cooldown()
        self.colusion_cooldown(self.hit_time)
