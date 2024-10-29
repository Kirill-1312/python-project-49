from brain_games.cli import welcome_user
from random import randint
import prompt


def main() -> None:
    name = welcome_user()
    count = 0
    
    print('What number is missing in the progression?')
    while count != 3:
        first_number = randint(1, 100)
        step = randint(1, 5)
        random_index = randint(0, 9)
        sequence = [str(x) for x in range(first_number, first_number + step*10, step)]
        answer = sequence[random_index]
        sequence[random_index] = '..'
        sequence_str = ' '.join(sequence)
        print(f'Question: {sequence_str}')
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print('Correct!')
            count += 1
        else:
            print (f''''{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.
Let's try again, {name}''')
            break
        
    else:
        print(f'Congratulations, {name}!')
