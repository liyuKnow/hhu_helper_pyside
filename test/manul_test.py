import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import register_user, get_users, find_user, update_password, delete_user, login, logout, get_db_path_and_name

def test_repository ():
    print("Started testing")
    # Test the functionalities

    # Get database name.
    print(get_db_path_and_name())

    # Get table information.

    # Register user.
    register_user("test2", "12345")

    # Find user by username.
    user = find_user("test1")
    if user :
        print(f"Username => {user.username}")
    else :
        print("User not found")

    # Login test
    login_result = login("test1", "12345")
    print("Login successful:", login_result)

    # Update password.
    user = find_user("test1")
    if user :
        update_password(user, "pass1")
    else:
        print("User to update is not found")

    login_result = login("test1", "12345")
    print("Login successful:", login_result)

    # Get all users.
    users = get_users()
    if users:
        for user in users :
            print(f"Username : {user.username} && Password : {user.password}")
    else:
        print("Users not found")
    
    # Delete user.
    user = find_user("test1")
    if user :
        delete_user(user)
    else:
        print("User to delete was not found")   

    
    logout()

if __name__ == "__main__":
    test_repository()