from brain_games.engine import engine
from brain_games.games.game_gcd import gcd


def main():
    engine(gcd, "Find the greatest common divisor of given numbers.")
