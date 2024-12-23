import unittest
from app import create_app, db

class AppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Patient Information', response.data)

    def test_patient_page(self):
        response = self.client.get('/patient/1')
        self.assertEqual(response.status_code, 404)  # Assuming no patient with ID 1 exists

    def test_create_patient(self):
        response = self.client.post('/create', data={
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male'
        })
        self.assertEqual(response.status_code, 302)  # Assuming a redirect after successful creation

    def test_invalid_patient_creation(self):
        response = self.client.post('/create', data={
            'name': '',
            'age': 'invalid_age',
            'gender': 'Male'
        })
        self.assertEqual(response.status_code, 400)  # Assuming a bad request for invalid data

if __name__ == '__main__':
    unittest.main()