from os import fsdecode
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QRadioButton
)
from oop_test_model import oop_questions
from oop_test_controller import OOPQuestionController
from PySide6.QtCore import Qt

# Set up app and main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle("OOP Quiz")
main_window.resize(700, 500)
app.setStyleSheet("""
QWidget {
    color : rgb(30, 30, 30);
    font-size : 14px;
    font-family : courier new;
    }
""")

# Set up main widget
main_widget = QWidget()
main_window.setCentralWidget(main_widget)
main_layout = QVBoxLayout()
main_widget.setLayout(main_layout)

reward_info_label = QLabel("Select your reward for the next question below: ")
certain_reward_button = QPushButton("""
Correct answer gets 100pts, a Wrong \
answer gets 0 pts
""")
uncertain_reward_button = QPushButton("""Correct answer gets x2 points, Wrong \
answer halves my points""")

# Set up second window
secondary_window = QMainWindow()
secondary_window.setWindowTitle("Bet Page")
secondary_window.resize(700, 500)
secondary_widget = QWidget()
secondary_window.setCentralWidget(secondary_widget)
secondary_layout = QVBoxLayout()
secondary_widget.setLayout(secondary_layout)
answer_status_label = QLabel()  # Displays if selected answer is right or wrong
question_info_label = QLabel()  # Displays information about the question
secondary_layout.addWidget(answer_status_label)
answer_status_label.setStyleSheet("QLabel { font-size: 16px; }")
answer_status_label.setAlignment(Qt.AlignCenter)
secondary_layout.addWidget(question_info_label)
question_info_label.setAlignment(Qt.AlignCenter)
secondary_layout.addWidget(reward_info_label)
reward_info_label.setStyleSheet("QLabel { font-size: 16px; }")
reward_info_label.setAlignment(Qt.AlignCenter)
secondary_layout.addWidget(certain_reward_button)
secondary_layout.addWidget(uncertain_reward_button)
secondary_window.setStyleSheet("""
    QPushButton {
        background-color : rgb(251, 203, 7);
        border-radius: 10%;
        height: 50px;
        width: 50%;
        font-size : 15px
    }
    QPushButton:hover {
        color: white;
        border: 2px
    }
""")
certain_reward_button.setStyleSheet("""
QPushButton {
    background-color: rgb(135, 205, 248)
    }
""")
# Set up initial page
dialouge_label = QLabel("Welcome to the OOP Quiz!")
dialouge_label.setAlignment(Qt.AlignCenter)
dialouge_label.setStyleSheet("QLabel { margin-top: 175px, }")
next_button = QPushButton("Next")
back_button = QPushButton("Back")
back_button.setStyleSheet("""
    QPushButton {
        background-color : rgb(135, 205, 248);
        border-radius: 10%;
        height: 50px;
        width: 50%;
        font-size : 15px
    }
    QPushButton:hover {
        color: rgb(135, 205, 248);
        border: 2px
    }
""")
main_window.setStyleSheet("""
    QPushButton {
        background-color : rgb(251, 203, 7);
        border-radius: 10%;
        height: 50px;
        width: 50%;
        font-size : 15px
    }
    QPushButton:hover {
        color: white;
        border: 2px
    }
""")
main_layout.addWidget(dialouge_label)
# bottom
bottom_button_widget = QWidget()
main_layout.addWidget(bottom_button_widget)
bottom_hbox = QHBoxLayout()
bottom_button_widget.setLayout(bottom_hbox)
main_layout.addWidget(next_button)
# Set up question page
points_label = QLabel()
oop_quiz_label = QLabel("OOP Quiz")
code_snip_label = QLabel()
question_label = QLabel()
answer_one_button = QRadioButton()
answer_two_button = QRadioButton()
answer_three_button = QRadioButton()
submit_button = QPushButton("Submit")
top_widget = QWidget()
top_layout = QHBoxLayout()
middle_widget = QWidget()
middle_layout = QHBoxLayout()
left_middle_widget = QWidget()
left_middle_vbox = QVBoxLayout()
right_middle_widget = QWidget()
right_middle_vbox = QVBoxLayout()
bottom_widget = QWidget()
bottom_layout = QHBoxLayout()

# Set up controller
controller = OOPQuestionController(
    main_window, main_layout, dialouge_label, bottom_button_widget,
    next_button, back_button, points_label, oop_quiz_label, code_snip_label,
    question_label, answer_one_button, answer_two_button, answer_three_button,
    submit_button, secondary_window, answer_status_label, question_info_label,
    reward_info_label, certain_reward_button, uncertain_reward_button,
    top_widget, top_layout, middle_widget, middle_layout, left_middle_widget,
    left_middle_vbox, right_middle_widget, right_middle_vbox, bottom_widget,
    bottom_layout,)

main_window.show()
app.exec()
