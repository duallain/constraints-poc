from ortools.linear_solver import pywraplp
from examples.my_or_tools import SolVal, ObjVal, newSolver


"""
    minimizes cost while still meeting nutrition
"""


def solve_diet(InputTable):
    s = newSolver("Diet")

    # nb == number of
    # nbF == number of foods
    # nbN == number of nutrients
    nbF, nbN = len(InputTable) - 2, len(InputTable[0]) - 3

    # for a food row, there is a column per nutrient
    # then min/max/cost in that order.
    # we're just using offsets here
    # for nmin/max we're doing the same thing, skipping rows.
    # In this case min/max are whole rows, after all the food data

    # this seems like a gnarly way to do this, would it be better to build a different/better structure?
    FMin, FMax, FCost, NMin, NMax = nbN, nbN + 1, nbN + 2, nbF, nbF + 1

    # build an array of variables
    # one for each Food
    # range of possible values set by the min/max columns in the data structure
    f = [s.NumVar(InputTable[i][FMin], InputTable[i][FMax], "") for i in range(nbF)]

    # for each nutrient
    for j in range(nbN):
        # sum of (each food * the amount of a nutrient per food)
        # should be more than the min allowed for a nutrient
        s.Add(
            InputTable[NMin][j]
            <= s.Sum([f[food_i] * InputTable[food_i][j] for food_i in range(nbF)])
        )

        # and less than the max allowed for a nutrient
        s.Add(
            s.Sum([f[food_i] * InputTable[food_i][j] for food_i in range(nbF)])
            <= InputTable[NMax][j]
        )

    # minimize the sum of each food * cost/food
    s.Minimize(s.Sum([f[food_i] * InputTable[food_i][FCost] for food_i in range(nbF)]))

    rc = s.Solve()

    return rc, ObjVal(s), SolVal(f)


def solve_diet_2(FoodInput, NutrientInput):
    s = newSolver("Diet")

    food_vars = [s.NumVar(food["min"], food["max"], "") for food in FoodInput]

    for n_idx, nutrient in enumerate(NutrientInput):
        # sum of (each food * the amount of a nutrient per food)

        s.Add(
            nutrient["min"]
            <= s.Sum(
                [
                    food_vars[f_idx] * food["nutrients"][n_idx]
                    for f_idx, food in enumerate(FoodInput)
                ]
            )
        )

        s.Add(
            nutrient["max"]
            >= s.Sum(
                [
                    food_vars[f_idx] * food["nutrients"][n_idx]
                    for f_idx, food in enumerate(FoodInput)
                ]
            )
        )

    s.Minimize(
        s.Sum([food_vars[f_idx] * food["cost"] for f_idx, food in enumerate(FoodInput)])
    )

    rc = s.Solve()
    return rc, ObjVal(s), SolVal(food_vars)
