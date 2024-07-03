#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games import prime


def main():
    """The function starts the game engine using the module prime"""
    run_game(prime)


if __name__ == '__main__':
    main()
