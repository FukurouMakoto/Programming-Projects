import random

def collect_input():
    choice = input("Rock, paper, or scissors?\n")
    return choice

def message(comp_choice, result):
    return f"Computer chose {comp_choice}. You {result}!"

def invalid_request():
    return f"Invalid choice. Try again."

def rock_paper_scissors(choice):
    choices = ['rock', 'paper', 'scissors']

    win = 'win'
    lose = 'lose'
    tie = 'tie'

    comp_choice = random.choice(choices)
    
    if choice.lower() == 'rock':
        if comp_choice == 'paper':
            print(message(comp_choice, lose))
        elif comp_choice == 'scissors':
            print(message(comp_choice, win))
        elif comp_choice == 'rock':
            print(message(comp_choice, tie))
        else:
            print(invalid_request())
            collect_input()

    if choice.lower() == 'paper':
        if comp_choice == 'paper':
            print(message(comp_choice, tie))
        elif comp_choice == 'scissors':
            print(message(comp_choice, lose))
        elif comp_choice == 'rock':
            print(message(comp_choice, win))
        else:
            print(invalid_request())
            collect_input()

    if choice.lower() == 'scissors':
        if comp_choice == 'paper':
            print(message(comp_choice, win))
        elif comp_choice == 'scissors':
            print(message(comp_choice, tie))
        elif comp_choice == 'rock':
            print(message(comp_choice, lose))
        else:
            print(invalid_request())
            collect_input()


while True:
    rock_paper_scissors(collect_input())