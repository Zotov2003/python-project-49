#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games import even


def main():
    run_game(even.game, even.condition)


if __name__ == '__main__':
    main()
