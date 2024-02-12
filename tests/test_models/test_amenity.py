import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_instance_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_update_name(self):
        amenity = Amenity()
        amenity.name = "Test Amenity"
        self.assertEqual(amenity.name, "Test Amenity")


if __name__ == "__main__":
    unittest.main()
