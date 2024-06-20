from brain_games.games.greetings import welcome_user


def run_game(brain, condition):
    start = 0
    counter = 0
    name = welcome_user()
    print(condition)

    while start < 3:
        print(operation)
        if input1 == res:
            counter += 1
            print("Correct!")
        else:
            print(f"{input1} is  wrong answer ;(. ", end="")
            print(f"Correct answer was {res}")
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")