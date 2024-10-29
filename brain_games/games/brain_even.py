from brain_games.cli import welcome_user
from random import randint
import prompt


def main() -> None:
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        random_number = randint(1, 20)
        if random_number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        print('Question:', random_number)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            break
    
    else:
        print(f'Congratulations, {name}!')




    

    