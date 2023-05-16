from typing import Dict
from .db_helper import Database
from .base_model import BaseModel

class UserTable(BaseModel):
    TABLE_NAME = "User"
    COLUMNS = {"id": "INTEGER PRIMARY KEY", "username": "TEXT", "password": "TEXT"}

    @classmethod
    def create_table(cls, db: Database) -> None:
        column_definitions = ", ".join([f"{name} {data_type}" for name, data_type in cls.COLUMNS.items()])
        query = f"CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} ({column_definitions})"
        db.execute(query)
        db.commit()