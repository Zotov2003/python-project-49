from brain_games.cli import welcome_user


def run_game(game_module):
    """The function starts the game process itself by accessing the required modules"""
    counter = 0
    name = welcome_user()
    print(game_module.CONDITION)

    while counter < 3:
        task, result_task = game_module.get_question_and_answer()
        print(f"Question: {task}")
        user_answer = input("Your answer: ")
        if user_answer == str(result_task):
            counter += 1
            print("Correct!")
        else:
            print(f"{user_answer} is  wrong answer ;(. ", end="")
            print(f"Correct answer was {result_task}")
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")
