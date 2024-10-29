from brain_games.cli import welcome_user
import prompt
import math
from random import randint


def gcd() -> None:
    number_left = randint(1, 100)
    number_right = randint(1, 100)
    question = f'{number_left} {number_right}'
    answer = str(math.gcd(number_left, number_right))
    return question, answer


