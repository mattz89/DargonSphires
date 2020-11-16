""" import pygame, csv, os

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet('players.png').parse_sprite('knight.png')
        self.rect = self.image.get_rect()

    def draw(self, surface):
        display.blit(self.image, (self.rect.x, self.rect.y))

class Knight():
    def __init__(self, filename, spritesheet):
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.sprites = self.load_sprites(filename)
        self.load_map()

    def parse_knight():


    def load_sprites(self, filename):
        tiles = []
        for row in map:
            x = 0
            for tile in row:
                if tile == '-1':
                    pass
                else:
                    tiles.append(Tile(f'floor-{tile}.png', x * self.tile_width, y * self.tile_height, self.spritesheet))
                    x += 1
                    
            y += 1
            z += 1
        
        self.map_width, self.map_height = z * self.tile_width, y * self.tile_height
        print(self.map_width)
        print(self.map_height)
        return tiles """