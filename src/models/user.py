import sqlite3
from PySide6.QtCore import QObject, Signal, Property

class User(QObject):
    """
    A class representing a user.

    Attributes:
        idChanged (Signal): A signal emitted when the 'id' property changes.
        usernameChanged (Signal): A signal emitted when the 'username' property changes.
        passwordChanged (Signal): A signal emitted when the 'password' property changes.
    """

    def __init__(self, username="", password="", id=None):
        """
        Initializes a new instance of the User class.

        Args:
            username (str, optional): The username of the user. Defaults to "".
            password (str, optional): The password of the user. Defaults to "".
            id (int, optional): The ID of the user. Defaults to None.
        """
        super().__init__()
        self._id = id
        self._username = username
        self._password = password

    idChanged = Signal()
    usernameChanged = Signal()
    passwordChanged = Signal()

    @Property(int, notify=idChanged)
    def id(self):
        """
        Gets the ID of the user.

        Returns:
            int: The ID of the user.
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        Sets the ID of the user.

        Args:
            value (int): The new ID of the user.
        """
        self._id = value
        self.idChanged.emit()

    @Property(str, notify=usernameChanged)
    def username(self):
        """
        Gets the username of the user.

        Returns:
            str: The username of the user.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the username of the user.

        Args:
            value (str): The new username of the user.
        """
        self._username = value
        self.usernameChanged.emit()

    @Property(str, notify=passwordChanged)
    def password(self):
        """
        Gets the password of the user.

        Returns:
            str: The password of the user.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the password of the user.

        Args:
            value (str): The new password of the user.
        """
        self._password = value
        self.passwordChanged.emit()