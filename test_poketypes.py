import unittest
from poketypes import typesMultFactor


class TestPoketypes(unittest.TestCase):
    def test_typesMultFactor(self):
        """ Tests the function for some Pokémon types. """
        self.assertEqual(typesMultFactor("grass", "grass"), 0.5)
        self.assertEqual(typesMultFactor("grass", "fire"), 0.5)
        self.assertEqual(typesMultFactor("grass", "water"), 2.0)
        self.assertEqual(typesMultFactor("normal", "water"), 1.0)
        self.assertEqual(typesMultFactor("water", "normal"), 1.0)
        self.assertEqual(typesMultFactor("fighting", "normal"), 2.0)
        self.assertEqual(typesMultFactor("fighting", "psychic"), 0.5)

    def test_typesInput(self):
        """ Tests if the input exceptions are handled correctly. """
        self.assertRaises(TypeError, typesMultFactor, 1)
