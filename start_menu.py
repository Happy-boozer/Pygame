import pygame
import first_level
import information




clock = pygame.time.Clock

def main():
    pygame.init()
    pygame.font.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    color_1 = (177, 255, 0)
    coords_1 = (100, 100, 300, 100)
    color_2 = (0, 128, 128)
    coords_2 = (100, 300, 310, 100)
    font = pygame.font.Font(None, 50)
    text_1 = font.render("Начать Игру", True, (210, 50, 10))
    text_2 = font.render("получить справку", True, (255, 69, 0))
    screen_2 = pygame.Surface(screen.get_size())


    running = True
    while running:
        for event in pygame.event.get():
            pygame.draw.rect(screen_2, color_1, coords_1, 0)
            pygame.draw.rect(screen_2, color_2, coords_2, 0)
            screen_2.blit(text_2, (105, 330))
            screen_2.blit(text_1, (130, 150))
            screen.blit(screen_2, (0, 0))
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if 400 >= x >= 100 and 200 >= y >= 100:
                    first_level.main()
                if 400 >= x >= 100 and 400 >= y >= 300:
                    information.main()
            # проверка нажатия кнопки (строки 39 - 41)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()