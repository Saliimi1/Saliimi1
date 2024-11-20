import random

def load_dictionary(file_path):
    """Load dictionary words from a file and filter words of length between 4 and 12."""
    with open(file_path, 'r') as f:
        words = [line.strip().upper() for line in f if 4 <= len(line.strip()) <= 12]
    return words

def filter_words_by_length(words, length):
    """Filter words to match a specific length."""
    return [word for word in words if len(word) == length]

def update_display_word(display_word, target_word, guessed_letter):
    """Update the displayed word based on the guessed letter."""
    return ''.join([guessed_letter if target_word[i] == guessed_letter else display_word[i] for i in range(len(target_word))])

def play_guess_the_word(words, difficulty):
    word_length = random.randint(4, 12)
    word_list = filter_words_by_length(words, word_length)
    correct_word = random.choice(word_list)
    display_word = '_' * word_length
    guesses_remaining = word_length * 2
    guessed_letters = set()
    
    print(f"The word has {word_length} letters: {display_word}")
    
    while guesses_remaining > 0 and display_word != correct_word:
        print(f"\nGuesses left: {guesses_remaining}")
        print(f"Guessed letters: {sorted(guessed_letters)}")
        print(f"Current word: {display_word}")
        
        guess = input("Guess a letter: ").upper()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try another.")
            continue
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical letter.")
            continue

        # HARD mode dodge logic (silent)
        if difficulty == "HARD" and random.random() < 0.3 and guess in correct_word:
            continue  # Skip further processing for dodged correct guesses
        
        # Add the guess to guessed_letters
        guessed_letters.add(guess)

        if guess in correct_word:
            display_word = update_display_word(display_word, correct_word, guess)
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            guesses_remaining -= 1
            print(f"The letter '{guess}' is not in the word.")
    
    if display_word == correct_word:
        print(f"\n🎉 Congratulations! You've guessed the word: {correct_word} 🎉")
        return True
    else:
        print(f"\n😞 Out of guesses! The word was: {correct_word}. 😞")
        return False

def main():
    print("=" * 50)
    print("🎮 Welcome to 'Guess the Word'! 🎮")
    print("Can you figure out the secret word before running out of guesses?")
    print("=" * 50)
    
    words = load_dictionary('dictionary.txt')
    
    while True:
        difficulty = input("\nChoose difficulty (EASY/HARD): ").upper()
        while difficulty not in {"EASY", "HARD"}:
            difficulty = input("Please choose either EASY or HARD: ").upper()
        
        # Play the game and determine win/loss
        result = play_guess_the_word(words, difficulty)
        
        # Ask if the player wants to play again
        play_again = input("\nWould you like to play again? (Y/N): ").upper()
        while play_again not in {"Y", "N"}:
            play_again = input("Please enter 'Y' for yes or 'N' for no: ").upper()
        
        if play_again == "N":
            print("\nThank you for playing! Goodbye! 🎉")
            break

if __name__ == "__main__":
    main()
