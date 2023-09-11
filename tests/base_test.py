# create a base test file which can be used by other test cases
# This is going to be parent class to each non-unit test
# It allows for the instantiation of the database dynamically which gets repeated multiple times in each test case
# It makes sure that database is blank and new each time after instantiation

from unittest import TestCase
from experian_poc import experian_poc
from app import app
from db import db  # for SQLAlchemy database instance


class BaseTest(TestCase):
    # Set up the test client
    # make db blank after each test
    def SetUp(self):
        # Runs before every test
        db.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()

        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # Runs after every test
        with app.app_context():
            db.session.remove()
            db.drop_all()
