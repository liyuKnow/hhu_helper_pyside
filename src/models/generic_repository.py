from typing import List, Dict
from PySide6.QtCore import QObject, Signal, Property
from .db_helper import Database


class GenericRepository(QObject):
    """
    A generic repository class for interacting with SQLite databases.

    Attributes:
        db (Database): The database object to use for interacting with the database.
    """

    def __init__(self, db: Database):
        """
        Initializes a new instance of the GenericRepository class.

        Args:
            db (Database): The database object to use for interacting with the database.
        """
        super().__init__()
        self._db = db

    def add_item(self, table_name: str, columns: Dict[str, str], item: Dict[str, str]) -> Dict[str, str]:
        """
        Adds a new item to the specified table in the database.

        Args:
            table_name (str): The name of the table to add the item to.
            columns (Dict[str, str]): A dictionary of column names and their data types.
            item (Dict[str, str]): A dictionary of item data.

        Returns:
            Dict[str, str]: The item with its 'id' property set to the ID assigned by the database.
        """
        column_names = ", ".join(columns.keys())
        placeholders = ", ".join(["?"] * len(columns))
        values = tuple(item.get(column_name, "") for column_name in columns.keys())
        query = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
        self._db.execute(query, values)
        self._db.commit()
        item_id = self._db.execute("SELECT last_insert_rowid() as id")[0]["id"]
        item["id"] = item_id
        return item

    def remove_item(self, table_name: str, item_id: int) -> None:
        """
        Removes an item from the specified table in the database.

        Args:
            table_name (str): The name of the table to remove the item from.
            item_id (int): The ID of the item to remove.
        """
        query = f"DELETE FROM {table_name} WHERE id=?"
        self._db.execute(query, (item_id,))
        self._db.commit()

    def update_item(self, table_name: str, columns: Dict[str, str], item: Dict[str, str]) -> None:
        """
        Updates an item in the specified table in the database.

        Args:
            table_name (str): The name of the table to update the item in.
            columns (Dict[str, str]): A dictionary of column names and their data types.
            item (Dict[str, str]): A dictionary of item data.
        """
        set_clause = ", ".join([f"{column_name}=?" for column_name in columns.keys()])
        values = tuple(item.get(column_name, "") for column_name in columns.keys())
        query = f"UPDATE {table_name} SET {set_clause} WHERE id=?"
        self._db.execute(query, values + (item["id"],))
        self._db.commit()

    def get_items(self, table_name: str, columns: Dict[str, str], page: int = 1, page_size: int = 10) -> List[Dict[str, str]]:
        """
        Retrieves items from the specified table in the database.

        Args:
            table_name (str): The name of the table to retrieve items from.
            columns (Dict[str, str]): A dictionary of column names and their data types.
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of items to retrieve per page. Defaults to 10.

        Returns:
            List[Dict[str, str]]: A list of dictionaries, where each dictionary represents an item.
        """
        offset = (page - 1) * page_size
        column_names = ", ".join(columns.keys())
        query = f"SELECT {column_names} FROM {table_name} LIMIT ? OFFSET ?"
        return self._db.execute(query, (page_size, offset))