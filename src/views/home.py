import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HHU Helper")
        self.setStyleSheet("background-color: #f2f2f2;")
        # COMPONENT WIDGETS
        self.create_UI()

        # LAYOUT
        self.create_layout()

        # SCREEN SIZE
        self.setFixedSize(800, 500)
        self.setMinimumSize(500, 300)

        # Logo
    def create_UI(self):
        self.create_logo()
        self.create_company_name()
        self.create_username_input()
        self.create_password_input()
        self.create_login_button()
        self.create_layout()
    
    def create_logo(self):
        # Company Logo
        logo_label = QLabel(self)
        logo_pixmap = QPixmap("public/images/eep-logo.png")
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setGeometry(50, 20, 300, 100)

    def create_company_name(self):
        # Company Name
        company_label = QLabel(self)
        company_label.setText("Ethiopian Electric Utility")
        company_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        company_label.setAlignment(Qt.AlignCenter)
        company_label.setGeometry(50, 120, 300, 30)

    def create_username_input(self):
        # Username Input
        username_label = QLabel(self)
        username_label.setText("Username:")
        username_label.setGeometry(50, 170, 100, 30)
        username_input = QLineEdit(self)
        username_input.setGeometry(160, 170, 190, 30)

    def create_password_input(self):
        # Password Input
        password_label = QLabel(self)
        password_label.setText("Password:")
        password_label.setGeometry(50, 220, 100, 30)
        password_input = QLineEdit(self)
        password_input.setGeometry(160, 220, 190, 30)
        password_input.setEchoMode(QLineEdit.Password)

    def create_login_button(self):
        # Login Button
        login_button = QPushButton(self)
        login_button.setText("Login")
        login_button.setGeometry(160, 270, 80, 30)
        login_button.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        login_button.clicked.connect(self.login)

    def create_layout(self):
        # CREATE MAIN LAYOUT
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        # CONTAINER LAYOUT 
        self.container_widget = QWidget(self)
        self.container_widget.setStyleSheet('background-color: #f0f0f0')
        self.container_layout = QVBoxLayout(self.container_widget)
        self.container_layout.setContentsMargins(50,50,50,50)
        self.container_layout.setSpacing(20)

        # ADD CONTAINER TO MAIN LAYOUT VBOX
        self.main_layout.addWidget(self.container_widget)

        # CREATING LOGIN CARD
        self.card_widget = QWidget(self.container_widget)
        self.card_widget.setStyleSheet('background-color: #d0d0d0')
        self.card_layout = QVBoxLayout(self.card_widget)
        self.card_layout.setContentsMargins(20,20,20,20)
        self.card_layout.setSpacing(10)
        self.card_layout.setAlignment(Qt.AlignCenter)

        # ADD CARD WIDGET TO CONTAINER LAYOUT
        self.container_layout.addWidget(self.card_widget)

        # TEST 
        self.label = QLabel("Hello, World", self.card_widget)
        self.label.setStyleSheet('font-size: 24px; font-weight:bold;')
        self.card_layout.addWidget(self.label)

    # ACTION BINDINGS
    def onLogin(self):
        # Add your login logic here
        print("Login button clicked")
    
