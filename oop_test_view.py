from os import fsdecode
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton)
from oop_test_model import oop_questions
from oop_test_controller import OOPQuestionController

# Set up app and main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle("OOP Quiz")
main_window.resize(700, 500)

secondary_window = QMainWindow()
secondary_window.setWindowTitle("Hilo")


# Set up main widget
main_widget = QWidget()
main_window.setCentralWidget(main_widget)
main_layout = QVBoxLayout()
main_widget.setLayout(main_layout)

# Set up second window widget
secondary_widget = QWidget()
secondary_window.setCentralWidget(secondary_widget)
secondary_layout = QVBoxLayout()
secondary_widget.setLayout(secondary_layout) 

answer_status_label = QLabel() # Displays if selected answer is right or wrong
question_info_label = QLabel() # Displays information about the question
secondary_layout.addWidget(answer_status_label)
secondary_layout.addWidget(question_info_label)

reward_info_label = QLabel("Select your reward for the next question")
certain_reward_button = QPushButton("Get 100 points if i answer correctly and 0 points if answer incorrectly")
uncertain_reward_button = QPushButton("Double my points if i answer correctly and half my points if i answer incorrectly")

secondary_layout.addWidget(reward_info_label)
secondary_layout.addWidget(certain_reward_button)
secondary_layout.addWidget(uncertain_reward_button)

# Set up initial page
dialouge_label = QLabel("Welcome to the OOP Quiz!")
next_button = QPushButton("Next")
main_layout.addWidget(dialouge_label)
main_layout.addWidget(next_button)

# Set up question page
points_label = QLabel()
code_snip_label = QLabel()
question_label = QLabel()
answer_one_button = QRadioButton()
answer_two_button = QRadioButton()
answer_three_button = QRadioButton()
submit_button = QPushButton("Submit")


# Set up controller
controller = OOPQuestionController(main_layout, dialouge_label, next_button, points_label, code_snip_label, question_label, answer_one_button, answer_two_button, answer_three_button, submit_button, secondary_window, answer_status_label, question_info_label, reward_info_label, certain_reward_button, uncertain_reward_button)

main_window.show()
app.exec()
