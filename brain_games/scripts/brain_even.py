#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games import even


def main():
    """The function starts the game engine using the module even"""
    run_game(even)


if __name__ == '__main__':
    main()
