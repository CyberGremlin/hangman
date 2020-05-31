import random

word = random.choice(['python', 'java', 'kotlin', 'javascript'])
lives = 8
guesses = set()
play = ''
prev_hint = ''
for letter in range(len(word)):
    prev_hint += '-'

print('H A N G M A N')

while play != 'play' and play != 'exit':
    play = input('Type "play" to play the game, "exit" to quit:')
    if play == 'exit':
        break
    elif play == 'play':
        continue

while True:
    if lives > 0:
        hint = ''
        for letter in range(len(word)):
            if word[letter] in guesses:
                hint += word[letter]
            else:
                hint += '-'

        print()
        print(hint)

        if guesses != set(word):
            guess = input('Input a letter:')

            if len(guess) != 1:
                print('You should input a single letter')
                continue
            elif guess in guesses:
                print('You already typed this letter')
                continue
            elif not guess.isalpha() or not guess.islower():
                print('It is not an ASCII lowercase letter')
                continue
            else:
                guesses.add(guess)
                if guess not in word:
                    print('No such letter in the word')
                    lives -= 1
                continue
        else:
            print(hint)
            print('You guessed the word!')
            print('You survived!')
            break
    elif guesses == set(word):
        print('You survived!')
        break
    else:
        print('You are hanged!')
        break
