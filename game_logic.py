import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    # Stage 2: Only the head remains
    """
     ___  
    /___\\ 
    (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
     ___  
    /___\\ 
    """
]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Show the current snowman stage and the masked secret word."""
    stage_idx = min(max(0, mistakes), len(STAGES) - 1)
    print(STAGES[stage_idx])

    # Build the masked word
    display_chars = [
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    ]
    print("Word:", " ".join(display_chars))
    if guessed_letters:
        print("Guessed:", " ".join(sorted(guessed_letters)))
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}\n")

def is_word_revealed(secret_word, guessed_letters):
    """Return True if every unique letter in the secret word has been guessed."""
    return set(secret_word).issubset(guessed_letters)

def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1  # last stage is fully melted

    print("Welcome to Snowman Meltdown!")
    print("Save the snowman by guessing the word one letter at a time.\n")

    # Main loop: keep going until win or out of lives
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check for win before asking again (covers instant-win in edge cases)
        if is_word_revealed(secret_word, guessed_letters):
            print("❄️  You saved the snowman! You guessed the word!")
            print(f"The word was: {secret_word}\n")
            break

        if mistakes >= max_mistakes:
            print("💧 The snowman melted… Game over.")
            print(f"The word was: {secret_word}\n")
            break

        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a new one.\n")
            continue

        # Record the guess
        guessed_letters.add(guess)

        # Check correctness
        if guess in secret_word:
            print(f"Nice! '{guess}' is in the word.\n")
        else:
            mistakes += 1
            print(f"Nope! '{guess}' is not in the word.\n")

        # Loop continues; end conditions are re-checked at the top

if __name__ == "__main__":
    play_game()

