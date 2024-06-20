#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.module_brain_calc import brain_prime


def main():
    condition = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
    run_game(brain_prime, condition)

if __name__ == '__main__':
    main()
