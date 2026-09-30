HANGMAN - PSEUDOCODE

1. SETUP
   SET secret    TO a random English word, in UPPERCASE
   SET revealed  TO an empty set
   SET penalties TO 0

2. GAME LOOP (repeat until the game ends)
   SHOW the word ("_" for hidden letters)
   SHOW the penalties ("penalty" if 0 or 1, else "penalties")
   ASK a guess, in UPPERCASE

   IF the guess is empty or has non-letters:
       SAY "Letters only", ASK again (no penalty)

   IF the guess is one letter:
       IF it is already in revealed:  SAY "Already found" (no penalty)
       ELSE IF it is in secret:       ADD it to revealed, SAY "Found <count> '<letter>'"
       ELSE:                          ADD 1 penalty,      SAY "No '<letter>' found"

   IF the guess is a word:
       IF it equals secret:  SAY "correct guess", END -> win
       ELSE:                 ADD 5 penalties, EMPTY revealed, SAY "incorrect guess"

   IF all letters are revealed:  END -> win
   IF penalties > 12:            SAY "You lose!", END -> lose