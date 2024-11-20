from brain_games.engine import engine
from brain_games.games.game_calc import calc


def main():
    engine(calc, "What is the result of the expression?")
