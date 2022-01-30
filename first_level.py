import pygame
import os
import sys
import second_level


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
    def __init__(self, screen, flag, time):
        self.screen = screen
        self.flag = flag
        self.time = time

    def render(self):
        font = pygame.font.Font(None, 50)
        text_1 = font.render("Выйди", True, (0, 0, 0))
        text_2 = font.render("и зайди", True, (0, 0, 0))
        text_3 = font.render("с уважением", True, (0, 0, 0))
        text_coords_1 = (0, 350)
        text_coords_2 = (0, 400)
        text_coords_3 = (0, 450)
        rect_for_text_coords = (0, 300, 200, 200)
        coords_1 = (200, 0, 200, 200)
        coords_2 = (200, 300, 200, 200)
        thickness = 0
        color = (255, 0, 0)
        color_2 = (128, 255, 0)
        text_color = (0, 0, 0)
        self.screen.fill((200, 150, 210))
        pygame.draw.rect(self.screen, color, coords_1, thickness)
        pygame.draw.rect(self.screen, color, coords_2, thickness)
        font = pygame.font.Font(None, 50)
        text_1 = font.render(f'время игры{round(self.time / 22500, 2)}',
                             True, (0, 0, 0))
        self.screen.blit(text_1, (0, 250))
        if self.flag is True:
            pygame.draw.rect(self.screen, color_2, rect_for_text_coords, thickness)
            self.screen.blit(text_1, text_coords_1)
            self.screen.blit(text_2, text_coords_2)
            self.screen.blit(text_3, text_coords_3)


def main():
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
    dist = 10
    clock = pygame.time.Clock()
    shift_flag = False
    running = True
    Flag = False
    time_0 = 0
    while running:
        time_0 += int(pygame.time.get_ticks() / 1000)
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

            if check_x >= 340 and 221 > check_y > 199 and Flag is False:
                Flag = True
                Scene(screen, Flag, time_0).render()
            if event.type == pygame.KEYDOWN or pygame.KEYUP:
                if key[pygame.K_f]:
                    shift_flag = True
            if check_x >= 340 and 221 > check_y > 199 and Flag and shift_flag:
                second_level.main(time_0)

        Scene(screen, Flag, time_0).render()
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()
    

if __name__ == '__main__':
    main()