from dataclasses import dataclass
from PySide6.QtWidgets import (QVBoxLayout, QPushButton, QLabel, QRadioButton, QMessageBox, QMainWindow, QWidget, QHBoxLayout)
from PySide6.QtGui import(QPixmap)
from oop_test_model import oop_questions, current_question_index
import os
from PySide6.QtCore import Qt

@dataclass
class OOPQuestionController:
    """Class for controlling the GUI"""
    main_window: QMainWindow
    main_layout: QVBoxLayout
    dialouge_label: QLabel
    bottom_button_widget: QPushButton
    next_button: QPushButton 
    back_button: QPushButton
    points_label: QLabel
    oop_quiz_label: QLabel
    code_snip_label: QLabel
    question_label: QLabel
    answer_one_button: QRadioButton
    answer_two_button: QRadioButton
    answer_three_button: QRadioButton
    submit_button: QPushButton
    secondary_window: QMainWindow
    answer_status_label: QLabel
    question_info_label: QLabel
    reward_info_label: QLabel
    certain_reward_button: QPushButton
    uncertain_reward_button: QPushButton
    top_widget : QWidget
    top_layout: QHBoxLayout
    middle_widget: QWidget
    middle_layout: QHBoxLayout
    left_middle_widget: QWidget
    left_middle_vbox: QVBoxLayout
    right_middle_widget: QWidget
    right_middle_vbox: QVBoxLayout
    bottom_widget: QWidget
    bottom_layout: QHBoxLayout

    def get_current_dialouge(self):
        """Gets the text of the current how to play dialouge that's showing"""
        # Explain game in slides
        # List of dialouges
        how_to_play = [
            ("The OOP quiz contains a\nseries of questions\nrelating to oop"),
            ("Answer correctly to get 100\npoints"),
            ("After answering a question,\nchoose to gamble or recieve\nthe 100 dollar reward if you\nanswer the next question\ncorrectly"),
            ("You start with 100 points"),
            ("Let's begin")
        ]
        # If its showing the welcome message
        if self.dialouge_label.text() == ("Welcome to the OOP Quiz!"):
            index = -1
            next_text = how_to_play[index + 1]
            back_text = ""
        # If its on the last dialouge
        elif self.dialouge_label.text() == ("Let's begin"):
            index = 4
            next_text = ""
            back_text = how_to_play[index - 1]
        else:
            index = how_to_play.index(self.dialouge_label.text()) 
            next_text = how_to_play[index + 1]
            back_text = how_to_play[index - 1]
        return next_text, back_text, index

    def next_button_clicked(self, checked: bool):
        # Set text based on what is currently in the dialouge label
        next_text, back_text, index = self.get_current_dialouge()
        self.dialouge_label.setText(next_text)
        # If the text has changed from the welcome label, show the back button to the gui
        if back_text == "":
            self.main_layout.addWidget(self.back_button)
            self.back_button.show()
        # If its showing the last message, bring up question page
        elif next_text == "":
            self.show_question()
        # User starts with 100 points, on the first question, if they answer correctly they get another 100, incorrect, they get no points
        global points
        points = 100
        global points_receivable
        points_receivable = 100
        global points_deductable
        points_deductable = 0
        
    def back_button_clicked(self):
        # Set text based on what is currently in the dialouge label
        next_text, back_text, index = self.get_current_dialouge()
        self.dialouge_label.setText(back_text)
        # If we're going back from the first dialoge slide, remove back button and show welcome message
        if index == 0:
            self.back_button.hide()
            self.dialouge_label.setText("Welcome to the OOP Quiz!")
    
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
        print(current_question_index)
        # Clear the starting page layout only if it is on the layout
        if current_question_index == 1:
            self.main_layout.removeWidget(self.dialouge_label)
            self.main_layout.removeWidget(self.next_button)
            self.main_layout.removeWidget(self.back_button)
            self.dialouge_label.deleteLater()
            self.next_button.deleteLater()
            self.back_button.deleteLater()
            self.main_layout.removeWidget(self.bottom_button_widget)
            self.bottom_button_widget.deleteLater()
            # Set up and style question page
            # Top
            self.main_layout.addWidget(self.top_widget)
            self.top_widget.setLayout(self.top_layout)
            self.top_layout.addWidget(self.oop_quiz_label)
            self.oop_quiz_label.setAlignment(Qt.AlignTop)
            self.top_layout.addWidget(self.points_label)
            self.points_label.setAlignment(Qt.AlignTop)
            self.points_label.setAlignment(Qt.AlignRight)
            self.top_widget.setStyleSheet("QWidget { font-size : 16px }")
            # Middle 
            middle_widget = QWidget()
            self.main_layout.addWidget(middle_widget)
            middle_layout = QHBoxLayout()
            middle_widget.setLayout(middle_layout)
            left_middle_widget = QWidget()
            middle_layout.addWidget(left_middle_widget)
            left_middle_vbox = QVBoxLayout()
            left_middle_widget.setLayout(left_middle_vbox)
            left_middle_vbox.addWidget(self.question_label)
            self.question_label.setAlignment(Qt.AlignCenter)
            left_middle_widget.setStyleSheet("QWidget { font-size : 16px }")
            left_middle_vbox.addWidget(self.code_snip_label)
            right_middle_widget = QWidget()
            middle_layout.addWidget(right_middle_widget)
            right_middle_vbox = QVBoxLayout()
            right_middle_widget.setLayout(right_middle_vbox)
            right_middle_vbox.addWidget(self.answer_one_button)
            right_middle_vbox.addWidget(self.answer_two_button)
            right_middle_vbox.addWidget(self.answer_three_button)
            global answer_buttons
            answer_buttons = [self.answer_one_button, self.answer_two_button, self.answer_three_button]
            # Bottom
            bottom_widget = QWidget()
            self.main_layout.addWidget(bottom_widget)
            bottom_layout = QHBoxLayout()
            bottom_widget.setLayout(bottom_layout)
            bottom_layout.addWidget(self.submit_button)
        # Set the answer status to null if its the first question
        global answer_status
        answer_status = ""
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
        # Display points
        global points
        self.points_label.setText(f"Points: {points}")
        # Set all the answer buttons to unchecked
        # Add answer text to buttons
        for button in answer_buttons:
            button.setAutoExclusive(False)
            button.setChecked(False)
            index = answer_buttons.index(button)
            answer = answer_list[index]
            button.setText(answer)
            # Make the buttons auto exclusive again
            button.setAutoExclusive(True)

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
        if current_answer == correct_answer:
            answer_status = True
        else:
            answer_status = False
        print(answer_status)
        
    def submit_button_clicked(self, checked: bool):
        # Check that a radio button has been selected
        if answer_status == "":
            QMessageBox(QMessageBox.Icon.Warning, f"Error", f"Please select an answer before moving on").exec()
        # If the current question is the last, then show the last page
        elif current_question_index == 12:
            self.show_end_page()
        else:
            # bring up a window saying if answer is correct or not, post informational dialouge
            self.secondary_window.show()
            self.main_window.hide()
            global points
            global points_receivable
            global points_deductable
            if answer_status == True:
                self.answer_status_label.setText(f"Correct!\nYou have won {points_receivable} points!")
                points += points_receivable
                self.question_info_label.setText("")
            else:
                if points_deductable == 0:
                    self.answer_status_label.setText(f"Incorrect.\nYour points stay the same.")
                else:
                    self.answer_status_label.setText(f"Incorrect.\nYou have lost {points_deductable} points!")
                points -= points_deductable
                # Display info about the current question
                info = self.get_current_question().info
                self.question_info_label.setText(info)

    def certain_reward_button_clicked(self):
        """If user chooses the certain reward, set their points receivable to 100"""
        global points_receivable
        points_receivable = 100
        global points_deductable
        points_deductable = 0
        
        # Increment current index # Reset the answer status for the next question
        global current_question_index
        new_question_index = current_question_index + 1
        current_question_index = new_question_index
        # Ask next question
        self.secondary_window.hide()
        self.main_window.show()
        self.show_question()
        
    def uncertain_reward_button_clicked(self):
        """If user chooses the uncertain reward, they either double their points or halve them"""
        global points
        global points_receivable
        global points_deductable
        points_receivable = points
        points_deductable = points / 2
        # Increment current index # Reset the answer status for the next question
        global current_question_index
        new_question_index = current_question_index + 1
        current_question_index = new_question_index
        # Ask next question
        self.secondary_window.hide()
        self.main_window.show()
        self.show_question()
    
    def show_end_page(self):
        # Remove all widgets from the question page
        self.top_layout.removeWidget(self.oop_quiz_label)
        self.top_layout.removeWidget(self.points_label)
        self.main_layout.removeWidget(self.top_widget)
        self.oop_quiz_label.deleteLater()
        points = self.points_label.text()
        self.points_label.deleteLater()
        self.top_widget.deleteLater()
        self.main_layout.removeWidget(self.middle_widget)
        self.middle_layout.removeWidget(self.left_middle_widget)
        self.left_middle_vbox.removeWidget(self.question_label)
        self.left_middle_vbox.removeWidget(self.code_snip_label)
        self.middle_layout.removeWidget(self.right_middle_widget)
        self.right_middle_vbox.removeWidget(self.answer_one_button)
        self.right_middle_vbox.removeWidget(self.answer_two_button)
        self.right_middle_vbox.removeWidget(self.answer_three_button)
        self.main_layout.removeWidget(self.bottom_widget)
        self.bottom_layout.removeWidget(self.submit_button)
        self.middle_widget.deleteLater()
        self.left_middle_widget.deleteLater()
        self.question_label.deleteLater()
        self.code_snip_label.deleteLater()
        self.right_middle_widget.deleteLater()
        self.answer_one_button.deleteLater()
        self.answer_two_button.deleteLater()
        self.answer_three_button.deleteLater()
        self.bottom_widget.deleteLater()
        self.submit_button.deleteLater()
        # Set up the final page
        final_points_label = QLabel(f"Game Over.\n\nTotal {points}\nCongratulations")
        self.main_layout.addWidget(final_points_label)
        final_points_label.setAlignment(Qt.AlignCenter)
        final_points_label.setStyleSheet("QLabel { font-size: 16px, }")


    def __post_init__(self):
        """Connect signal functions to GUI"""
        self.next_button.clicked.connect(self.next_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)
        self.answer_one_button.clicked.connect(self.answer_button_clicked)
        self.answer_two_button.clicked.connect(self.answer_button_clicked)
        self.answer_three_button.clicked.connect(self.answer_button_clicked)
        self.submit_button.clicked.connect(self.submit_button_clicked)
        self.certain_reward_button.clicked.connect(self.certain_reward_button_clicked)
        self.uncertain_reward_button.clicked.connect(self.uncertain_reward_button_clicked)
