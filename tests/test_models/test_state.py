#!/usr/bin/python3import unittest
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_instance_creation(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_name_update(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")


if __name__ == "__main__":
    unittest.main()
