from brain_games.cli import welcome_user
import prompt
import math
from random import randint


def main() -> None:
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    count = 0
    while count != 3:
        number_left = randint(1, 100)
        number_right = randint(1, 100)
        print(f'Question: {number_left} {number_right}')
        answer = math.gcd(number_left, number_right)
        user_answer_str = prompt.string('Your answer: ')
        user_answer = int(user_answer_str)
        if answer == user_answer:
            print("Correct!")
            count += 1
        if answer != user_answer:
            print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.
Let's try again, Sam!''')
            break
    else:
        print(f'Congratulations, {name}')


