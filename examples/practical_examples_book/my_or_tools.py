from ortools.linear_solver import pywraplp

"""
some helper functions from 'practical' git repo
"""


def newSolver(name, integer=False):
    return pywraplp.Solver(
        name,
        pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING
        if integer
        else pywraplp.Solver.GLOP_LINEAR_PROGRAMMING,
    )


def SolVal(x):
    if not isinstance(x, list):
        return (
            0
            if x is None
            else x
            if isinstance(x, (int, float))
            else round(x.SolutionValue(), 2)
            if x.Integer() is False
            else int(x.SolutionValue())
        )
    elif isinstance(x, list):
        return [SolVal(e) for e in x]


def ObjVal(x):
    return round(x.Objective().Value(), 2)
