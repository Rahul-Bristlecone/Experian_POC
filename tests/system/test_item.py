import json

import jwt

from models.item import ItemModel
from models.store import StoreModel
from models.user import UserModel
from tests.base_test import BaseTest


class TestItem(BaseTest):
    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                response = client.get("/item/test")

                self.assertEqual(response.status_code, 401)

    def test_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                UserModel("Hulk", "12345").save_to_db()
                StoreModel("test").save_to_db()
                auth = client.get("/auth", data=json.dumps({"username": "Hulk", "password": "12345"}),
                                  headers={"content-Type": "application/json"})

                token = json.loads(auth.data)["access_token"]
                header = {"Authorization": "Jwt" + token}

                response = client.get("/item/test", headers=header)
                self.assertEqual(response.status_code, 404)

    def test_item_found(self):
        with self.app() as client:
            with self.app_context():
                UserModel("Hulk", "12345").save_to_db()
                StoreModel("test").save_to_db()
                auth = client.post("/auth", data=json.dumps({"username": "Hulk", "password": "12345"}),
                                   headers={"content-Type": "application/json"})

                token = json.loads(auth.data)["access_token"]
                header = {"Authorization": "Jwt" + token}

                response = client.get("/item/test", headers=header)
                self.assertEqual(response.status_code, 200)

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test").save_to_db()
                ItemModel("test", "18.12", 1).save_to_db()

                response = client.delete("/item/test")
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({"message": "Item deleted"}, json.loads(response.data))

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test").save_to_db()

                response = client.post("/item/test", data={"price": 20.1,
                                                           "store_id": 1
                                                           })
                self.assertEqual(response.status_code, 201)
                self.assertDictEqual({"name": "test", "price": 20.1}, json.loads(response.data))

    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test").save_to_db()

                response = client.post("/item/test", data={"price": 20.1,
                                                           "store_id": 1
                                                           })
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({"message": "already exist"}, json.loads(response.data))

    def test_put_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test").save_to_db()
                # ItemModel("test", "18.12", 1).save_to_db()
                response = client.put("/item/test", data={"price": 21.1,
                                                          "store_id": 1
                                                          })
                self.assertEqual(response.status_code, 200)

                # this is to test that when we tried to update the item but item did not exist, and
                # it got created when we updated it (below)
                self.assertEqual(ItemModel.find_by_name("test").price, 17.09)
                self.assertDictEqual({"name": "test", "price": 17.90}, json.loads(response.data))

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test").save_to_db()
                ItemModel("test", "18.12", 1).save_to_db()
                response = client.put("/item/test", data={"price": 21.1,
                                                          "store_id": 1
                                                          })

                self.assertEqual(response.status_code, 200)
                self.assertEqual(ItemModel.find_by_name("test").price, 17.09)
                self.assertDictEqual({"name": "test", "price": 21.1}, json.loads(response.data))

    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test").save_to_db()
                ItemModel("test", "18.12", 1).save_to_db()
                response = client.get("/items")

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({"items": [{"name": "test", "price": 21.1}]}, json.loads(response.data))
