"Questions and answers to be imported to run.py "


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
    Question("Where is Captain America from", "b", ["(a) Chicago", "(b) Brooklyn", "(c) Cleveland"]),
    Question("The shield of Captain America is made of what", "c", ["(a) Tetranium", "(b) Palladium", "(c) Vibranium"]),
    Question("What is the metal inside Wolverine", "b", ["(a) Tetranium", "(b) Adamantium", "(c) Krytasium"]),
    Question("What was the skin color  of the original Hulk", "c", ["(a) blue", "(b) yellow", "(c) gray"]),
    Question("Which country is the birthplace of Black Widow", "c", ["(a) Belarus", "(b) Ukraine", "(c) Russia"]),
    Question("Who is the brother of Scarlet Witch", "a", ["(a) Quicksilver", "(b) Deathstrike", "(c) Silverburn"]),
    Question("Who does the Mad Titan sacrifice to acquire the Soul Stone", "b", ["(a) Nebulla", "(b) Gamora", "(c) Ramonda"]),
    Question("Who is the sister of the Black Panther", "c", ["(a) Nakia", "(b) Sooki", "(c) Shuri"]),
    Question("What color is the power stone", "a", ["(a) purple", "(b) green", "(c) red"]),
    Question("Who is the Winter Soldier", "b", ["(a) Hawkeye", "(b) Bucky", "(c) Heimdall"])
]
