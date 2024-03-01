def word_count(text):
    """Creates a list of words by using the split method on the arguement 
    then returns the length of that list (how many elements are inside it)"""

    list_words = text.split()
    num_words = len(list_words)
    return num_words


def find_longest_word(text):
    """Splits the string argument into a list then iterates over the elements in the list. 
    In each iteration the length of the elements are compared, and at the end returns the longest element"""

    list_words = text.split()

    longest = ''
    for word in list_words:
        if len(word) > len(longest):
            longest = word
    return longest


def count_substring(text, substring):
    """Uses the count method to find the number of times a substring occurs in the text, then returns that value"""

    return text.count(substring)


def extract_unique_words(text):
    """Splits the string argument into a list. Then iterates over the list and appends unique elements to a new list"""

    words_list = text.split()
    unique_words = []

    for i in words_list:
        if i not in unique_words:
            unique_words.append(i)
    
    return unique_words


def main():
    """Location to weave together previous functions to develop the whole program that will be called in the __main__"""

    #Following format for game introduction
    print('Welcome to the Text processing Program!')
    print()
    text = input('Enter a text: ')
    print()
    print(f'Original Text:\n{text}')
    print()

    #Repeat this code until the user selects exit
    while True:
        #Printing Menu
        print('Text Analysis Options:')
        print('1. Word Count')
        print('2. Longest Word')
        print('3. Count of Substring')
        print('4. Unique Words')
        print('5. Exit')
        option = input('Enter the number of the analysis option (1-5): ')

        #Finding the operation the user selected and performing it
        if option == '1':   #Word Count
            print()
            print(f'Word Count: {word_count(text)}')
            print()

        elif option == '2':     #Longest word
            print()
            print(f'Longest Word: {find_longest_word(text)}')
            print()

        elif option == '3':     #num of substring
            substring = input('Enter a substring to count: ')
            print(f"Count of Substring '{substring}': {count_substring(text, substring)}")
            print()

        elif option == '4':     #Unique words
            print()
            print(f'Unique Words: {extract_unique_words(text)}')
            print()
        
        elif option == '5':     #Exit
            print()
            print('Thank you for using the Text Processing Program!')
            break


#Where the program is called
if __name__ == '__main__':
    main()