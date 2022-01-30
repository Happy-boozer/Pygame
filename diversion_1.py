import pygame
import os
import sys

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

pygame.init()
pygame.font.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        a = 0
        line = mapFile.read().splitlines()
        return list(line)
        #return [line.strip() for line in mapFile]
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')
tile_width = tile_height = 50
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

def generate_level(level):
    #print(type(level))
    for i in level:
        #print(level)
        #print(type(i))
        #print(i[35])
        y = level.index(i)
        print(y)
        for t in list(i):
            #y = level.index(i)

            #print(t)
            #x, y = i.index(t), level.index(i),
            #print(x)
            #print(y)
            """
            if t == '0':
                hero_image = tile_images['wall']
                screen.blit(hero_image, tuple([x, y]))

            elif t == '1':
                her_image = tile_images['empty']
                screen.blit(her_image, tuple([x, y]))
"""
'''             
            for x in range(len(i)):
                if i[x] == '0':
                    return tile_images['wall']
                    #Tile('empty', x, y)
                elif i[x] == '1':
                    return tile_images['empty']
                    #Tile('wall', x, y)

    # вернем игрока, а также размер поля в клетках
    #return x, y
'''
for elem in load_level('3_level.txt'):
    pass
   #print(generate_level(elem))
    #print(list(elem))

def main():
    #level_x, level_y = generate_level(load_level('3_level.txt'))
    print(load_level('3_level.txt'))
    (generate_level(load_level('3_level.txt')))
    running = True
    while running:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if key[pygame.K_DOWN]:
                pass
            elif key[pygame.K_UP]:
                pass
            if key[pygame.K_RIGHT]:
                level_x += 10
        tiles_group.draw(screen)
        all_sprites.draw(screen)
        #player_group.draw(screen)
        pygame.display.flip()


    pygame.quit()
if __name__ == '__main__':
    main()