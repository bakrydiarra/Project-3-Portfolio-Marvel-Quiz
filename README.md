# Marvel Quiz

## Project Portfolio 3 - Full Stack Development 
##  Python Essentials
---


# Site Info

* The Marvel Quiz is a game is a simple straight forward quiz that suits everyone who'd like to test his/her marvel knowledge.
* This is my Project Portfolio 3 submission for Code Institute's Diploma in Web Application Development course.It is basic command-line application based on the programing language Python.
  - Live website [here]
 ---

# Index – Table of Contents
* [User Experience (UX)](#user-experience-ux)
* [Features](#features)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
---

# User Experience (UXD)

## Target Audiance
 
 - This project targets an inclusive audiance. The only prerequisites is a good comprehension of the english language.

## Objectives

 - Simple and entertainng quiz game application.
 - Clear inforamation delivered to proceed throught the game.
 - deliver a score at the end of the game.

## User stories

 - As a user I  can:

   - see a title indicating the purpose of the app
   - see clear, short, and concise instructions
   - enter his/her name to initiate the game
   - receive feedback when the name chosen isn't valid
   - receive an encouragement word to start the quiz when the name is valid
   - read clear questions with mutliple choice answer identified with the letter a, b and c
   - enter his answer using a, b. or c
   - recive a feedback when the answer is not valid
   - receive a feedback about the correctness of his/her answer
   - receive a score from 0 to 100 out of 100
   - reset the game for another play
   - quit the game 

## Technical Design
   
  ![Flowchart](docs/Flowchart.jpg)


## Data Model

  - The application is based on three simple compartmentalised module.
  This helps to avoid overloading the main module run.py and makes the code easier to read. 
  The class structure in the quiz.py with the list quiz_questions allow us in the future to extend the number of question without readjusting other codes. 
  The main logic of the code is based on the iteration of a for loop in the list quiz_questions which takes its structure from the class Question. 
  The username’s  answer are compared to the solution contained in the quiz_questions list.
  To initiate the game, the user must  fulfil the criteria fixed by the function validate_name. The database model is quite simple and linear.

  
  ---


   
# Features

### Existing Features

### Welcome & Instructions screen

### Username Feedback

### Questions & Choices

### Answer Feedback

### Score & Play again choice

### Reset Game

### Quit Game




### Features which could be implemented in the future

 
 ---

## Testing

### Validator Testing

---
 

 Testing the user experience

| Feature | Expect | Action | Result |
| :--- | :--- | :--- | :--- |
| XXX | 4x4 grid style game, title, two buttons | clicked live link| positive | 
| Start Game| By clicking a card | clicked a card | postive |


---

# Deployment


---
 

 
# Credits 

### Technologie used

### Languages Used 
    - Python - To create a command-line application.

### Tools and Other Resources Used:

 - [Github](https://github.com/) -  for version control and pushing content to repository.
 - [Heroku](https://id.heroku.com/login) - for deployment.
 - [Gitpod](https://www.gitpod.io/)  -  for editting code.
 - [Love Sandwiches](https://github.com/bakrydiarra/love-sandwiches) - for inspiration and understanding practice coding with the python.  
 - [W3 Schools](https://www.w3schools.com/) - for understanding Python's logic and syntax. 
 - [Lucid](https://lucid.app/users/login#/login) - for creating a flowchart.
 - [Python Linter](https://pep8ci.herokuapp.com/)- for validating python code.
 - [Patorjk.com](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - for creating ASCII text.
 - [Bro Code](https://github.com/beratzorlu/python-quiz/blob/main/README.md#libraries) - for understanding the logic of a quiz game:
   - [QUIZ GAME written in Python](https://www.youtube.com/watch?v=zehwgTB0vV8)
   - [Python quiz game](https://www.youtube.com/watch?v=yriw5Zh406s)
 - [Dev.to How to build a Quiz Game in Python](https://dev.to/mindninjax/how-to-build-a-quiz-game-in-python-10ik) - or understanding the logic of a quiz game.
 - [Python: Print ascii art](https://www.youtube.com/watch?v=arcFqEuV_XQ) - for understanding the use of ASCII.
 - [Geeks for Geeks](https://www.geeksforgeeks.org/print-colors-python-terminal/) - for understanding the use of colors in python.
 

### Libraries

  - Local libraries:
    - os
    - sleep

  - Third party Library:
    - colorama

### Code Used
  
 - [Gitpod Full Template](https://github.com/Code-Institute-Org/python-essentials-template) -  used as a template for the gitpod environment.
 - [Python if __name__ == __main__ Explained](https://www.freecodecamp.org/news/if-name-main-python-example/) - used to make sure the function start run as main programm.
 - [W3docs](https://www.w3docs.com/snippets/python/how-to-clear-the-interpreter-console.html) - used to clear the screen.



### Content
 
 - The quiz content came from the source below:
   - [Parade](https://parade.com/1192384/alexandra-hurtado/marvel-trivia-quiz/)
   - [QuizBreaker](https://www.quizbreaker.com/marvel-trivia#)

- I wrote the multiple choice content.


## Acknowledgments

 - Many thanks to my Mentor Antonio Rodriguez for helpful feedback, industry insights and recommended tools.
 - Many thanks to my friends (Marjorie and Louise) and family for helping me testing the website and for their precious feedbacks.