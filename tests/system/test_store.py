import json

from models.store import StoreModel
from models.item import ItemModel
# from resources.store import Store
from tests.base_test import BaseTest


class TestStore(BaseTest):
    def test_store_found(self):
        with self.app() as client:
            with self.app_context:
                StoreModel("plum").save_to_db()
                response = client.get("/store/plum")
                self.assertEqual(response.status_code, 201)
                self.assertDictEqual({"message": "Successful"}, json.loads(response.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context:
                response = client.get("/store/plum")
                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({"message": "unSuccessful"}, json.loads(response.data))

    def test_create_store(self):
        with self.app() as client:
            with self.app_context:
                response = client.post("/store/plum")
                self.assertEqual(response.status_code, 200)
                self.assertIsNotNone(StoreModel.find_by_name("plum"))
                self.assertDictEqual({"name": "plum", "items": []}, json.loads(response.data))

    def test_create_duplicate(self):
        with self.app() as client:
            with self.app_context:
                response = client.post("/store/plum", {"name": "plum", "items": []})
                self.assertEqual(response.status_code, 404)
                self.assertIsNone(StoreModel.find_by_name("plum"))
                self.assertDictEqual({"message": "Successful"}, json.loads(response.data))

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context:
                StoreModel("plum").save_to_db()
                response = client.delete("/store/plum")
                self.assertEqual(response.status_code, 200)
                self.assertIsNone(StoreModel.find_by_name("plum"))
                self.assertDictEqual({"message": "Store deleted"}, json.loads(response.data))

    def test_store_items(self):
        with self.app() as client:
            with self.app_context:
                StoreModel("plum").save_to_db()
                ItemModel("cream", 19.99, 1).save_to_db()
                response = client.get("/store/plum")

                self.assertEqual(response.status_code, 201)
                self.assertDictEqual({"name": "plum",
                                      "items": [{"name": "cream", "price": 19.99}]},
                                     json.loads(response.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context:
                StoreModel("plum").save_to_db()
                response = client.get("/stores")

                self.assertEqual(response.status_code, 201)
                self.assertDictEqual({"stores": [{"name": "plum", "items": []}]},
                                     json.loads(response.data))

    def test_store_list_items(self):
        with self.app() as client:
            with self.app_context:
                StoreModel("plum").save_to_db()
                ItemModel("cream", 19.99, 1).save_to_db()
                response = client.get("/stores")

                self.assertEqual(response.status_code, 201)
                self.assertDictEqual({"stores": [{"name": "plum", "items": [{"name": "cream", "price": 19.99}]}]},
                                     json.loads(response.data))
