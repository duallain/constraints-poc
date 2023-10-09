import unittest
from examples.youtube_LP_series.linear_scheduling import solve_schedule_pyomo


class TestSolveSchedulePyomo(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        price_schedule = {
            0: 0.5,
            1: 0.6,
            2: 1.5,
            3: 1.0,
            4: 0.9,
            5: 1.1,
            6: 1.8,
            7: 1.5,
            8: 0.9,
            9: 0.8,
            10: 0.7,
            11: 1.0,
        }

        charge_schedule = {
            0: 0.0,
            1: 0.0,
            2: 0.0,
            3: 0.0,
            4: 0.3,
            5: 0.15,
            6: 0.15,
            7: 0.05,
            8: 0.05,
            9: 0.05,
            10: 0.0,
            11: 0.0,
        }

        self.rc, self.power_sold, self.energy_stored = solve_schedule_pyomo(
            price_schedule, charge_schedule
        )

    # Tests to write:
    # test that a solution was returned

    # test how much sold for each time period?
    # test total sold?

    def test_returned_code(self):
        self.assertEqual(self.rc, True)

    def test_power_sold(self):
        self.assertEqual(
            self.power_sold,
            {
                0: -0.0,
                1: 0.0,
                2: 150.0,
                3: 125.0,
                4: 0.0,
                5: 150.0,
                6: 150.0,
                7: 150.0,
                8: 0.0,
                9: 0.0,
                10: 0.0,
                11: 150.0,
            },
        )

    def test_energy_stored(self):
        self.assertEqual(
            self.energy_stored,
            {
                0: 500.0,
                1: 500.0,
                2: 350.0,
                3: 225.0,
                4: 375.0,
                5: 300.0,
                6: 225.0,
                7: 100.0,
                8: 125.0,
                9: 150.0,
                10: 150.0,
                11: 0.0,
            },
        )
