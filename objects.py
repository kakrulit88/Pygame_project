import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, pos, group, sprite_type, image='rock.png'):
        super().__init__(group)
        self.sprite_type = sprite_type
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos))
        self.hitbox = self.rect.inflate(-10, -30)
