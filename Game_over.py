import pygame
import os
import sys
import start_menu
import first_level

def main(time):
    pygame.font.init()
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((0, 8, 2))
    pygame.draw.rect(screen, (124, 252, 0), (50, 350, 150, 100), 0)
    pygame.draw.rect(screen, (249, 104, 21), (250, 350, 150, 100), 0)
    font = pygame.font.Font(None, 50)
    screen.blit(font.render('В меню', True, (0, 0, 0)), (50, 350))
    screen.blit(font.render('Рестарт', True, (0, 0, 0)), (250, 350))
    running = True
    time = round(time / 22500, 2)
    while running:
        screen.blit(font.render(f'Вы играли {time} спецсек', True, (255, 255, 255)), (50, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and 50 < event.pos[0] < 200\
                    and 350 < event.pos[1] < 450:
                start_menu.main()
            if event.type == pygame.MOUSEBUTTONDOWN and 250 < event.pos[0] < 400\
                    and 350 < event.pos[1] < 450:
                first_level.main()


        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main(0)