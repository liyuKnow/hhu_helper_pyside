import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

from src.views import LoginScreen, HomeScreen

from src import login, get_db_path_and_name


class HHUHelper(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        # define our app screens
        self.login_screen = LoginScreen()
        self.home_screen = HomeScreen()
        
        self.login_screen.login_signal.connect(self.login_button_clicked)
        self.login_screen.show()    
    
    def login_button_clicked(self, username: str, password: str):
        # Check if the username password are valid
        if login(username, password):
            print("Login success")
            self.login_screen.close()
            self.home_screen.show()
        else:
            # Display an error
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Invalid username or password")
            msg_box.exec_()

def main():
    try:
        app = HHUHelper(sys.argv)
        print(get_db_path_and_name())
        sys.exit(app.exec())
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing window ...")
    except Exception:
        print("Exception:", sys.exc_info()[1])

if __name__ == "__main__":
    main()


# import sys
# import os
# from PySide6.QtWidgets import QApplication
# from tabulate import tabulate

# # MODELS
# from src.models.db_helper import Database
# from src.models.user import User
# from src.models.user_repository import UserRepository

# # SCREENS 
# from src.views.login import LoginScreen 

# def main ():
#     # Create the path to the database file in the user's application data directory
#     app_name = "HHU_Helper"
#     data_dir = os.path.join(os.environ["APPDATA"], app_name)
    
#     if not os.path.exists(data_dir):
#         os.makedirs(data_dir)

#     db_file = os.path.join(data_dir, "hhu_helper.db")

#     # Create an instance of the Database class using the db_file path
#     db = Database(db_file)

#     # Create an instance of the UserRepository class using the db object
#     repo = UserRepository(db)

#     # ----------- TEST ----------- #
#     # test_db_and_user_table(repo)
#     # ----------------------------- #


#     # Run your application code here
#     app = QApplication(sys.argv)

#     login_screen = LoginScreen(repo)
#     login_screen.show()

#     sys.exit(app.exec())

# def test_db_and_user_table (repo:UserRepository):
#     """
#     Inserts and retrieves a user to test if the local app data db and the user table are operable.
#     """

#     # new_user  = ["kidus@hhu", "123456"]

#     # insert user
#     default_user  = repo.create_user("kidus@hhu", "123456")

#     # Retrieve user
#     retrieved_user = repo.get_user_by_id(default_user.id)

#     table = [
#         ["Id", "Username", "Password"],
#         [retrieved_user.id, retrieved_user.username, retrieved_user.password]
#     ]

#     print(tabulate(table,headers='firstrow'))

# if __name__ == "__main__":
#     main()