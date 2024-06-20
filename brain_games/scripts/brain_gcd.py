#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.module_brain_calc import brain_gcd


def main():
    condition = "Find the greatest common divisor of given numbers."
    run_game(brain_gcd, condition)

if __name__ == '__main__':
    main()
