from typing import Dict
from .db_helper import Database

class BaseModel:
    TABLE_NAME = ""
    COLUMNS = {}

    @classmethod
    def create_table(cls, db: Database) -> None:
        column_definitions = ", ".join([f"{name} {data_type}" for name, data_type in cls.COLUMNS.items()])
        query = f"CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} ({column_definitions})"
        db.execute(query)
        db.commit()