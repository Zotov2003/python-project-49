from brain_games.cli import welcome_user


def run_game(game_module):
    counter = 0
    name = welcome_user()
    condition = game_module.condition
    print(condition)

    while counter < 3:
        operation, res = game_module.game()
        print(f"Question: {operation}")
        input1 = input("Your answer: ")
        if input1 == str(res):
            counter += 1
            print("Correct!")
        else:
            print(f"{input1} is  wrong answer ;(. ", end="")
            print(f"Correct answer was {res}")
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")
