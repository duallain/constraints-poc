import unittest
from examples.amphibian_coexistence import solve_coexistence


class TestSolveCoexistence(unittest.TestCase):
    def setUp(self) -> None:
        self.coexistence_total, self.coexistence_species = solve_coexistence()
        return super().setUp()

    def test_total_pop(self):
        self.assertEqual(self.coexistence_total, 1400.0)

    # names are from table formatting of results
    # hard to trace it back to the actual code
    # but easy to connect to example from book
    # would probably prefer to make a table to give to this function
    # to keep name and the constraints connected?
    def test_toads_pop(self):
        self.assertEqual(self.coexistence_species[0], 100.0)

    def test_salamanders_pop(self):
        self.assertEqual(self.coexistence_species[1], 300.0)

    def test_caecilians_pop(self):
        self.assertEqual(self.coexistence_species[2], 1000.0)
