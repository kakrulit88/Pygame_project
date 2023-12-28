import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.direction = [0, 0]

    def move(self, speed):
        self.hitbox.x += self.direction[0] * speed
        self.colusion(self.direction, 'x')
        self.hitbox.y += self.direction[1] * speed
        self.colusion(self.direction, 'y')
        self.rect.center = self.hitbox.center

    def colusion(self, direction, space):
        if space == 'x':
            for sprite in self.obstical_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction[0] > 0:
                        self.hitbox.right = sprite.hitbox.left
                    elif direction[0] < 0:
                        self.hitbox.left = sprite.hitbox.right
        elif space == 'y':
            for sprite in self.obstical_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction[1] > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    elif direction[1] < 0:
                        self.hitbox.top = sprite.hitbox.bottom
