import random
import logging

guess = ''

#configure and start logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
while guess not in ('heads', 'tails'):
  print('Guess the coin toss! Enter heads or tails:')
  guess=input()
  logging.debug('Inside loop. Guess is {}'.format(guess))

logging.debug('Out of loop. Guess is {}'.format(guess))
#change guess based on output
if guess == 'heads':
    guess = 1
else:
    guess = 0
toss = random.randint(0, 1) #0 = tails, 1 = heads
logging.debug('Toss is {}'.format(toss))
if toss == guess:
  print('You got it!')
else:
  print('Nope! Guess again!')
  guess = input()
  if toss == guess:
    print('You got it!')
  else:
    print('Nope. You are really bad at this game.')
logging.debug('End of program.')

