from brain_games.cli import welcome_user
from random import randint
import prompt

def prime() -> None:
    def prime_number(random_number):
        count = 0
        if random_number in (0, 1):
            return False
        for i in range(2, random_number):
            if random_number % i == 0:
                return False
        else:
            return True
    
    
    question = randint(1, 50)
    answer = 'yes' if prime_number(question) is True else 'no'
    return question, answer
    

    

