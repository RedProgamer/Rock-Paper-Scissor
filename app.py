from random import choice

possibleMoves = ['r', 'p', 's']
computer_points = 0
user_points = 0

def user_choice():
    user_input = input('Rock, Paper or Scissor : ').lower()
    if user_input in ['rock', 'paper', 'scissor', 'r', 'p', 's']:
        if user_input in ['rock', 'r']:
            user_input = 'r'
        elif user_input in ['paper', 'p']:
            user_input = 'p'
        elif user_input in ['scissor', 's']:
            user_input = 's'
        return user_input
    else:
        user_input = input('Please give valid input (rock, paper or scissor) : ')
        



while True:
    computer_move = choice(possibleMoves)
    user_input = user_choice()
    if computer_move == 'r':
        if user_input == 'r':
            print(f'Your move is rock.\nComputers move is rock.\nTie')
        elif user_input == 'p':
            print(f'Your move is paper.\nComputers move is rock.\nYou won')
            user_points += 1
        elif user_input == 's':
            print(f'Your move is scissor.\nComputers move is rock.\nYou lost')
            computer_points += 1
    elif computer_move == 'p':
        if user_input == 'p':
            print(f'Your move is paper.\nComputers move is paper.\nTie')
        elif user_input == 'r':
            print(f'Your move is rock.\nComputers move is paper.\nYou lost')
            computer_points += 1
        elif user_input == 's':
            print(f'Your move is scissor.\nComputers move is paper.\nYou won')
            user_points += 1
    elif computer_move == 's':
        if user_input == 's':
            print(f'Your move is scissor.\nComputers move is scissor.\nTie')
        elif user_input == 'r':
            print(f'Your move is rock.\nComputers move is scissor.\nYou won')
            user_points += 1
        elif user_input == 'p':
            print(f'Your move is paper.\n Computers move is scissor.\n You lost')
            computer_points += 1

    print("")
    print("Player's score : {}".format(str(user_points)))
    print("Computer's score {}".format(str(computer_points)))
    print("")
    
    replay_game = input('Do you want to play again (y/n) : ').lower()
    while replay_game not in ["yes", "no", "y", "n"]:
        replay_game = input('Please! do you want to play again (y/n) : ').lower()
    else:
        if replay_game in ['yes', 'y']:
            pass
        elif replay_game in ['no', 'n']:
            print('Thanks for playing the game.')
            break

    



