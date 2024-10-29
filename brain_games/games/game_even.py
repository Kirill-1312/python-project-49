from brain_games.cli import welcome_user
from random import randint
import prompt


def even() -> None:
    random_number = randint(1, 20)
    if random_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    question = random_number
    return question, answer




    

    