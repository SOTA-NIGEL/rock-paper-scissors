# Rock, Paper, Scissors Game
# This is a simple implementation of the Rock, Paper, Scissors game.
import random

def game():
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)

    user = input('Choose between rock, paper or scissors? ').lower().strip()
    while user not in choices:
        user = input('Invalid input. Please enter rock, paper, or scissors: ').lower().strip()

    print(f'\nComputer chose {computer}, you chose {user}.\n')

    if user == computer:
        print('It\'s a tie!')
    elif user == 'rock':
        if computer == 'scissors':
            print('Rock smashes scissors! You win!')
        else:
            print('Paper covers rock! You lose.')
    elif user == 'paper':
        if computer == 'rock':
            print('Paper covers rock! You win!')
        else:
            print('Scissors cuts paper! You lose.')
    elif user == 'scissors':
        if computer == 'paper':
            print('Scissors cuts paper! You win!')
        else:
            print('Rock smashes scissors! You lose.')

if __name__ == '__main__':
    game()
    play_again = input('Do you want to play again? (yes/no): ').lower().split()
    if play_again == 'yes':  
        game()
    else :
        print('Thanks for playing!')