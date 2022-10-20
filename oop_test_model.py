from dataclasses import dataclass

#@dataclass
#class Reward:
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
    Question(1, "Question goes here", {"1" : False, "2" : True, "3" : False}, "Info about question goes here"),
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
current_question_index = 1
