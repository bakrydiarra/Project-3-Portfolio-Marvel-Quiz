"Quiz material"


class Question:
    """
    Creating a class questions as purpose to be used in a for loop iteration
    """
    def __init__(self, item, answer, choice):
        self.item = item
        self.answer = answer
        self.choice = choice

    def __repr__(self):
        return '{' + self.item + ',' + self.answer + ','\
             + str(self.choice) + '}'


quiz_questions = [
    Question("Where is Captain America from?", "b", ["(a) Chicago", "(b) Brooklyn", "(c) Cleveland"]),
    Question("The shield of Captain America is made of what?", "c", ["(a) Tetranium", "(b) Palladium", "(c) Vibranium"]),
    Question("What is the metal inside Wolverine?", "b", ["(a) Tetranium", "(b) Adamantium", "(c) Krytasium"]),

]
