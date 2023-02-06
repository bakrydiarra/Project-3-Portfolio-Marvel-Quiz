"Questions and answers to be imported to run.py "


class Question:
    """
    Creating a class question as purpose to be used in a for loop
    using a def__rep__ to make sure the class object will be
    printed as a string
    ref: https://www.educative.io/answers/what-is-the-repr-method-in-python
    the concrete implementation of this class - Objects - will be contained in
    a list which allows us to add continually new questions if needed
    """
    def __init__(self, item, answer, choice):
        self.item = item
        self.answer = answer
        self.choice = choice

    def __repr__(self):
        return '{' + self.item + ',' + self.answer + ','\
             + self.choice + '}'


quiz_questions = [
    Question("1. Where is Captain America from", "b", ["a. Chicago",
             "b. Brooklyn", "c. Cleveland"]),
    Question("2. The shield of Captain America is made of what", "c",
             ["a. Tetranium", "b. Palladium", "c. Vibranium"]),
    Question("3. What is the metal inside Wolverine", "b",
             ["a. Tetranium", "b. Adamantium", "c. Krytasium"]),
    Question("4. What was the skin color  of the original Hulk", "c",
             ["a. blue", "b. yellow", "c. gray"]),
    Question("5. Which country is the birthplace of Black Widow",
             "c", ["a. Belarus", "b. Ukraine", "c. Russia"]),
    Question("6. Who is the brother of Scarlet Witch", "a",
             ["a. Quicksilver", "b. Deathstrike", "c. Silverburn"]),
    Question("7. Who does the Mad Titan sacrifice to acquire the Soul Stone",
             "b", ["a. Nebulla", "b. Gamora", "c. Ramonda"]),
    Question("8. Who is the sister of the Black Panther", "c",
             ["a. Nakia", "b. Sooki", "c. Shuri"]),
    Question("9. What color is the power stone", "a",
             ["a. purple", "b. green", "c. red"]),
    Question("10. Who is the Winter Soldier", "b",
             ["a. Hawkeye", "b. Bucky", "c. Heimdall"])
]
