"""
Import libraries needed to the function of this application.
"""
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
from logo import TITLE


def start():
    """
    Display logo and instructions of the quiz
    """
    print(TITLE)
