import pygame, csv, os

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()

        # Get offsets
        cart_x = x/2
        cart_y = y
        iso_x = (cart_x - cart_y)
        iso_y = (cart_x + cart_y)/2
        centered_x = x/(2**13) + iso_x + 1920/2
        centered_y = y/(2**13) + iso_y

        # Set offsets for rect
        self.rect.x, self.rect.y = centered_x, centered_y
        

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class TileMap():
    def __init__(self, filename, spritesheet):
        self.tile_width = 62
        self.tile_height = 32
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_width, self.map_height))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()


    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))


    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)


    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map


    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y, z = 0, 0, 0
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
        return tiles