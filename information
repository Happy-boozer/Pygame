import pygame

def main():
    pygame.init()
    pygame.font.init()
    size = width, height = 500, 350
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    phrases = ["Эта игра представляет собой", "бродилку/угадайку в которй",
               "Вам предстоит проявить", "смекалку, котороя поможет",
               "проходить уровни бычтрее", "в финале нужны двойные", "клики"]
    text_coords_1 = [0, 0]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for elem in phrases:
            screen.blit(font.render(elem, True, (255, 255, 255)), tuple(text_coords_1))
            text_coords_1[1] += 50

        pygame.display.flip()
    pygame.quit()
