import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while attempts < 3:
        try:
            player_guess = int(input("Your guess: "))
            attempts += 1

            if player_guess < number_to_guess:
                print("Try a higher number.")
            elif player_guess > number_to_guess:
                print("Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                return

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_number()
