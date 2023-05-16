import sys
from PySide6.QtWidgets import (QApplication, QSpacerItem, QWidget, QMessageBox, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

from src.models.user_repository import UserRepository
from .home import HomeScreen


import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget

# class LoginScreen(QWidget):
#     def __init__(self, repo:UserRepository):
#         super().__init__()
#         self.repo = repo
#         # Create the main layout
#         layout = QVBoxLayout(self)

#         # Create the login card
#         card = QWidget(self)
#         card.setObjectName("card")
#         card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         card_layout = QVBoxLayout(card)

#         # Create the username field
#         username_layout = QHBoxLayout()
#         username_label = QLabel("Username:")
#         username_label.setFont(QFont("Arial", 12))
#         username_input = QLineEdit()
#         username_input.setFont(QFont("Arial", 12))
#         username_layout.addWidget(username_label)
#         username_layout.addWidget(username_input)
#         card_layout.addLayout(username_layout)

#         # Create the password field
#         password_layout = QHBoxLayout()
#         password_label = QLabel("Password:")
#         password_label.setFont(QFont("Arial", 12))
#         password_input = QLineEdit()
#         password_input.setFont(QFont("Arial", 12))
#         password_input.setEchoMode(QLineEdit.Password)
#         password_layout.addWidget(password_label)
#         password_layout.addWidget(password_input)
#         card_layout.addLayout(password_layout)

#         # Create the login button
#         login_button = QPushButton("Login")
#         login_button.setFont(QFont("Arial", 12))
#         card_layout.addWidget(login_button)

#         # Add the card to the main layout with a margin
#         layout.addStretch()
#         layout.addWidget(card, alignment=Qt.AlignCenter)
#         layout.addStretch()
        
#         # Set the styles for the card and its children
#         self.setStyleSheet("""
#             #card {
#                 background-color: #FFFFFF;
#                 border-radius: 5px;
#                 margin: 20px;
#                 padding: 20px;
#             }
#             QLabel {
#                 color: #000000;
#             }
#             QLineEdit {
#                 border: 2px solid #CCCCCC;
#                 border-radius: 5px;
#                 padding: 5px;
#             }
#             QPushButton {
#                 background-color: #007ACC;
#                 border-radius: 5px;
#                 color: #FFFFFF;
#                 padding: 5px 10px;
#             }
#             QPushButton:hover {
#                 background-color: #005F8C;
#             }
#         """)



class LoginScreen(QWidget):
    def __init__(self, repo:UserRepository):
        super().__init__()
        self.repo = repo

        self.screenSettings()
        self.setStyles()

        # Create the main layout
        layout = QVBoxLayout(self)

        # Create the login card
        card = QWidget(self)
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)

        # Create the username group
        username_widget = QWidget()
        username_layout = QVBoxLayout(username_widget)
        username_label = QLabel("Username:")
        username_label.setFont(QFont("Arial", 12))
        username_input = QLineEdit()
        username_input.setFont(QFont("Arial", 12))
        username_layout.addWidget(username_label)
        username_layout.addWidget(username_input)
        username_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        card_layout.addWidget(username_widget)

        # username_widget = QWidget(card)
        # username_label = QLabel("Username:")
        # username_label.setFont(QFont("Arial", 12))
        # username_input = QLineEdit()
        # username_input.setFont(QFont("Arial", 12))
        # username_layout = QHBoxLayout(username_widget)
        # username_layout.addWidget(username_label)
        # username_layout.addWidget(username_input)
        # card_layout.addWidget(username_widget)

        # Create the username field
        # username_label = QLabel("Username:")
        # username_label.setFont(QFont("Arial", 12))
        # username_input = QLineEdit()
        # username_input.setFont(QFont("Arial", 12))
        # card_layout.addWidget(username_label)
        # card_layout.addWidget(username_input)

        # Create the password field
        # password_label = QLabel("Password:")
        # password_label.setFont(QFont("Arial", 12))
        # password_input = QLineEdit()
        # password_input.setFont(QFont("Arial", 12))
        # password_input.setEchoMode(QLineEdit.Password)
        # card_layout.addWidget(password_label)
        # card_layout.addWidget(password_input)

        # Create the login button
        # login_button = QPushButton("Login")
        # login_button.setFont(QFont("Arial", 12))
        # card_layout.addWidget(login_button)

        # Add the card to the main layout with a margin
        layout.addStretch()
        layout.addWidget(card, alignment=Qt.AlignCenter)
        layout.addStretch()
        
    def setStyles(self):
        # Set the styles for the card and its children
        self.setStyleSheet("""
            #card {
                min-width:300px;
                min-height : 400px;
                background-color: #696969;
                border-radius: 5px;
                margin: 20px;
                padding: 20px;
            }
            QLabel {
                color: #000000;
            }
            QLineEdit {
                border: 2px solid #CCCCCC;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #007ACC;
                border-radius: 5px;
                color: #FFFFFF;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #005F8C;
            }
        """)

    def screenSettings(self):
        # Title
        self.setWindowTitle("HHU Helper")
        # Screen Size
        self.setMinimumSize(468,569)
        self.setMaximumSize(960,540)

