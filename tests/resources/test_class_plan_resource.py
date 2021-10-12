import unittest

from flask_testing import TestCase
from testcontainers.postgres import PostgresContainer

from src.app import create_app
from src.infrastructure.db.orm.orms import db

from src.resources.schemas import ClassPlanSchema


class TestClassPlanResource(TestCase):
    _test_container = None

    _POST_REQ = {
        "contents": "string",
        "date": "2021-10-11",
        "evaluation": "string",
        "goals": [
            "string"
        ],
        "group": {
            "code": "string",
            "name": "string"
        },
        "materials": [
            "string"
        ],
        "period": "FIRST",
        "subject": {
            "code": "string",
            "name": "string"
        },
        "teacher": {
            "code": "string",
            "name": "string"
        }
    }

    _PUT_REQ = {
        "contents": "string-update",
        "date": "2021-10-11",
        "evaluation": "string-update",
        "goals": [
            "string"
        ],
        "group": {
            "code": "string",
            "name": "string"
        },
        "materials": [
            "string"
        ],
        "period": "FIRST",
        "subject": {
            "code": "string",
            "name": "string"
        },
        "teacher": {
            "code": "string",
            "name": "string"
        }
    }

    @classmethod
    def setUpClass(cls) -> None:
        print("Start")
        cls._test_container = PostgresContainer()
        cls._test_container.start()
        cls._db_url = cls._test_container.get_connection_url()

    @classmethod
    def tearDownClass(cls) -> None:
        cls._test_container.stop()

    def setUp(self) -> None:
        self.app = self.create_app()
        with self.app.app_context():
            db.create_all()
        self.client = self.app.test_client

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def create_app(self):
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI=self._db_url
        )
        return app

    def test_should_return_code_204_on_update_resource_success(self):
        """
        Test that given a successful update should return a status code 204 with no body in response.
        :return:
        """

        response = self.client().post('/class-plans/', json=self._POST_REQ)

        self.assertIn("Location", response.headers)

        code = response.headers["Location"].split("/")[-1]

        response = self.client().get('/class-plans/' + code)
        self.assertEqual(200, response.status_code)

        response = self.client().put('/class-plans/' + code, json=self._PUT_REQ)
        self.assertEqual(204, response.status_code)

    def test_should_return_code_204_on_delete_resource_success(self):
        """
        Test that given a successful deletion should return a status code 204 with no body in response.
        :return:
        """

        response = self.client().post('/class-plans/', json=self._POST_REQ)

        self.assertIn("Location", response.headers)

        code = response.headers["Location"].split("/")[-1]

        response = self.client().get('/class-plans/' + code)
        self.assertEqual(200, response.status_code)

        response = self.client().delete('/class-plans/' + code)
        self.assertEqual(204, response.status_code)

    def test_should_return_code_200_existing_code(self):
        """
        Test that given an existent code, should return a status code 200 and the json resource in the response body.
        :return:
        """

        response = self.client().post('/class-plans/', json=self._POST_REQ)

        self.assertIn("Location", response.headers)

        code = response.headers["Location"].split("/")[-1]
        response = self.client().get('/class-plans/' + code)

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.data)

    def test_should_return_code_201_on_valid_request(self):
        """
        Test that when sent a valid body should return a status code 201 and the created resource url in the header
        Location.
        :return:
        """

        response = self.client().post('/class-plans/', json=self._POST_REQ)

        self.assertEqual(201, response.status_code)
        self.assertIn("Location", response.headers)

    def test_should_return_code_200_on_successful_search(self):
        """
        Test that given a search with result, should return status code 200 with the result list in the response body.
        :return:
        """

        self.client().post('/class-plans/', json=self._POST_REQ)
        self.client().post('/class-plans/', json=self._POST_REQ)
        self.client().post('/class-plans/', json=self._POST_REQ)

        response = self.client().get('/class-plans/')

        self.assert200(response)

        schema = ClassPlanSchema(many=True)
        class_plans = schema.load(response.json)

        self.assertIsNotNone(class_plans)
        self.assertEqual(3, len(class_plans))


if __name__ == '__main__':
    unittest.main()
