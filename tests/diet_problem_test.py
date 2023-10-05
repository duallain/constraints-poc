import unittest
from examples.diet_problem import solve_diet, solve_diet_2


class TestSolveDiet(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # this data was generated from the code the book's github repo has
        # it seems like it makes some sense to just hardcode one exmple for testing
        self.nutrition_info = [
            [35, 508, 69, 47, 0, 27, 5.65],
            [320, 637, 369, 49, 2, 26, 2.03],
            [858, 303, 375, 77, 1, 21, 3.59],
            [523, 671, 872, 60, 21, 32, 2.17],
            [956, 995, 75, 12, 4, 20, 2.08],
            [21537, 9573, 35294, 4448, "", "", "", ""],
            [102479, 94878, 73651, 8974, "", "", "", ""],
        ]

        self.result_value, self.cost_value, self.nutrition_values = solve_diet(
            self.nutrition_info
        )

    def test_result_value(self):
        """test to ensure model solved successfully"""
        self.assertEqual(self.result_value, 0)

    def test_cost(self):
        """pass"""
        self.assertEqual(self.cost_value, 186.77)

    def test_nutrient_values(self):
        """pass"""
        # values returned are the - min,max,?,max,min - of the foods
        # which makes sense for this type of optimization problem
        # we're really near the vertices of the graph
        # except for [2] which seems to be the 'filler', which is probably why it's a fraction as well
        self.assertEqual(self.nutrition_values, [0.0, 26.0, 15.66, 32.0, 4.0])


class TestSolveDiet2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # this data was generated from the code the book's github repo has
        # it seems like it makes some sense to just hardcode one exmple for testing
        self.food_info = [
            {"cost": 5.65, "min": 0, "max": 27, "nutrients": [35, 508, 69, 47]},
            {"cost": 2.03, "min": 2, "max": 26, "nutrients": [320, 637, 369, 49]},
            {"cost": 3.59, "min": 1, "max": 21, "nutrients": [858, 303, 375, 77]},
            {"cost": 2.17, "min": 21, "max": 32, "nutrients": [523, 671, 872, 60]},
            {"cost": 2.08, "min": 4, "max": 20, "nutrients": [956, 995, 75, 12]},
        ]

        self.nutrient_info = [
            {"min": 21537, "max": 102479},
            {"min": 9573, "max": 94878},
            {"min": 35294, "max": 73651},
            {"min": 4448, "max": 8974},
        ]

        self.result_value, self.cost_value, self.nutrition_values = solve_diet_2(
            self.food_info, self.nutrient_info
        )

    def test_result_value(self):
        """test to ensure model solved successfully"""
        self.assertEqual(self.result_value, 0)

    def test_cost(self):
        """pass"""
        self.assertEqual(self.cost_value, 186.77)

    def test_nutrient_values(self):
        """pass"""
        # values returned are the - min,max,?,max,min - of the foods
        # which makes sense for this type of optimization problem
        # we're really near the vertices of the graph
        # except for [2] which seems to be the 'filler', which is probably why it's a fraction as well
        self.assertEqual(self.nutrition_values, [0.0, 26.0, 15.66, 32.0, 4.0])
