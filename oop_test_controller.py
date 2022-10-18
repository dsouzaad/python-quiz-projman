from dataclasses import dataclass
from PySide6.QtWidgets import (QVBoxLayout, QPushButton, QLabel)
from oop_test_model import oop_questions, current_question_index

@dataclass
class OOPQuestionController:
    """Class for controlling the GUI"""
    main_layout: QVBoxLayout
    dialouge_label: QLabel
    next_button: QPushButton 
    code_snip_label: QLabel
    question_label: QLabel
    answer_one_button: QLabel
    answer_two_button: QLabel
    answer_three_button: QLabel
    submit_button: QPushButton




    def next_button_clicked(self, checked: bool):
        # Explain game in slides
        # List of dialouges
        how_to_play = [
            ("The OOP quiz contains a series of questions relating to oop"),
            ("Answer correctly to get 100 points"),
            ("After answering a question, choose to gamble or recieve the 100 dollar reward if you answer the next question correctly"),
            ("You start with 100 points"),
            ("Let's begin")
        ]
        # Set text based on what is currently in the dialouge label
        # If its showing the welcome message
        if self.dialouge_label.text() == ("Welcome to the OOP Quiz!\n Start by entering your name"):
            self.dialouge_label.setText(how_to_play[0])

        # If its showing the last message,bring up first question 
        elif self.dialouge_label.text() == how_to_play[len(how_to_play) - 1]:
            self.show_question()

        else:
            string_index = how_to_play.index(self.dialouge_label.text())
            self.dialouge_label.setText(how_to_play[string_index + 1])
        # Can go back and forth with buttons
    
    def show_question(self):
        # Clear the layout
            self.main_layout.removeWidget(self.dialouge_label)
            self.main_layout.removeWidget(self.next_button)
            self.dialouge_label.deleteLater()
            self.next_button.deleteLater()

            # Set up question page
            self.main_layout.addWidget(self.code_snip_label)
            self.main_layout.addWidget(self.question_label)
            self.main_layout.addWidget(self.answer_one_button)
            self.main_layout.addWidget(self.answer_two_button)
            self.main_layout.addWidget(self.answer_three_button)
            self.main_layout.addWidget(self.submit_button)

            self.question_label.setText(oop_questions[current_question_index])

    def submit_button_clicked(self, checked: bool):
        pass



    def __post_init__(self):
        """Connect signal functions to GUI"""
        self.next_button.clicked.connect(self.next_button_clicked)
        self.submit_button.clicked.connect(self.submit_button_clicked)
# Ask Question
# Show code snippet and buttons for answers

# Mark answer, if answer is wrong, explain how, add 100 points

# Offer a randomised reward

# Loop, update points and percentage

# Once all questions are asked, show end messages
# Show leaderboard