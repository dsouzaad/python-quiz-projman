from dataclasses import dataclass
@dataclass
class Question:
    """Class representing a question in the quiz"""
    _index: int
    _question: str
    _answers: dict
    _info: str

    @property
    def index(self) -> int:
        """Returns the place of the question in the question order"""
        return self._index

    @property
    def question(self) -> str:
        """Returns the question"""
        return self._question

    @property
    def answers(self) -> dict:
        """Returns a dictionary of answers and if they are right or wrong"""
        return self._answers

    @property
    def info(self) -> str:
        """Returns information about the question"""
        return self._info

    @property
    def answer_list(self) -> list:
        """Returns a list of answers for a question"""
        answer_list = []
        for answer in self.answers.keys():
            answer_list.append(answer)
        return answer_list

    @property
    def get_correct_answer(self) -> str:
        """Returns the correct answer as a string"""
        for answer in self.answers.keys():
            # Get the value of the key, if value is true, the answer is correct
            value = self.answers[answer]
            if value == True:
                correct_answer = answer
        return correct_answer
    
    @property
    def pixmap_filename(self) -> str:
        return f"code_snip{self.index}.png"
@dataclass
class QuestionSet:
    """Class representing a question in the quiz"""
    _questions: list

    @property
    def questions(self) -> list:
        """Returns a list of questions"""
        return self._questions

# Create a list of questions
oop_questions = QuestionSet(
    [
    Question(1, "1. How can the Members be protected?", {"Put an Underscore ( _ ) before\neach Member" : True, "Put Brackets around each Member" : False, "Double Underscores before and\nafter each Member is defined" : False}, "The correct answer was: Put an\nUnderscore ( _ ) before each\nMember. This signals to developers\nnot to access the member directly."),
    Question(2, "2. What is the function of this code?", {"Setter: allows the ‘type’\nMember to be changed to a valid\ninput" : False, "Returns the variables ‘self’\nand ‘type’" : False, "Getter: it allows the ‘type’\nMember to be accessed safely" : True}, "The correct answer was: Getter:\nit allows the ‘type’ Member\nto be accessed safely"),
    Question(3, "3. Which block of code correctly\ninstantiates an Object?", {"#1" : True, "#2" : False, "#3" : False}, "The correct answer was #1: (apple = Fruit(“rose”, 3, 100, 0.25)"),
    Question(4, "4. What is a Member?", {"A Function in a Class": False, "A value stored in a Class or\nObject" : True, "A Variable made based on a Class": False}, "The correct answer was: A value stored in a Class or Object"),
    Question(5, "5. What do the bottom two lines\nof code represent?", {"A Property" : False, "A Method" : True, "A Function" : False}, "The correct answer was: A method.\nA method is a function inside of a Class."),
    Question(6, "6. What do the bottom two lines\nof code do?", {"Declare a Class that can be\nreferred to as either Fruit or\nProduce, interchangeably" : False, "Declare Fruit as a Superclass\nof Produce" : False, "Declare Fruit as a Subclass of\nProduce" : True}, "The correct answer was:\nFruit is a subclass of Produce"),
    Question(7, "7. Which is NOT a true of a\nProtocol?", {"A Class that inherits a Protocol\ncan only have the Methods\noutlined in the Protocol." : True, "Contains Methods with no code\n(they only pass)" : False, "Any Class that inherits a\nProtocol must have the same\nMethods as the Protocol (instead\nof passing, they contain code)" : False}, "The correct answer was:\nA Class that inherits a Protocol\ncan only have the Methods outlined\nin the Protocol"),
    Question(8, "8. Select the false statement\nabout immutable properties.", {"Immutable Properties are Members\nthat cannot be changed after\nthey are initially defined" : False, "Immutable Properties have no\nSetters" : False, "Immutable Properties cannot be\nused in Methods " : True}, "The correct answer was:\nImmutable Properties cannot be used\nin methods. This is false as immutable\nproperties can in fact be used in methods."),
    Question(9, "9. Which of the following is\nNOT a benefit of object-oriented\nprogramming?", {"Preventing variables from\nchanging without the new value\nbeing checked" : False, "Eliminates need for comments" : True, "Having all information about a\ncomponent in one variable" : False}, "The correct answer was:\nEliminates the need for comments"),
    Question(10, "10. What do the bottom two lines\n of code do? ", {"Add a new Member called price to\nthe object variable ‘apple’ that\nhas a value of 0.75" : False, "Increase the price of an apple\nby 0.75" : False, "Change the price of an apple\nto 0.75" : True}, "The correct answer was:\nChange the price of an apple to 0.75"),
    Question(11, "11. Which line will print the\nripeness of an Apple?", {"1" : True, "2" : False, "3" : False}, "The correct answer was #1"),
    Question(12, "12. How should the code be\nchanged so follows convention?", {"Replace @dataclass with @property" : False, "Replace the ‘=’ symbols with “:”\nsymbols" : True, "Decapitalize Class names" : False}, "The correct answer was: Replace the ‘=’ symbols with “:” symbols"),
    ]
)
current_question_index = 1
