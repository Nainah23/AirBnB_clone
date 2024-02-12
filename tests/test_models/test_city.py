import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_instance_creation(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_update_name(self):
        city = City()
        city.name = "New York"
        self.assertEqual(city.name, "New York")

    def test_update_state_id(self):
        city = City()
        city.state_id = "NY"
        self.assertEqual(city.state_id, "NY")


if __name__ == "__main__":
    unittest.main()
