#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.progression import brain_progression


def main():
    condition = "What number is missing in the progression?"
    run_game(brain_progression, condition)


if __name__ == '__main__':
    main()
