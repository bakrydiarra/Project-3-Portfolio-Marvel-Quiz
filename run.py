"""
Import libraries needed to the function of this application.
code : if __name__ == "__main__" at the end of the fle
make sure that the function run as main programm
code taken:
https://www.freecodecamp.org/news/if-name-main-python-example/
"""
from time import sleep
import os
import colorama
from colorama import Fore, Style
from logo import TITLE
from logo import BYE
from quiz import quiz_questions
colorama.init(autoreset=True)


def start():
    """
    Display logo and instructions for the quiz.
    call all the other functions to run the
    application
    """
    print(TITLE)
    print("Welcome to the superheroes universe!\n")
    sleep(1)
    print("Are you ready to test your knowledge?\n")
    sleep(1)
    print("You have 10 multiple choice questions.\n")
    sleep(1)
    print("Select your answer typing 'a', 'b' or 'c'.\n")
    sleep(1)
    validate_name()
    run_quiz()
    play_again()


def validate_name():
    """
    User has to give a valid name
    in order to run the quiz
    """
    while True:
        name = input("Enter your name to start the quiz: \n")
        name = name.strip().lower()
        print("")
        if len(name) > 10 or len(name) < 4:
            print(f"{Fore.RED}Please enter a name between 4 and 10 letters")
        elif not name.isalpha():
            print(f"{Fore.RED}Please enter a name between 4 and 10 letters")
        else:
            print(f"Godd luck, {name}!")
            print("")
            sleep(1)
            break


def run_quiz():
    """
    Iterate through the questions list.
    Iterate through the choice list.
    Get user input-answer.
    Validate user input-answer: invalid, correct,wrong.
    Implementing score +=10 for a good answer.
    """

    score = 0

    for question in quiz_questions:
        print(f"{question.item}?")
        print("")
        for option in question.choice:
            print(option)
        user_answer = input("Enter your answer: \n")
        if user_answer.lower() not in ["a", "b", "c"]:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid answer! Pick: a, b or c.")
            user_answer = input("Enter your answer: \n")
        if user_answer.lower() == question.answer.lower():
            print(f"{Fore.GREEN}Well done!")
            print("")
            score += 10
        else:
            print(f"{Fore.RED}Sorry, wrong answer!")
            print("")
    final_score(score)


def final_score(score):
    """
    Display user's score
    and a message
    """

    if score < 50:
        print("You're almost passed!")
        print(f"Your score is {score} out of 100 \n")
    elif score >= 50 and score <= 70:
        print("Good job. You passed!")
        print(f"Your score is {score} out of 100 \n")
    else:
        print("Excellent Job!")
        print(f"Your score is {score} out of 100 \n")


def play_again():
    """
    Reset the quiz to play again
    or quit the game if the user
    want to stop playing
    """
    while True:
        user_wish = input("Wanna play again? y/n\n")
        user_wish = user_wish.lower()
        if user_wish == "y":
            clear()
            print(f"{Fore.BLUE}{Style.BRIGHT}Reseting Quiz...")
            sleep(1)
            clear()
            start()
            break
        if user_wish == "n":
            print(BYE)
            sleep(1)
            print("Closing application...")
            sleep(2)
            clear()
            print("To reset the quiz click the button 'Run Programm'")
            return False
        if user_wish != "y" and user_wish != "n":
            print(f"{Fore.RED}{Style.BRIGHT}Invalid answer! Pick: 'y' or 'n'")


def clear():
    """
    use code from
    https://www.w3docs.com/snippets/python/how-to-clear-the-interpreter-console.html
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(3)


if __name__ == "__main__":
    start()
