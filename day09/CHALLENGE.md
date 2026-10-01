# Day 09 - Challenge: break the hangman

Beta testing of `hangman.py` (terminal) and `hangman_gui.py` (pygame).
Each line: what I tried -> what a naive version (no checks) does -> what my program does now.

## Command-line arguments
| Test | Before | Now |
|---|---|---|
| `python hangman.py` (no file) | crash `IndexError` | `Error: missing argument` on stderr, exit 1 |
| `python hangman.py a.txt b.txt` | second file ignored | `Error: too many arguments`, exit 1 |

## Word file
| Test | Before | Now |
|---|---|---|
| file does not exist | crash `FileNotFoundError` | `Error: cannot read file ...` |
| a folder (`.`) | crash `PermissionError` | same clean error |
| a binary file (`python.exe`) | crash `UnicodeDecodeError` | same clean error |
| empty file / only numbers, spaces, `,,,` | crash on `random.choice([])` | `Error: no valid word in ...` |
| accents or Korean (`hé llo`, `가나다`) | accepted, impossible to guess | ignored (A-Z only) |
| file of 10 MB+ | reads everything into memory | `Error: file ... is too big` |
| Notepad file (BOM, Windows `\r\n`, spaces) | first word silently dropped | cleaned (`utf-8-sig` + `strip`) |

## Player input
| Test | Before | Now |
|---|---|---|
| empty, `123`, `!!`, `가` | counted as a guess | `Letters only`, no attempt, no penalty |
| same wrong letter twice | penalty again | `Already tried`, no penalty |
| very long text (30+ letters) | counted as a word guess | `Letters only` |
| Ctrl+C / Ctrl+D | big red traceback | `Game stopped. Bye!`, exit 1 |

## High score file
| Test | Before | Now |
|---|---|---|
| file missing (first game) | crash | treated as "no record" |
| hand-edited lines (`hello`, `-5`, bad date) | crash `ValueError` | bad lines are skipped |
| folder is read-only | crash | `Error: cannot save the high score`, game still ends |

## Security notes
- The program never needs admin rights. It only writes `highscore.txt` next to itself.
- It can only read files the user can already read, so it gives no extra access.
- Shared logic lives in `hangman.py`, so the terminal and GUI versions get the same protections.
