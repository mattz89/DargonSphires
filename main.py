from tiles import *
from spritesheet import SpriteSheet

# Load up window
pygame.init()
DISPLAY_WIDTH, DISPLAY_HEIGHT = 2976, 1536
canvas = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
window = pygame.display.set_mode(((DISPLAY_WIDTH, DISPLAY_HEIGHT)))
running = True
clock = pygame.time.Clock()


# Load all spritesheets
tileset = SpriteSheet('floor.png')
players = SpriteSheet('players.png')
# For when players added
#player_img = players.parse_sprite('name.png')
#player_rect = player_img.get_rect()



# Load the map
map1 = TileMap('map1_tile.csv', tileset)
# For when players added
#player_rect.x, player_rect.y = map.start_x, map.start_y

# Game loop
while running: 
    clock.tick(30)

    # Check for player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass


    # Update window and display
    #canvas.fill((0, 180, 240))
    map1.draw_map(canvas)
    # For when players added
    #canvas.blit(player_img, player_rect)
    window.blit(canvas, (0, 0))
    pygame.display.update()