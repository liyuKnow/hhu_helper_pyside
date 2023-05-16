import hashlib
from typing import List
from .user import User
from .database import session, engine

# Register a user
def register_user(username: str, password: str) -> None:
    # Hash the password using sha3_256
    hashed_password: str = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
    # Create a new user object with the hashed password
    user: User = User(username=username, password=hashed_password)
    # Add the user to the session and commit the changes to the database
    session.add(user)
    session.commit()

# Login
def login(username: str, password: str) -> bool:
    # Hash the password using sha3_256
    hashed_password: str = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
    # Find the user with the specified username
    user: User = find_user(username)
    # Check if the user exists and if the hashed password matches the stored password
    if user and user.password == hashed_password:
        return True
    return False

# Logout
def logout() -> None:
    print("Logout !")

# ---------------------------------------------------------------------------- #
# ------------------------------------ DEV ----------------------------------- #
# ---------------------------------------------------------------------------- #

# Get the path and name of the database file
def get_db_path_and_name() -> str:
    return engine.url.database

# Get a list of all users in the database
def get_users() -> List[User]:
    users: List[User] = session.query(User).all()
    return users

# Find a user by their username
def find_user(username: str) -> User:
    user: User = session.query(User).filter_by(username=username).first()
    return user

# Update a user's password
def update_password(user: User, new_password: str) -> None:
    # Hash the new password using sha3_256
    hashed_password: str = hashlib.sha3_256(new_password.encode('utf-8')).hexdigest()
    # Update the user's password in the session and commit the changes to the database
    user.password = hashed_password
    session.commit()

# Delete a user from the database
def delete_user(user: User) -> None:
    # Delete the user from the session and commit the changes to the database
    session.delete(user)
    session.commit()