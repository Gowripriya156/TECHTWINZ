import random
import time
import os

# Word list categorized by themes
words = {
    "animals": [
        "cat", "dog", "elephant", "lion", "giraffe", "tiger", "bear", "wolf", "fox", "zebra", "kangaroo", 
        "panda", "koala", "rabbit", "deer", "cheetah", "leopard", "dolphin", "shark", "whale"
    ],
    "technology": [
        "python", "computer", "internet", "algorithm", "database", "hardware", "software", "network", 
        "encryption", "firewall", "robotics", "artificial intelligence", "blockchain", "cloud", "quantum computing"
    ],
    "cities": [
        "new york", "los angeles", "chicago", "miami", "toronto", "vancouver", "rio de janeiro", 
        "sao paulo", "mexico city", "buenos aires", "paris", "london", "rome", "berlin", "madrid", 
        "barcelona", "amsterdam", "vienna", "prague", "lisbon", "tokyo", "seoul", "shanghai", "beijing", 
        "mumbai", "bangkok", "dubai", "singapore", "istanbul", "kuala lumpur", "cairo", "cape town", 
        "johannesburg", "nairobi", "marrakech", "lagos", "addis ababa", "accra", "dakar", "tunis", 
        "sydney", "melbourne", "auckland", "wellington", "brisbane", "perth", "christchurch", "hobart", 
        "adelaide", "darwin"
    ]
}

LEADERBOARD_FILE = "leaderboard.txt"

def scramble_word(word):
    """Scrambles the letters of a word."""
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def load_leaderboard():
    """Loads the leaderboard from a file."""
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    with open(LEADERBOARD_FILE, "r") as file:
        leaderboard = [line.strip().split(",") for line in file]
    return [(name, int(score)) for name, score in leaderboard]

def save_leaderboard(leaderboard):
    """Saves the leaderboard to a file."""
    with open(LEADERBOARD_FILE, "w") as file:
        for name, score in leaderboard:
            file.write(f"{name},{score}\n")

def display_leaderboard():
    """Displays the leaderboard."""
    leaderboard = load_leaderboard()
    if not leaderboard:
        print("\nNo scores yet on the leaderboard.\n")
        return

    print("\nLeaderboard:")
    print("Rank | Name         | Score")
    print("-" * 25)
    for rank, (name, score) in enumerate(sorted(leaderboard, key=lambda x: x[1], reverse=True), start=1):
        print(f"{rank:>4} | {name:<12} | {score}")
    print()

def play_game():
    print("Welcome to the Word Scramble Game!")
    print("Choose a category: Animals, Technology, or Cities.")
    print("Type 'exit' at any time to quit the game.\n")

    # Category selection
    category = input("Select a category (animals/technology/cities): ").strip().lower()
    while category not in words:
        print("Invalid choice. Please select 'animals', 'technology', or 'cities'.")
        category = input("Select a category: ").strip().lower()

    word_list = words[category]

    # Multiplayer setup
    print("\nMultiplayer mode enabled. Each player takes turns guessing words.")
    player1 = input("Enter Player 1's name: ").strip()
    player2 = input("Enter Player 2's name: ").strip()

    scores = {player1: 0, player2: 0}
    players = [player1, player2]

    round_count = 1
    while True:
        current_player = players[(round_count - 1) % 2]
        print(f"\nRound {round_count}: {current_player}'s turn!")

        # Select and scramble a word
        original_word = random.choice(word_list)
        scrambled = scramble_word(original_word)
        print(f"Scrambled word: {scrambled}")
        print(f"You have 10 seconds to guess the word!")

        # Timer and input
        start_time = time.time()
        time_limit = 10
        while True:
            elapsed_time = int(time.time() - start_time)
            remaining_time = time_limit - elapsed_time

            if remaining_time <= 0:
                print("Time's up!")
                print(f"The correct word was: {original_word}")
                break

            print(f"Time remaining: {remaining_time} seconds", end="\r")
            guess = input("Your guess: ").strip().lower()

            if guess == "exit":
                print(f"Thanks for playing! Final scores:")
                for player, score in scores.items():
                    print(f"{player}: {score} points")
                update_leaderboard(scores)
                return

            if guess == original_word:
                print("Correct! Well done!")
                scores[current_player] += 10
                break
            else:
                print("Wrong guess. Round ends.")
                print(f"The correct word was: {original_word}")
                break

        print(f"Current scores: {player1} = {scores[player1]} | {player2} = {scores[player2]}")
        round_count += 1

def update_leaderboard(scores):
    """Updates the leaderboard with the scores."""
    leaderboard = load_leaderboard()
    for player, score in scores.items():
        leaderboard.append((player, score))
    save_leaderboard(leaderboard)

def main():
    while True:
        print("\n--- Word Scramble Game ---")
        print("1. Play Game")
        print("2. View Leaderboard")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            display_leaderboard()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the game
if __name__ == "__main__":
    main()

