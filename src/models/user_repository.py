import hashlib
from typing import Dict
from .db_helper import Database
from .generic_repository import GenericRepository

class UserRepository(GenericRepository):
    def __init__(self, db: Database):
        super().__init__(db)

    def register_user(self, username: str, password: str) -> Dict[str, str]:
        columns = {"username": "TEXT", "password": "TEXT"}
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        item = {"username": username, "password": hashed_password}
        return self.add_item("User", columns, item)

    def login_user(self, username: str, password: str) -> bool:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        query = f"SELECT * FROM User WHERE username = ? AND password = ?"
        params = (username, hashed_password)
        result = self.db.execute_query(query, params)
        return len(result) > 0