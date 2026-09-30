import os
import pygame

BLACK = (0, 0, 0)


def draw_stickman(surface):
    pygame.draw.circle(surface, BLACK, (300, 300), 30, 3)
    pygame.draw.line(surface, BLACK, (300, 330), (300, 430), 3)
    pygame.draw.line(surface, BLACK, (300, 360), (250, 400), 3)
    pygame.draw.line(surface, BLACK, (300, 360), (350, 400), 3)
    pygame.draw.line(surface, BLACK, (300, 430), (260, 520), 3)
    pygame.draw.line(surface, BLACK, (300, 430), (340, 520), 3)


pygame.init()
screen = pygame.display.set_mode((600, 600))

folder = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(folder, "assets", "background.png"))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    draw_stickman(screen)
    pygame.display.flip()

pygame.quit()
