from dataclasses import dataclass
from PySide6.QtWidgets import (QVBoxLayout, QPushButton, QLabel, QRadioButton, QMessageBox, QMainWindow)
from PySide6.QtGui import(QPixmap)
from oop_test_model import oop_questions, current_question_index
import os
@dataclass
class OOPQuestionController:
    """Class for controlling the GUI"""
    main_layout: QVBoxLayout
    dialouge_label: QLabel
    next_button: QPushButton 
    code_snip_label: QLabel
    question_label: QLabel
    answer_one_button: QRadioButton
    answer_two_button: QRadioButton
    answer_three_button: QRadioButton
    submit_button: QPushButton
    secondary_window: QMainWindow
    answer_status_label: QLabel
    question_info_label: QLabel

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
        
        # for functionality/development, (back and forth with buttons)
    
    def get_current_question(self):
        # Get list of question objects
        question_set = oop_questions.questions
        # Match the current question index to a question order
        for question in question_set:
            if question.index == current_question_index:
                current_question = question
        return current_question
    
    def show_question(self):
        global current_question_index
        # Clear the starting page layout only if it is on the layout
        if current_question_index == 1:
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
        global answer_buttons
        answer_buttons = [self.answer_one_button, self.answer_two_button, self.answer_three_button]
        self.main_layout.addWidget(self.submit_button)
        # Get the current question
        current_question = self.get_current_question()
        # Add infomation about the question to GUI
        self.question_label.setText(current_question.question) 
        # Code from onslowcollege.github (to display code snippet)
        # --
        path = os.path.dirname(os.path.abspath(__file__)) #load path to file
        pixmap = QPixmap(os.path.join(path, current_question.pixmap_filename))
        self.code_snip_label.setPixmap(pixmap)
        # --
        # Add answers from a dictionary to buttons
        global answer_list
        answer_list = current_question.answer_list 

        for button in answer_buttons:
            index = answer_buttons.index(button)
            answer = answer_list[index]
            button.setText(answer)

    def answer_button_clicked(self):
        """"Get the selected answer""" 
        # Get the index of selected answer button from global answer_buttons
        for button in answer_buttons:
            if button.isChecked():
                current_answer_index = answer_buttons.index(button)
        # Use index to get corresponding answer from global answer_list
        current_answer = answer_list[current_answer_index]
        # Return the correct answer for the current question
        correct_answer = self.get_current_question().get_correct_answer
        # Check if the answer is correct and store result in a variable
        global answer_status
        answer_status = ""
        if current_answer == correct_answer:
            answer_status = True
        else:
            answer_status = False
        print(answer_status)
        
        # for functionality/development, (check highlight button selected) (Change from push to radio buttons)

    def submit_button_clicked(self, checked: bool):
        # Check that a radio button has been selected
        if answer_status == "":
            print("answer is empty")
            #QMessageBox(QMessageBox.Icon.Warning, f"Error", f"Please select an answer before moving on")
        else:
            # clear all the question page widgets
            # bring up a window saying if answer is correct or not, post informational dialouge
            self.secondary_window.show()
            if answer_status == True:
                self.answer_status_label.setText("Correct")
            else:
                self.answer_status_label.setText("Incorrect")
            # Display info about the current question
            info = self.get_current_question().info
            self.question_info_label.setText(info)

            

            # for usability, show the correct answer if answer is wrong
            # reset answer status
            
            

        # Increment current index
        current_question_index =+ 1 
        # Reset the answer status for the next question


    def __post_init__(self):
        """Connect signal functions to GUI"""
        self.next_button.clicked.connect(self.next_button_clicked)
        self.answer_one_button.clicked.connect(self.answer_button_clicked)
        self.answer_two_button.clicked.connect(self.answer_button_clicked)
        self.answer_three_button.clicked.connect(self.answer_button_clicked)
        self.submit_button.clicked.connect(self.submit_button_clicked)
# Ask Question
# Show code snippet and buttons for answers

# Mark answer, if answer is wrong, explain how, add 100 points

# Offer a randomised reward

# Loop, update points and percentage

# Once all questions are asked, show end messages
# Show leaderboard