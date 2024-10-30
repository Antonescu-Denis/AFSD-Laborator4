import random as rng


words = ['python']
word_to_guess = rng.choice(words)
progress = ['_' for _ in word_to_guess]
lives = 6
used_letters = {}
answer_char = ''
play_again = 'y'

while play_again == 'y':
    while '_' in progress and lives > 0:
        print(f"Word: {' '.join(progress)}\n")
        answer_char = input('Guess a letter: ')
    
        if len(answer_char) > 1 and answer_char != word_to_guess:
            print('Input a single letter!!!\n\n\n')
            continue
        if len(answer_char) < 1:
            print('Answer is empty!!!\n\n\n')
            continue
        
        print()
        if answer_char == word_to_guess:
            progress = [ch for ch in word_to_guess]
            print(f"\nWord: {' '.join(progress)}\n")
            print('~~~~~ You guessed the whole word!!!!! ~~~~~')
        elif answer_char in word_to_guess:
            progress[word_to_guess.find(answer_char)] = answer_char
            print('Correct guess!')
            print(f"Guessed the letter \'{answer_char}\' at position {word_to_guess.find(answer_char)+1}!")
            print('\n\n\n\n\n')
        else:
            lives -= 1
            print(f"Wrong guess, you have {lives} lives left...")
            print('\n\n\n\n\n')
    
    if lives == 0:
        print('Game over!')
        print('Better luck next time...')
    else:
        print('Congratulations!!!')
        print('You won!!!')
    print('\n')

    play_again = ''
    while play_again != 'n' and play_again != 'y':
        print('Play again?\n')
        print('Valid answers: [y, ye, yes, n, no]\n')
        play_again = input('Answer: ').lower()
        if play_again in ['y', 'ye', 'yes']:
            play_again = 'y'
            lives = 6
            word_to_guess = rng.choice(words)
            progress = ['_' for _ in word_to_guess]
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        elif play_again in ['n', 'no']:
            play_again = 'n'
        else:
            print('\nNot a valid answer!!!')
            print('The list of valid answers is right above, read it!\n\n\n')

print('\n\n\n\n\n')
print('     ___________________________     ')
print('     |                         |     ')
print('     |   Thanks for playing!   |     ')
print('     |_________________________|     ')
print('\n\n\n\n\n')
