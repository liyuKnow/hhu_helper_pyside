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

    def get_user_by_username(self, username: str) -> Dict[str, str]:
        columns = {"id": "INTEGER", "username": "TEXT", "password": "TEXT"}
        items = self.get_items("User", columns, page=1, page_size=1, where_clause="WHERE username=?", where_params=(username,))
        return items[0] if items else None