import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout , QLabel, QLineEdit, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import  QIcon, QPalette, QColor, QPixmap
from PySide6.QtCore import Signal,Slot,Qt

WINDOW_TITLE = "HHU Helper | Login"

class UsernameField(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setPlaceholderText("Username")
        self.setMinimumSize(375,36)
        self.setMaximumSize(375,36)

class PasswordField(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setPlaceholderText("Password")
        self.setEchoMode(QLineEdit.Password)
        self.setMinimumSize(375,36)
        self.setMaximumSize(375,36)

class LoginButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setText("Login")
        self.setMinimumSize(375,40)
        self.setMaximumSize(375,40)

class LoginLayout(QVBoxLayout):
    def __init__ (self)-> None:
        super().__init__()
        self.setAlignment(Qt.AlignCenter)

        # Add the logo and brand title to the layout
        self.createLogo()

        self.logoText()

        # Add Username and Password Widgets directly
        self.username_field = UsernameField()
        self.password_field = PasswordField()
        self.addWidget(self.username_field)
        self.addWidget(self.password_field)
    
    def createLogo(self):
        logo_label = QLabel()
        logo_pixmap = QPixmap("./public/images/logo.png")
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setWindowOpacity(0)
        logo_label.setMinimumSize(400,100)
        logo_label.setMaximumSize(400,100)
        logo_label.setStyleSheet("background-color: transparent;")  # set the background color to transparent
        
        
        self.addWidget(logo_label)

    def logoText(self):
        brand_label = QLabel("የኢትዮጵያ ኤሌክትሪክ አገልገሎት")
        brand_label.setAlignment(Qt.AlignCenter)
        brand_label.setStyleSheet("color:#ff9f00;")

        brand_label_en = QLabel("Ethiopian Electric Utility")
        brand_label_en.setAlignment(Qt.AlignCenter)
        brand_label_en.setStyleSheet("color:green;")

        self.addWidget(brand_label)
        self.addWidget(brand_label_en)

class LoginScreen(QWidget):
    login_signal = Signal(str, str)

    def __init__(self):
        super().__init__()

        self.initGUI()
        
        # Create the layout
        layout = LoginLayout()
        self.setLayout(layout)

        # Add the login button to the layout
        self.login_button = LoginButton()
        layout.addWidget(self.login_button)

        # Connect the login button signal to the login signal
        self.login_button.clicked.connect(self.emit_login_signal)
    
    def initGUI(self):
        self.setWindowTitle(" HHU Helper | Login")
        # self.setWindowTitle("Ethiopian Electric Utility | HHU Helper - Login")

        # Load the QSS or styling file
        with open("./src/views/login_screen.qss", "r") as f:
            self.setStyleSheet(f.read())

        # Set size.
        self.setFixedSize(600, 400)

        # Set app icon
        self.set_app_icon()

        # Set bg image
        self.set_background_img()


    def set_app_icon(self):
        appIcon = QIcon("./public/images/logo.png")
        self.setWindowIcon(appIcon)

    def set_background_img(self):
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("./public/images/grid-4.png"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, self.width(), self.height())

        # Set opacity and other properties on the image
        self.background.setStyleSheet("background-color: green;")

    def get_username(self) -> str:
        return self.layout().username_field.text()

    def get_password(self) -> str:
        return self.layout().password_field.text()

    @Slot()
    def emit_login_signal(self):
        username = self.get_username()
        password = self.get_password()

        # Emit the login signal
        self.login_signal.emit(username, password)
