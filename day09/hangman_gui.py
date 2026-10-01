import os
import random
import sys
import textwrap

import pygame

import hangman

RESOURCES = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
WIDTH = 800
HEIGHT = 600
TIME_LIMIT = 180

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (90, 90, 90)
RED = (200, 40, 40)
GREEN = (40, 150, 60)
SKY = (170, 210, 240)

DIFFICULTIES = {
    "1": ["Easy", 3, 5],
    "2": ["Normal", 6, 8],
    "3": ["Hard", 9, 20],
}


def pick_word(words, difficulty):
    name, shortest, longest = DIFFICULTIES[difficulty]
    choices = []
    for word in words:
        if shortest <= len(word) <= longest:
            choices.append(word)
    if len(choices) == 0:
        choices = words
    return random.choice(choices)


def draw_text(surface, font, text, color, position):
    surface.blit(font.render(text, True, color), position)


def draw_hangman(surface, penalties, color):
    pygame.draw.line(surface, BLACK, (60, 520), (260, 520), 6)
    pygame.draw.line(surface, BLACK, (100, 520), (100, 140), 6)
    pygame.draw.line(surface, BLACK, (100, 140), (220, 140), 6)
    pygame.draw.line(surface, BLACK, (220, 140), (220, 180), 3)
    parts = penalties // 2
    if parts >= 1:
        pygame.draw.circle(surface, color, (220, 210), 30, 3)
    if parts >= 2:
        pygame.draw.line(surface, color, (220, 240), (220, 340), 3)
    if parts >= 3:
        pygame.draw.line(surface, color, (220, 270), (180, 310), 3)
    if parts >= 4:
        pygame.draw.line(surface, color, (220, 270), (260, 310), 3)
    if parts >= 5:
        pygame.draw.line(surface, color, (220, 340), (185, 420), 3)
    if parts >= 6:
        pygame.draw.line(surface, color, (220, 340), (255, 420), 3)


def draw_life_bar(surface, penalties):
    lives = hangman.MAX_PENALTIES + 1 - penalties
    width = 200 * max(0, lives) // (hangman.MAX_PENALTIES + 1)
    pygame.draw.rect(surface, WHITE, (560, 20, 200, 20))
    pygame.draw.rect(surface, GREEN if lives > 4 else RED, (560, 20, width, 20))
    pygame.draw.rect(surface, BLACK, (560, 20, 200, 20), 2)


def draw_menu(surface, fonts, error):
    big, medium, small = fonts
    draw_text(surface, big, "HANGMAN", BLACK, (290, 100))
    draw_text(surface, medium, "Choose a difficulty:", BLACK, (280, 220))
    y = 270
    for key in DIFFICULTIES:
        name, shortest, longest = DIFFICULTIES[key]
        line = key + " - " + name + " (" + str(shortest) + " to " + str(longest) + " letters)"
        draw_text(surface, medium, line, GREY, (280, y))
        y += 45
    draw_text(surface, small, "Esc: quit", GREY, (20, 560))
    if error:
        draw_text(surface, small, error, RED, (20, 420))
        draw_text(surface, small, "Usage: hangman_gui [wordlist.txt]", RED, (20, 450))


def draw_game(surface, fonts, game, typed, message, seconds_left):
    big, medium, small = fonts
    draw_hangman(surface, game["penalties"], BLACK)
    draw_life_bar(surface, game["penalties"])
    draw_text(surface, small, "Lives", BLACK, (500, 22))
    draw_text(surface, medium, "Attempts: " + str(game["attempts"]), BLACK, (20, 20))
    timer_color = RED if seconds_left <= 30 else BLACK
    draw_text(surface, medium, "Time: " + str(seconds_left) + "s", timer_color, (250, 20))
    word_font = big if len(game["secret"]) <= 12 else medium
    draw_text(surface, word_font, hangman.show_word(game), BLACK, (320, 180))
    wrong = " ".join(sorted(game["wrong"]))
    draw_text(surface, small, "Wrong: " + wrong, RED, (320, 260))
    pygame.draw.rect(surface, WHITE, (320, 320, 440, 50))
    pygame.draw.rect(surface, BLACK, (320, 320, 440, 50), 2)
    draw_text(surface, medium, typed + "|", BLACK, (330, 332))
    draw_text(surface, medium, message, GREY, (320, 390))
    draw_text(surface, small, "Enter: guess   Tab: hint   Esc: menu", GREY, (320, 560))


def draw_end(surface, fonts, game, lines):
    big, medium, small = fonts
    won = hangman.is_won(game)
    if won:
        draw_hangman(surface, game["penalties"], BLACK)
    else:
        draw_hangman(surface, hangman.MAX_PENALTIES, RED)
    draw_text(surface, big, "YOU WIN!" if won else "YOU LOSE!", GREEN if won else RED, (320, 60))
    y = 140
    for line in lines:
        draw_text(surface, small, line, BLACK, (320, y))
        y += 30
    draw_text(surface, medium, "Leaderboard", BLACK, (320, 300))
    y = 340
    rank = 1
    for score in hangman.read_scores()[:5]:
        line = str(rank) + ". " + str(score[0]) + " attempts - " + score[2] + " (" + score[1] + ")"
        draw_text(surface, small, line, GREY, (320, y))
        y += 28
        rank += 1
    draw_text(surface, small, "R: play again   Esc: quit", GREY, (320, 560))


def end_lines(game, seconds_left):
    secret = game["secret"]
    if hangman.is_won(game):
        message = hangman.highscore_message(secret, game["attempts"])
        return textwrap.wrap(message, 40)
    if seconds_left <= 0:
        return ["Time is up!", "The word was '" + secret + "'"]
    return ["Too many penalties!", "The word was '" + secret + "'"]


def load_background():
    try:
        image = pygame.image.load(os.path.join(RESOURCES, "assets", "background.png"))
        return pygame.transform.scale(image, (WIDTH, HEIGHT))
    except (pygame.error, OSError):
        return None


def load_word_list():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = os.path.join(RESOURCES, "words.txt")
    try:
        return hangman.load_words(filename), ""
    except ValueError as error:
        return [], "Error: " + str(error)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")
    clock = pygame.time.Clock()
    fonts = [pygame.font.SysFont(None, 64), pygame.font.SysFont(None, 36), pygame.font.SysFont(None, 26)]
    background = load_background()
    words, error = load_word_list()

    page = "menu"
    game = None
    typed = ""
    message = ""
    lines = []
    start = 0
    seconds_left = TIME_LIMIT

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type != pygame.KEYDOWN:
                continue
            elif page == "menu":
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.unicode in DIFFICULTIES and len(words) > 0:
                    game = hangman.new_game(pick_word(words, event.unicode))
                    typed = ""
                    message = "Type a letter or a word, then press Enter"
                    start = pygame.time.get_ticks()
                    page = "game"
            elif page == "game":
                if event.key == pygame.K_ESCAPE:
                    page = "menu"
                elif event.key == pygame.K_RETURN:
                    if typed != "":
                        message = hangman.apply_guess(game, typed)
                        typed = ""
                elif event.key == pygame.K_BACKSPACE:
                    typed = typed[:-1]
                elif event.key == pygame.K_TAB:
                    letter = hangman.suggest_letter(game, words)
                    if letter is None:
                        message = "Hint: try to guess the whole word!"
                    else:
                        message = "Hint: try '" + letter + "'"
                elif hangman.is_letters(event.unicode) and len(typed) < hangman.MAX_WORD_LENGTH:
                    typed += event.unicode.upper()
            elif page == "end":
                if event.key == pygame.K_r:
                    page = "menu"
                elif event.key == pygame.K_ESCAPE:
                    running = False

        if page == "game":
            seconds_left = TIME_LIMIT - (pygame.time.get_ticks() - start) // 1000
            if hangman.is_won(game) or hangman.is_lost(game) or seconds_left <= 0:
                lines = end_lines(game, seconds_left)
                page = "end"

        if background is None:
            screen.fill(SKY)
        else:
            screen.blit(background, (0, 0))
        if page == "menu":
            draw_menu(screen, fonts, error)
        elif page == "game":
            draw_game(screen, fonts, game, typed, message, seconds_left)
        else:
            draw_end(screen, fonts, game, lines)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
