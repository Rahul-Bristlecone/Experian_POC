from unittest import TestCase
from models.item import ItemModel


class TestItem(TestCase):
    def test_item(self):
        item_obj = ItemModel("Hunter", 2)
        self.assertEqual(item_obj.name, "Hunter", "Name of the item is not available")
        self.assertEqual(item_obj.price, 2)

    def test_json(self):
        item_obj = ItemModel("Hunter", 2)
        expected_res = {"name": "Hunter", "price": 2}
        self.assertDictEqual(expected_res, item_obj.json(),
                             "The Json export of the item is incorrect, received {} while expected is {}"
                             .format(item_obj.json, expected_res))
