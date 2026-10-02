# Day 10 — Reflection

> ✏️ 초안이에요. 멘토 앞에서 "내 말"로 말할 수 있게 직접 고치세요.
> (Draft — rewrite it in your own words before the check.)

## Top 3 — best tips I learned

1. **Git = save points.** `git status` → `git add` → `git commit` → `git push`.
   Small commits with clear messages mean I can always go back.
2. **Read the error message from the bottom.** The last line of a Traceback says *what* broke,
   the line above says *where*. Then `try / except` lets my program handle it without crashing.
3. **Break a big problem into bricks.** Hangman (Day 07→09) was too big at first. Pseudocode +
   small functions (one job each) made it possible, and later I could reuse the same logic for the GUI.

## Worst 3 — what I missed

1. **Letting someone else type the code** (Day 01–03). It worked, but nothing stayed in my head.
   From Day 07 I went page by page and typed/ran things myself.
2. **Not testing edge cases first.** Empty input, `0`, a missing file, a word instead of a number…
   most bugs hide there (Day 09 error handling, Bonus `step = 0`).
3. **Pushing late.** Day 09 stayed only on my computer for a while. Commit *and push* at the end of every day.

## Best practices (rules for our company)

1. Clear names: `count_lines`, not `cl` or `x`.
2. One function = one job. Short functions are easy to test and to reuse.
3. No copy-paste: if I write the same code twice, make it a function.
4. Handle errors (`try / except`) and check user input. Never trust input.
5. Comments explain **why**, not what the code obviously does.
6. Small commits, one idea each, with a message that says what changed.
7. Follow PEP 8 (Python's style guide): 4-space indent, `snake_case`, readable line length.
8. Test it before you push, including the strange cases.

> Do I always follow them? **No.** See the code review below: my Day 04 challenge breaks rules 1, 4, 5 and 7.

## Code review — `day04/challenge.py`

Before:

```python
while 1:
 n,s=input().split(" ",1);n=int(n)
 if n==0:break
 print(n if n>=42 or set(s)&set("aeiouAEIOU")else s)
```

| Problem | Why it matters | Fix |
|---|---|---|
| Names `n`, `s` | Nobody knows what they mean | `number`, `text` |
| 1-space indent, `;`, everything packed | Hard to read (PEP 8) | 4 spaces, one statement per line |
| `while 1` | Works, but `while True` says what it means | `while True` |
| No input check | `"abc"` or a line without a space → crash | `try / except ValueError` |
| Vowel test hidden in a `set` trick | Clever but hard to understand | helper `has_vowel(text)` |

After:

```python
VOWELS = set("aeiouAEIOU")


def has_vowel(text):
    return bool(set(text) & VOWELS)


while True:
    try:
        number, text = input().split(" ", 1)
        number = int(number)
    except ValueError:
        print("Usage: <number> <text>")
        continue
    if number == 0:
        break
    print(number if number >= 42 or has_vowel(text) else text)
```

Peer review: _(with a classmate — write what they told you here)_

## Self-evaluation (crap / noob / average / goat)

| Skill | Me | Classmate's view |
|---|---|---|
| Navigate a Linux filesystem (`cd`, `ls`, `pwd`) | average | |
| Write a simple Python program | average | |
| Write a more complex Python program (hangman) | noob | |
| Find a bug in a Python program | noob | |
| Find information on the Internet | average | |
| Ask someone when I'm stuck | average | |
| Help people around me | noob | |
| Test a program efficiently | noob | |

Staff feedback: _(write it here)_
