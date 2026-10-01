import datetime
import os
import random
import sys

if getattr(sys, "frozen", False):
    FOLDER = os.path.dirname(sys.executable)
else:
    FOLDER = os.path.dirname(os.path.abspath(__file__))
HIGHSCORE_FILE = os.path.join(FOLDER, "highscore.txt")

MAX_FILE_SIZE = 10000000
MAX_WORD_LENGTH = 20
MAX_PENALTIES = 12


def is_letters(text):
    return text.isascii() and text.isalpha()


def load_words(filename):
    try:
        with open(filename, encoding="utf-8-sig") as file:
            content = file.read(MAX_FILE_SIZE + 1)
    except (OSError, UnicodeDecodeError, ValueError):
        raise ValueError("cannot read file '" + filename + "'")
    if len(content) > MAX_FILE_SIZE:
        raise ValueError("file '" + filename + "' is too big")
    words = []
    for line in content.splitlines():
        word = line.strip().upper()
        if is_letters(word) and len(word) <= MAX_WORD_LENGTH:
            words.append(word)
    if len(words) == 0:
        raise ValueError("no valid word in '" + filename + "'")
    return words


def new_game(secret):
    return {
        "secret": secret,
        "revealed": set(),
        "wrong": set(),
        "penalties": 0,
        "attempts": 0,
    }


def show_word(game):
    display = ""
    for letter in game["secret"]:
        if letter in game["revealed"]:
            display += letter + " "
        else:
            display += "_ "
    return display


def penalty_text(penalties):
    if penalties <= 1:
        return str(penalties) + " penalty"
    return str(penalties) + " penalties"


def apply_guess(game, guess):
    guess = guess.strip().upper()
    if not is_letters(guess) or len(guess) > MAX_WORD_LENGTH:
        return "Letters only"
    if guess in game["revealed"]:
        return "Already found"
    if guess in game["wrong"]:
        return "Already tried"
    game["attempts"] += 1
    secret = game["secret"]
    if len(guess) == 1:
        if guess in secret:
            game["revealed"].add(guess)
            return "Found " + str(secret.count(guess)) + " '" + guess + "'"
        game["wrong"].add(guess)
        game["penalties"] += 1
        return "No '" + guess + "' found"
    if guess == secret:
        game["revealed"] = set(secret)
        return "correct guess"
    game["wrong"].add(guess)
    game["penalties"] += 5
    game["revealed"] = set()
    return "incorrect guess"


def is_won(game):
    for letter in game["secret"]:
        if letter not in game["revealed"]:
            return False
    return True


def is_lost(game):
    return game["penalties"] > MAX_PENALTIES


def matches(word, game):
    if len(word) != len(game["secret"]) or word in game["wrong"]:
        return False
    for i in range(len(word)):
        letter = game["secret"][i]
        if letter in game["revealed"] and word[i] != letter:
            return False
        if letter not in game["revealed"] and word[i] in game["revealed"]:
            return False
        if word[i] in game["wrong"]:
            return False
    return True


def suggest_letter(game, words):
    counts = {}
    for word in words:
        if matches(word, game):
            for letter in set(word):
                if letter not in game["revealed"]:
                    counts[letter] = counts.get(letter, 0) + 1
    best = None
    for letter in counts:
        if best is None or counts[letter] > counts[best]:
            best = letter
    return best


def read_scores():
    try:
        with open(HIGHSCORE_FILE, encoding="utf-8") as file:
            lines = file.read(MAX_FILE_SIZE).splitlines()
    except (OSError, UnicodeDecodeError):
        return []
    scores = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) != 3 or not parts[0].isdigit():
            continue
        try:
            datetime.date.fromisoformat(parts[1])
        except ValueError:
            continue
        if not is_letters(parts[2]):
            continue
        scores.append([int(parts[0]), parts[1], parts[2]])
    scores.sort()
    return scores


def save_score(attempts, secret):
    today = datetime.date.today().isoformat()
    try:
        with open(HIGHSCORE_FILE, "a", encoding="utf-8") as file:
            file.write(str(attempts) + "," + today + "," + secret + "\n")
    except OSError:
        print("Error: cannot save the high score", file=sys.stderr)


def highscore_message(secret, attempts):
    scores = read_scores()
    if len(scores) == 0 or attempts < scores[0][0]:
        save_score(attempts, secret)
        return "Best ever! You guessed '" + secret + "' in " + str(attempts) + " attempts.."
    return ("You guessed '" + secret + "' in " + str(attempts)
            + " attempts, but the record from " + scores[0][1]
            + " is " + str(scores[0][0]) + " attempts .")


def play(secret):
    game = new_game(secret)
    while not is_won(game) and not is_lost(game):
        print(show_word(game))
        print(penalty_text(game["penalties"]))
        print(apply_guess(game, input("Your guess: ")))
    if is_lost(game):
        print("You lose! The word was '" + secret + "'")
        return None
    print(show_word(game))
    return game["attempts"]


def main():
    if len(sys.argv) < 2:
        print("Error: missing argument", file=sys.stderr)
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Error: too many arguments", file=sys.stderr)
        sys.exit(1)
    try:
        words = load_words(sys.argv[1])
    except ValueError as error:
        print("Error: " + str(error), file=sys.stderr)
        sys.exit(1)
    secret = random.choice(words)
    try:
        attempts = play(secret)
    except (KeyboardInterrupt, EOFError):
        print("\nGame stopped. Bye!", file=sys.stderr)
        sys.exit(1)
    if attempts is not None:
        print(highscore_message(secret, attempts))


if __name__ == "__main__":
    main()
