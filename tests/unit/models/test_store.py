from tests.base_test import BaseTest
from models.store import StoreModel
from models.item import ItemModel


class TestStore(BaseTest):

    def test_create_store(self):
        store = StoreModel("plum")
        self.assertEqual(store.name, "plum")

    def test_json(self):
        store = StoreModel("plum")
        expected_res = {"name": "plum", "items": []}
        self.assertEqual(store.json(), expected_res)
