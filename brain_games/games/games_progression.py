from random import randint


def progression() -> None:

    first_number = randint(1, 100)
    step = randint(1, 5)
    random_index = randint(0, 9)
    sequence = [
        str(x) for x in range(first_number, first_number + step * 10, step)
    ]
    answer = sequence[random_index]
    sequence[random_index] = ".."
    question = " ".join(sequence)
    return question, answer
