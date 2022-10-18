from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton)
from oop_test_model import oop_questions
from oop_test_controller import OOPQuestionController

# Set up app and main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle("OOP Quiz")
main_window.resize(500, 500)

# Set up main widget
main_widget = QWidget()
main_window.setCentralWidget(main_widget)
main_layout = QVBoxLayout()
main_widget.setLayout(main_layout)

# Set up initial page
dialouge_label = QLabel("Welcome to the OOP Quiz!\n Start by entering your name")
next_button = QPushButton("Next")
main_layout.addWidget(dialouge_label)
main_layout.addWidget(next_button)

# Set up question page
code_snip_label = QLabel()
question_label = QLabel()
answer_one_button = QPushButton()
answer_two_button = QPushButton()
answer_three_button = QPushButton()
submit_button = QPushButton("Submit")


# Set up controller
controller = OOPQuestionController(main_layout, dialouge_label, next_button, code_snip_label, question_label, answer_one_button, answer_two_button, answer_three_button, submit_button)

main_window.show()
app.exec()
