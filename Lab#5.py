import random

def choose_word(words):
    random_word = random.choice(words)
    return random_word

def display_word(word, guessed_letters):
    blank_word = '_' * len(word)
    fill_word = list(blank_word)

    for i in guessed_letters:
        if i in word:
            if word.count(i) < 2:
                index = word.find(i)
                fill_word[index] = i
            else:
                index1 = word.find(i)
                fill_word[index1] = i

                index2 = word.rfind(i)
                fill_word[index2] = i
    
    return ' '.join(fill_word)


def check_guess(word, guessed_letters, guess):
    guessed_letters.append(guess)
    if guess in word:
        return True
    


def is_word_guessed(word, guessed_letters):
    for i in word:
        if i not in guessed_letters:
            return False
    return True
            

def start_game():
    print('Welcome to the Word Game!')
    print()

    words = ["PYTHON", "JAVASCRIPT", "JAVA", "HTML", "CSS"]
    guessed_letters = []
    random_word = choose_word(words)
    
    while True:
        print(f'Guess the Word: {display_word(random_word, guessed_letters)}')
        #Get guess and validate
        while True:
            guess = input('Enter your guess: ').upper()
            if guess.isdigit():
                print('Invalid input. Please enter a single alphabetical character.')
            elif len(guess) > 1:
                print('Invalid input. Please enter a single alphabetical character.')
            else:
                break
        
        if check_guess(random_word, guessed_letters, guess) == True:
            print(f'Correct Guess! Word: {display_word(random_word, guessed_letters)}')
        else:
            print(f'Incorrect Guess! Word: {display_word(random_word, guessed_letters)} Guessed letters: {' '.join(guessed_letters)}')

        if is_word_guessed(random_word, guessed_letters) == True:
            print()
            print(f'Congratulations! You guessed the word: {random_word}')

            play_again = input('Do you want to play again?(yes/no): ')
            if play_again.lower() == 'no' or play_again.lower() =='n':
                break
            elif play_again.lower() == 'yes' or play_again.lower() =='y':
                #reset the values so the game can actually restart
                guessed_letters = []
                random_word = choose_word(words)
                continue
            else:
                print('Invalid input... exiting program')
                break
    print()
    print('Thank you for playing the Word Game!')

if __name__ == "__main__":
    start_game()