
from random import randint
import random

def calc():
    operators = '+-*'
    number_left = randint(1, 20)
    operator = random.choice(operators) 
    number_right = randint(1, 20)
    question = f'Question: {number_left} {operator} {number_right}'
    actions = eval(f'{number_left} {operator} {number_right}')
    answer = str(actions)
    return question, answer
    
     
    



        




