import prompt


def welcome_user():
    """The function greets the user"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name
