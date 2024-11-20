from brain_games.cli import welcome_user
import prompt


def engine(game, quest) -> None:
    name = welcome_user()
    print(quest)
    count = 0
    while count != 3:
        question, answer = game()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if answer == user_answer:
            print("Correct!")
            count += 1
        else:
            print(
                (
                    f"'{user_answer}' is wrong answer ;(. Correct answer was "
                    + f"'{answer}'.\nLet's try again, {name}!"
                )
            )
            break
    else:
        print(f"Congratulations, {name}!")
