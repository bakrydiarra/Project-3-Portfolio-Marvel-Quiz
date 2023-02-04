"""
Import libraries needed to the function of this application.
"""
import time
from time import sleep
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
from logo import TITLE
from quiz import Question
from quiz import quiz_questions


def start():
    """
    Display logo and instructions of the quiz.
    Asking username input to run the quiz.
    """
    print(TITLE)
    print("Welcome to the superheroes universe!\n")
    time.sleep(1)
    print("Are you ready to test your knowledge?\n")
    time.sleep(1)
    print("You have 10 multiple choice questions.\n")
    time.sleep(1)
    print("Select your answer typing 'a', 'b' or 'c'.\n")
    time.sleep(1)
    validate_name()
    run_quiz()


def validate_name():
    """
    validation of the username to start the game
    """
    while True:
        name = input("Enter your name to start the quiz: \n")
        name = name.strip().lower()
        print("")
        if len(name) > 10:
            print(f"""{Fore.RED}Please enter a name with 10 or less character \n""")
        else:
            print(f"Godd luck, {name} !")
            print("")
            break


def run_quiz():
    """
    Iterate through the questions list.
    Iterate through the choice list.
    Get user input-answer.
    validate user input-answer: invalid, correct,wrong.
    Implementing score +=10 for a good answer.
    """
    global user_answer
    score = 0

    for question in quiz_questions:
        print(f"{question.item}?")
        for option in question.choice:
            print(option)
        user_answer = input("Enter your answer: \n")
        if user_answer.lower() not in ["a", "b", "c"]:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid answer! Pick: a, b or c.")
            print("")
            user_answer = input("Enter your answer: \n")
        if user_answer.lower() == question.answer.lower():
            print(f"{Fore.GREEN} Well done!")
            score += 10
        else:
            print(f"{Fore.RED}Sorry, wrong answer!")
    final_score(score)


def final_score(score):
    """
    Display score
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


start()
