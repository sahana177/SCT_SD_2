import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("I've selected a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("\nEnter your guess (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("🚨 Please enter a number between 1 and 100!")
                continue

            if guess < secret_number:
                print("⬆️ Too low! Try a higher number.")
            elif guess > secret_number:
                print("⬇️ Too high! Try a lower number.")
            else:
                print(f"\n🎉 Correct! You guessed the number in {attempts} attempts!")
                break
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()


