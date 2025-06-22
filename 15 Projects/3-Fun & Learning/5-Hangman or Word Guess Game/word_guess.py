import random

def choose_word():
    words = ["python", "developer", "hangman", "keyboard", "function"]
    return random.choice(words)

def play_game():
    word = choose_word()
    guessed = ["_"] * len(word)
    attempts_left = 6
    guessed_letters = []

    print("🔤 Welcome to Word Guess Game!")
    
    while attempts_left > 0 and "_" in guessed:
        print("\nWord: ", " ".join(guessed))
        print(f"❌ Wrong guesses left: {attempts_left}")
        print(f"📚 Letters guessed: {', '.join(guessed_letters)}")

        guess = input("🔍 Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, ch in enumerate(word):
                if ch == guess:
                    guessed[i] = guess
            print("✅ Good guess!")
        else:
            attempts_left -= 1
            print("❌ Wrong guess!")

    if "_" not in guessed:
        print(f"\n🎉 You won! The word was: {word}")
    else:
        print(f"\n💀 Out of tries. The word was: {word}")

play_game()