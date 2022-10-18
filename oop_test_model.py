from dataclasses import dataclass

#@dataclass
#class Reward:
@dataclass
class Question:
    """Class representing a question in the quiz"""
    _order: int
    _question: str
    _answers: dict
    _info: str

    @property
    def order(self) -> int:
        """Returns the place of the question in the question order"""
        return self._order

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
    def pixmap_filename(self) -> str:
        return f"code_snip{self.order}.png"

@dataclass
class QuestionSet:
    """Class representing a question in the quiz"""
    _questions: list

    @property
    def questions(self) -> list:
        """Returns a list of questions"""
        return self._questions

@dataclass
class Player:
    """Class representing a quiz taker"""
    _name: str
    _points: 100
    _accuracy: float

    @property
    def name(self) -> str:
        """Returns player's name"""
        return self._name

    @name.setter
    def name(self, new_name):
        """Player name can be changed to another string"""
        if len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Cannot change player name to an empty string")
    
    @property
    def points(self) -> float:
        """Return the user's points"""
        return self._points

    #DON'T KNOW THAT THIS WILL WORK, WE'LL SEE
    @points.setter
    def points(self, new_points):
        """Can update points"""
        self._points = new_points

    @property
    def accuracy(self) -> float:
        """Returns percentage of correctly answered questions by the player"""
        return f"{self._accuracy}%"
    
    @accuracy.setter
    def accuracy(self, new_accuracy):
        """Can update accuracy"""
        self._accuracy = new_accuracy

# Create a list of questions
oop_questions = QuestionSet(
    [
    Question(1, "", {}, ""),
    Question(2, "", {}, ""),
    Question(3, "", {}, ""),
    Question(4, "", {}, ""),
    Question(5, "", {}, ""),
    Question(6, "", {}, ""),
    Question(7, "", {}, ""),
    Question(8, "", {}, ""),
    Question(9, "", {}, ""),
    Question(10, "", {}, ""),
    Question(11, "", {}, ""),
    Question(12, "", {}, ""),
    Question(13, "", {}, ""),
    Question(14, "", {}, ""),
    Question(15, "", {}, ""),
    Question(16, "", {}, ""),
    Question(17, "", {}, ""),
    Question(18, "", {}, ""),
    ]
)

current_question_index = 0
