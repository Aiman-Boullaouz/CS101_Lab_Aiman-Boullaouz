import random

def roll_dice():
    """Return the sum of 2 dice randomly rolled"""
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_total = dice1 + dice2
    return dice_total


def get_user_guess():
    """Gets a user input, checks if it is valid. If input is not valid loops"""
    while True:
        try:
            user_guess = int(input('Guess the total sum (between 2 and 12): '))
            if 2 <= user_guess <= 12:
                return user_guess
            else:
                print('Invalid guess. Please enter a number between 2 and 12.')
        except ValueError:
            print('Please enter a valid number.')


def check_guess(actual_sum, user_guess):
    """Compares the values of user_guess and actual_sum (the sum of the two dice) and outputs a message depending on the value"""
    if user_guess == actual_sum:
        print(f'Congratulations! Your guess is correct ({actual_sum}).')
    elif user_guess < actual_sum:
        print('Too low, try again!')
    elif user_guess > actual_sum:
        print('Too high, try again!')


def start_game():
    """Starts the game. Gives the user 3 chances to guess a number. After guessing asks the user if they would like to play again"""
    play_again = 'y'
    while play_again == 'y':
        print('You have 3 attempts to guess the total sum of two dice.')
        print()
        actual_sum = roll_dice()
        for i in range(3):
            user_guess = get_user_guess()
            check_guess(actual_sum, user_guess)
            if actual_sum == user_guess:
                break
        play_again = input('Play again? (y/n): ')


if __name__ == "__main__":
    print('Welcome to the Dice Rolling Game!')
    print()
    start_game()
    print('Thank you for playing the Dice Rolling Game!')




