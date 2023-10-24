import pyomo.environ as pyomo

"""
    'pyomo' example version of how to get max population
"""


def solve_coexistence_pyomo():
    """
    Solves for coexistence of some animals.

    Each species uses different amounts of some shared resources.
    This function maximizes total population without over utilizing those
    resources.

    This is the same as the other coexistence, except uses pyomo.

    :return: total population value, and a list of values for each species pop

    :rtype: float, list(float)
    """

    model = pyomo.ConcreteModel()
    solver = pyomo.SolverFactory("cbc")

    model.s1 = pyomo.Var(domain=pyomo.NonNegativeReals, bounds=(0, 1000))
    model.s2 = pyomo.Var(domain=pyomo.NonNegativeReals, bounds=(0, 1000))
    model.s3 = pyomo.Var(domain=pyomo.NonNegativeReals, bounds=(0, 1000))

    model.pop = pyomo.Var(domain=pyomo.NonNegativeReals, bounds=(0, 3000))

    model.c = pyomo.ConstraintList()
    # these constraints are almost identically defined vs or-tools
    model.c.add(2 * model.s1 + model.s2 + model.s3 <= 1500)
    model.c.add(model.s1 + 3 * model.s2 + 2 * model.s3 <= 3000)
    model.c.add(model.s1 + 2 * model.s2 + 3 * model.s3 <= 4000)
    model.c.add(model.pop == model.s1 + model.s2 + model.s3)

    model.objective = pyomo.Objective(
        rule=lambda model: model.pop, sense=pyomo.maximize
    )

    solver.solve(model)
    # print(result)

    total_pop = round(pyomo.value(model.pop), 1)
    species_pops = [
        round(pyomo.value(model.s1), 1),
        round(pyomo.value(model.s2), 1),
        round(pyomo.value(model.s3), 1),
    ]

    return total_pop, species_pops
