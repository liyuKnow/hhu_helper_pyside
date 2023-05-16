import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import register_user, find_user, update_password, delete_user, login, logout

class TestRepository(unittest.TestCase):
    # PASSED
    # def test_register_user(self):
    #     register_user("test1", "test")
    #     user = find_user("test1")
    #     self.assertIsNotNone(user)
    #     self.assertEqual(user.username, "test1")
    #     self.assertEqual(user.password, "test")

    # PASSED
    def test_login(self):
        self.assertTrue(login("test2", "12345"))
        self.assertFalse(login("test1", "wrong"))

    # PASSED
    # def test_update_password(self):
    #     user = find_user("test1")
    #     print(user.password)
    #     update_password(user, "test")
    #     self.assertEqual(user.password, "test")

    # def test_delete_user(self):
    #     user = find_user("test_user")
    #     delete_user(user)
    #     self.assertIsNone(find_user("test_user"))

if __name__ == "__main__":
    unittest.main() 