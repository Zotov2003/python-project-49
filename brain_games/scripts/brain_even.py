#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.even import brain_even


def main():
    condition = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    run_game(brain_even, condition)


if __name__ == '__main__':
    main()
