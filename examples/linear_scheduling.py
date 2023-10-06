import pyomo.environ as pyomo
from pyomo.opt import SolverStatus

"""
    'pyomo' example for optimal scheduling of power
"""


def solve_schedule_pyomo(price_schedule: dict, charge_schedule: dict) -> None:
    """doing some power scheduling

    :return: _description_
    :rtype: _type_
    """
    # add a little check to ensure the schedules are shaped the same
    if price_schedule.keys() != charge_schedule.keys():
        return False

    model = pyomo.ConcreteModel()
    solver = pyomo.SolverFactory("cbc")

    # setting up the time steps
    model.nt = pyomo.Param(initialize=len(price_schedule), domain=pyomo.Integers)
    model.T = pyomo.Set(initialize=range(model.nt()))

    model.price = pyomo.Param(model.T, initialize=price_schedule)
    model.charge = pyomo.Param(model.T, initialize=charge_schedule)

    model.S0 = pyomo.Param(initialize=500.0)
    model.SMax = pyomo.Param(initialize=500.0)

    model.wmax = pyomo.Param(initialize=150.0)

    # vars
    model.w = pyomo.Var(model.T, domain=pyomo.NonNegativeReals)
    model.s = pyomo.Var(model.T, domain=pyomo.NonNegativeReals)

    def maximize_price(model):
        return sum([model.w[t] * model.price[t] for t in model.T])

    model.objective = pyomo.Objective(rule=maximize_price, sense=pyomo.maximize)

    # prevents storage for any time period from being over the max allowed
    def constr_store_capacity(model, t):
        return model.s[t] <= model.SMax

    model.constr_store_capacity = pyomo.Constraint(model.T, rule=constr_store_capacity)

    def constr_power(model, t):
        return model.w[t] <= model.wmax

    model.constr_power = pyomo.Constraint(model.T, rule=constr_power)

    def constraint_store_balance(model, t):
        # charge is a percentage from the schedule, so to turn to a single value we multiple
        if t == 0:
            return model.s[t] == model.S0 - model.w[t] + model.charge[t] * model.SMax
        else:
            return (
                model.s[t] == model.s[t - 1] - model.w[t] + model.charge[t] * model.SMax
            )

    model.constr_store_balance = pyomo.Constraint(
        model.T, rule=constraint_store_balance
    )

    results = solver.solve(model)

    solver_returned_successfully = results.solver.status == SolverStatus.ok

    # print(model.w.extract_values())
    # print(model.s.extract_values())

    return (
        solver_returned_successfully,
        model.w.extract_values(),
        model.s.extract_values(),
    )
