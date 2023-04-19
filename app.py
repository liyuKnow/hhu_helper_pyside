import sys
import os
from PySide6.QtWidgets import QApplication

# MODELS
from src.models.db_helper import Database
from src.models.user_repository import UserRepository

# SCREENS 
from src.views.login import LoginScreen 

def main ():
    # Create the path to the database file in the user's application data directory
    app_name = "HHU_Helper"
    data_dir = os.path.join(os.environ["APPDATA"], app_name)
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    db_file = os.path.join(data_dir, "hhu_helper.db")

    # Create an instance of the Database class using the db_file path
    db = Database(db_file)

    # Create an instance of the UserRepository class using the db object
    repo = UserRepository(db)

    # Run your application code here
    app = QApplication(sys.argv)

    login_screen = LoginScreen(repo)
    login_screen.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()