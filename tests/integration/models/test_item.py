from models.item import ItemModel
from tests.base_test import BaseTest


class TestItem(BaseTest):
    def test_crud_db(self):
        with self.app_context():  # to access the app and the db associated
            item = ItemModel("Harley", "2.5")
            self.assertIsNotNone(ItemModel.find_by_name("Harley"))
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name("Harley"))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name("Harley"))
