"""
Import libraries needed to the function of this application.
"""
import time
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
from logo import TITLE


def start():
    """
    Display logo and instructions of the quiz
    Asking username input to run the quiz
    """
    print(TITLE)
    print("Welcome to the superheroes universe!\n")
    print("Are you ready to test your knowledge?\n")
    print("You have 10 multiple choice questions.\n")
    print("Select your answer typing 'a', 'b' or 'c'.\n")
    validate_name()


def validate_name():
    """
    validation of the username to start the game
    """
    while True:
        name = input("Enter your name to start the quiz. \n")
        name = name.strip().lower()
        print("")
        if len(name) > 10:
            print(f"""{Fore.RED}Please enter a name with 10 or less character \n""")
        else:
            print(f"Godd luck, {name} !")
            break


def run_quiz():
    """
    Iterate
    """
    pass


start()
