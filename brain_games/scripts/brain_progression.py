#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games import progression


def main():
    """The function starts the game engine using the module progression"""
    run_game(progression)


if __name__ == '__main__':
    main()
