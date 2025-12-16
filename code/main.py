from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame

from random import randint

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivor")
        self.running = True
        self.clock = pygame.time.Clock()

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

        # sprites
        self.player = Player((400,300), self.all_sprites, self.collision_sprites)
        

    def setup(self):
        map =load_pygame(join('data', 'maps', 'world.tmx'))
        
        for x,y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x*TILE_SIZE,y *TILE_SIZE), image, self.all_sprites)

        for obj in map.get_layer_by_name('Objects'):
            CollisionSprites((obj.x,obj.y), obj.image, (self.all_sprites, self.collision_sprites))
        
        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprites((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)
    
    def run(self):
        while self.running:
            dt = self.clock.tick()/1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # update
            self.all_sprites.update(dt)

            # draw
            self.WINDOW.fill('black')
            self.all_sprites.draw(self.WINDOW)
            
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()