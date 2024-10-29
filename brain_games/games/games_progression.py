from brain_games.cli import welcome_user
from random import randint
import prompt


def progression() -> None:

    first_number = randint(1, 100)
    step = randint(1, 5)
    random_index = randint(0, 9)
    sequence = [str(x) for x in range(first_number, first_number + step*10, step)]
    answer = sequence[random_index]
    sequence[random_index] = '..'
    question = ' '.join(sequence)
    return question, answer
