import random

def game(str):
    for i in range(6):
        flag = True
        guess = input("What is your guess? ")
        if len(guess) != len(str):
            print(f'You entered a guess with the wrong number of characters, you should enter a guess with {len(str)} characters, and not {len(guess)} chraracters like you did ')
            flag = False
        while not flag:
            guess = input('Enter another guess: ')
            if len(guess) == len(str):
                flag = True
        for j in range(len(str)):
            if j == 0:
                if str == guess:
                    print(f'You guessed the correct word in {i+1} guesses, congratulations!')
                    return
            if guess[j] == str[j]:
                print(guess[j], end='')
            elif guess[j] in str and guess.count(guess[j]) <= str.count(guess[j]):
                print(guess[j].upper(), end='')
            else:
                print('_', end='')
        print('')
            


my_file = open("sgb-words.txt", "r")

data = my_file.read()

wordlist = data.split("\n")

my_file.close()


number = random.randint(1, len(wordlist))

game(wordlist[number])
