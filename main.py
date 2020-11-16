from tiles import *
from playerss import PlayerSS
from spritesheet import SpriteSheet
from random import randint

# Load up window
pygame.init()
DISPLAY_WIDTH, DISPLAY_HEIGHT = 1920, 1280
window = pygame.display.set_mode(((DISPLAY_WIDTH, DISPLAY_HEIGHT)))
canvas = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('DargonSphires')
running = True
clock = pygame.time.Clock()
TARGET_FPS = 60

# Load all spritesheets
tileset = SpriteSheet('floor.png')
players = 'player.gif'

# Parse player sheet for knight
x = 0
y = 0
vel = 16
character_sheet = PlayerSS(players)
knight = {1: [1, 1, 44, 55], 2: [46, 1, 41, 56], 3: [88, 1, 43, 56], 
              4: [132, 1, 43, 54], 5: [176, 1, 43, 54], 6: [220, 1, 43, 55], 
              7: [264, 1, 45, 56], 8: [310, 1, 49, 56], 9: [360, 1, 62, 54], 
              10: [423, 1, 58, 54], 11: [1, 58, 42, 54], 12: [44, 58, 40, 54], 
              13: [85, 58, 41, 54], 14: [127, 58, 43, 53], 15: [171, 58, 43, 52], 
              16: [215, 58, 47, 54], 17: [263, 58, 42, 54], 18: [306, 58, 44, 54], 
              19: [351, 58, 52, 53], 20: [404, 58, 62, 52], 21: [1, 113, 47, 54], 
              22: [49, 113, 47, 55]}
for i in knight:
    knight[i] = character_sheet.image_at(knight[i], -1).convert_alpha()
#tems = SpriteSheet('items.png')
# For when players added
#player_img = players.parse_sprite('name.png')
#player_rect = player_img.get_rect()



# Load the map and players
map1 = TileMap('map1_tile.csv', tileset)
player = knight[3]

#map1_items = TileMap('map1_item.csv', items)
# For when players added
#player_rect.x, player_rect.y = map.start_x, map.start_y

# Game loop
while running: 
    dt = clock.tick(30) * .001 * TARGET_FPS

    # Check for player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                x -= vel
                y -= vel
                left = randint(11, 13)
                player = knight[left]
                direction = 'left'

            if keys[pygame.K_RIGHT]:
                x += vel
                y += vel
                right = randint(6, 8)
                player = knight[right]
                direction = 'right'

            if keys[pygame.K_UP]:
                y -= vel
                x += vel
                up = randint(16, 18)
                player = knight[up]
                direction = 'up'

            if keys[pygame.K_DOWN]:
                y += vel
                x -= vel
                down = randint(1, 3)
                player = knight[down]
                direction = 'down'

            if keys[pygame.K_TAB]:
                if direction == 'down':
                    attack = randint(4, 5)
                    player = knight[attack]
                elif direction == 'up':
                    attack = randint(19, 20)
                    player = knight[attack]
                elif direction == 'left':
                    attack = randint(14, 15)
                    player = knight[attack]
                elif direction == 'right':
                    attack = randint(9, 10)
                    player = knight[attack]




    # Update window and display
    canvas.fill((0, 0, 0))
    map1.draw_map(canvas)
    position = player.get_rect()
    position = position.move(x, y)
    #map1_items.draw_map(canvas)
    # For when players added
    #canvas.blit(player_img, player_rect)
    canvas.blit(player, position)
    window.blit(canvas, (0, 0))
    pygame.display.update()