from models.user import UserModel
from tests.base_test import BaseTest


class TestUser(BaseTest):
    def test_user_crud(self):
        with self.app_context():
            user = UserModel("Hulk", "87484")

            self.assertIsNone(UserModel.find_by_username("Hulk"))
            self.assertIsNone(UserModel.find_by_userid(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username("Hulk"))
            self.assertIsNotNone(UserModel.find_by_userid(1))
