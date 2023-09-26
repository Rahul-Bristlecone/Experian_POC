from models.item import ItemModel
# from models.store import StoreModel
from tests.base_test import BaseTest


class TestItem(BaseTest):
    def test_item(self):
        item_obj = ItemModel("Hunter", 2, 1)
        self.assertEqual(item_obj.name, "Hunter", "Name of the item is not available")
        self.assertEqual(item_obj.price, 2)
        self.assertEqual(item_obj.store_id, 1)
        self.assertIsNone(item_obj.store)

    def test_item_json(self):
        item_obj = ItemModel("Hunter", 2, 1)
        expected_res = {"name": "Hunter", "price": 2}
        self.assertDictEqual(expected_res, item_obj.json(),
                             "The Json export of the item is incorrect, received {} while expected is {}"
                             .format(item_obj.json, expected_res))
