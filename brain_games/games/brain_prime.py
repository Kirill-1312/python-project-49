from brain_games.cli import welcome_user
from random import randint
import prompt

def main() -> None:
    def prime_number(random_number):
        count = 0
        if random_number in (0, 1):
            return False
        for i in range(2, random_number):
            if random_number % i == 0:
                return False
        else:
            return True
    
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        random_number = randint(1, 50)
        print('Question:', random_number)
        answer = 'yes' if prime_number(random_number) is True else 'no'
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

    

