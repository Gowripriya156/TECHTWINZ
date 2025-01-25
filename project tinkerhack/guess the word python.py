import random

# Words and their characteristics
words = {
    "elephant": ["It is the largest land animal.", "It has a trunk.", "It has tusks."],
    "apple": ["It is a fruit.", "It can be red, green, or yellow.", "It keeps the doctor away."],
    "guitar": ["It is a musical instrument.", "It has strings.", "It is often used in bands."],
    "pyramid": ["It is a triangular structure.", "It is found in Egypt.", "It is an ancient wonder."],
    "ocean": ["It covers 70% of the Earth's surface.", "It is salty.", "It has waves."]
}

# Levels of difficulty
levels = {
    "easy": 3,
    "medium": 2,
    "hard": 1
}

# Initialize scoreboard
scoreboard = {}

def play_game(player_name):
    print("\nStarting the game!")
    level = input("Choose a difficulty level (easy, medium, hard): ").lower()

    while level not in levels:
        level = input("Invalid choice. Please choose from easy, medium, or hard: ").lower()

    max_hints = levels[level]
    word, hints = random.choice(list(words.items()))

    print("\nGuess the word based on its characteristics!")
    for i in range(max_hints):
        print(f"Hint {i + 1}: {hints[i]}")
        guess = input("Your guess: ").lower()

        if guess == word:
            print("Congratulations! You guessed it right.")
            scoreboard[player_name] = scoreboard.get(player_name, 0) + 1
            break
    else:
        print(f"Sorry, you've used all your hints. The word was '{word}'.")

    print(f"Your current score: {scoreboard.get(player_name, 0)}")

def view_scoreboard():
    if not scoreboard:
        print("\nNo scores yet. Play a game to get on the scoreboard!")
    else:
        print("\nScoreboard:")
        for player, score in sorted(scoreboard.items(), key=lambda x: x[1], reverse=True):
            print(f"{player}: {score}")

def main_menu():
    print("\nWelcome to the Guess the Word game!")
    while True:
        print("\nMenu:")
        print("1. Play Game")
        print("2. View Scoreboard")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            player_name = input("Enter your name: ")
            play_game(player_name)
        elif choice == "2":
            view_scoreboard()
        elif choice == "3":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
