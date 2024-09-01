import random

word_bank=["ayesha", "Usman", "Something"]
word = random.choice(word_bank)
guessedWord = ['_']*len(word)
attempts = 10

while attempts>0:
  print('\nCurrent word: ' + ' '.join(guessedWord))
  guess = input('\nGuess a letter: ')

  if guess in word: 
    for i in range(len(word)):
      if word[i] == guess:
        guessedWord[i] = guess

    print(guessedWord) 
  else:
    attempts -=1
    print('Wrong guess! Attempts left: '+str(attempts))

  if '_' not in guessedWord:
    print("Congrats, you win!")
    break
  else:
    print('\nYou have run out of attempts. The word was: '+word)
