import unittest
from models.place import Place


class TestPlaceAttributes(unittest.TestCase):
    def test_city_id_default(self):
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_user_id_default(self):
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_name_default(self):
        place = Place()
        self.assertEqual(place.name, "")

    def test_description_default(self):
        place = Place()
        self.assertEqual(place.description, "")

    def test_number_rooms_default(self):
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_default(self):
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_default(self):
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_default(self):
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_default(self):
        place = Place()
        self.assertEqual(place.latitude, 0.0)

    def test_longitude_default(self):
        place = Place()
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids_default(self):
        place = Place()
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
