from brain_games.cli import welcome_user
from random import randint
import random
import prompt

def main():
    name = welcome_user()
    print('What is the result of the expression?')
    operators = '+-*'
    count = 0
    while count != 3:
        number_left = randint(1, 20) 
        operator = random.choice(operators) 
        number_right = randint(1, 20)
        question = f'Question {number_left} {operator} {number_right}'
        print(question)
        user_answer = prompt.string('Your answer: ')
        actions = eval(f'{number_left} {operator} {number_right}')
        actions_new = str(actions)
        if user_answer == actions_new:
            count += 1
            print('Correct!')
        else:
            print (f'''{user_answer} is wrong answer ;(. Correct answer was '{actions_new}'.
Let's try again, {name}!''')
            break   
    else:
        print(f'Congratulations, {name}!')



        




