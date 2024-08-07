#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games import gcd


def main():
    """The function starts the game engine using the module gcd"""
    run_game(gcd)


if __name__ == '__main__':
    main()
