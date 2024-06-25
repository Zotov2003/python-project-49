#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.calc import brain_calc


def main():
    condition = "What is the result of the expression?"
    run_game(brain_calc, condition)


if __name__ == '__main__':
    main()
