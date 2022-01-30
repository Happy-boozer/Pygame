import pygame
import os
import sys
import second_level
import Game_over


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

def caller(time):
    Game_over.main(time)

class Scene:
    def __init__(self, screen, flag_1, flag_2, flag_3, time):
        self.screen = screen
        self.flag_1 = flag_1
        self.flag_2 = flag_2
        self.flag_3 = flag_3
        self.time = time
        self.rect_1 = pygame.Rect((300, 0, 200, 100))

    def render(self):
        points_t = [(0, 500), (100, 300), (200, 500)]
        coords_0 = (300, 0, 200, 100)
        coords_1 = (200, 0, 200, 200)
        coords_2 = (200, 300, 200, 200)
        thickness = 0
        color = (255, 0, 0)
        color_2 = (128, 255, 0)
        self.screen.fill((200, 20, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect_1, thickness)
        pygame.draw.polygon(self.screen, (0, 0, 0), points_t, thickness)
        pygame.draw.circle(self.screen, (0, 0, 0), (400, 400), 100, 0)
        if self.flag_1 and self.flag_2 and self.flag_3:
            pygame.draw.rect(self.screen, (124, 252, 0), self.rect_1, thickness)
            pygame.draw.polygon(self.screen, (124, 252, 0), points_t, thickness)
            pygame.draw.circle(self.screen, (124, 252, 0), (400, 400), 100, 0)
            return True
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), self.rect_1, thickness)
            pygame.draw.polygon(self.screen, (0, 0, 0), points_t, thickness)
            pygame.draw.circle(self.screen, (0, 0, 0), (400, 400), 100, 0)


def main(time):
    pygame.init()
    pygame.font.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    all_sprites = pygame.sprite.Group()
    hero_image = load_image('mar.png')
    hero = pygame.sprite.Sprite(all_sprites)
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    global flag_1
    flag_1 = False
    global flag_T
    flag_T = False
    global flag_C
    flag_C = False
    dist = 10
    running = True
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
            all_sprites.draw(screen)
            if 300 < check_x and 0 < check_y <= 100 or (event.type == pygame.MOUSEBUTTONDOWN and
                                                        300 < event.pos[0] and
                                                        0 < event.pos[1] <= 100):
                flag_1 = True
            if 0 < check_x < 200 and 300 <= check_y <= 500 or (event.type == pygame.MOUSEBUTTONDOWN and
                                                               0 < event.pos[0] < 200 and
                                                               300 < event.pos[1] <= 500):
                flag_T = True
            if 300 <= check_x <= 500 and 400 <= check_y <= 500 or (event.type == pygame.MOUSEBUTTONDOWN and
                                                                   300 < event.pos[0] < 500 and
                                                                   400 < event.pos[1] <= 500):
                flag_C = True
            if Scene(screen, flag_1, flag_T, flag_C, time).render():
                caller(time)
        Scene(screen, flag_1, flag_T, flag_C, time).render()
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main(0)
