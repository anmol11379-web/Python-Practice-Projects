import random

def number_guessing_game_with_levels():
    levels = {
        'easy': {'max_range': 50, 'max_attempts': 10},
        'medium': {'max_range': 100, 'max_attempts': 7},
        'hard': {'max_range': 200, 'max_attempts': 5}
    }
    print("Welcome to the Number Guessing Game!")
    while True:
        level_choice = input("Choose a level (easy, medium, hard): ").lower()
        if level_choice in levels:
            level_info = levels[level_choice]
            break
        else:
            print("Invalid level. Please choose easy, medium, or hard.")
    max_range = level_info['max_range']
    attempts_left = level_info['max_attempts']
    secret_number = random.randint(1, max_range)    
    print(f"\nI'm thinking of a number between 1 and {max_range}.")
    print(f"You have {attempts_left} attempts.")
    while attempts_left > 0:
        print(f"\nAttempts left: {attempts_left}")  
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue # Go back to the start of the loop
        if user_guess == secret_number:
            print(f"🎉 Congratulations! You guessed the number {secret_number}!")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
        attempts_left -= 1 
    if attempts_left == 0 and user_guess != secret_number:
        print(f"😔 Game Over. You ran out of attempts. The number was {secret_number}.")
number_guessing_game_with_levels()