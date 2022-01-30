import pygame
import os
import sys
import final
import diversion_3



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


class Scene:
    def __init__(self, screen, time):
        self.screen = screen
        self.time = time

    def render(self):
        thickness = 0
        color = (249, 104, 21)
        coords_1 = (300, 0, 100, 100)
        coords_2 = (300, 200, 100, 100)
        coords_3 = (300, 400, 100, 100)

        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, color, coords_1, thickness)
        pygame.draw.rect(self.screen, color, coords_2, thickness)
        pygame.draw.rect(self.screen, color, coords_3, thickness)
        font = pygame.font.Font(None, 50)
        text_1 = font.render(f'время игры{round(self.time / 22500, 2)}',
                             True, (249, 104, 21))
        self.screen.blit(text_1, (0, 450))


def main(time):
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    hero_image = load_image('mar.png')
    hero = pygame.sprite.Sprite(all_sprites)
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    dist = 10
    running = True
    time = round(time / 22500, 2)
    while running:
        time += int(pygame.time.get_ticks() / 1000)
        for event in pygame.event.get():
            check_x = 0
            check_y = 0
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if key[pygame.K_s]:
                hero.rect.top += dist
                check_x = list(hero.rect)[0]
                check_y = list(hero.rect)[1]
            elif key[pygame.K_w]:
                hero.rect.top -= dist
                check_x = list(hero.rect)[0]
                check_y = list(hero.rect)[1]
            if key[pygame.K_d]:
                hero.rect.left += dist
                check_x = list(hero.rect)[0]
                check_y = list(hero.rect)[1]
            elif key[pygame.K_a]:
                hero.rect.left -= dist
                check_x = list(hero.rect)[0]
                check_y = list(hero.rect)[1]
            if check_x > 310 and 199 > check_y > 100:
                final.main(time)
            if check_x > 310 and 400 > check_y > 300:
                diversion_3.main(time)
        Scene(screen, time).render()
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main(0)
