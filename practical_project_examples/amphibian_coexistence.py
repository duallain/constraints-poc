from ortools.linear_solver import pywraplp

"""this is an example module for sphinx 123abc """


def solve_coexistence():
    """solves for coexistence of some animals given some use of shared resources
    attempts to maximize total population

    :return: total population value, and a list of values for each species pop
    :rtype: float, list(float)
    """
    title = "Amphibian coexistence"
    solver = pywraplp.Solver(title, pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    x = [solver.NumVar(0, 1000, "x[%i]" % i) for i in range(3)]

    pop = solver.NumVar(0, 3000, "pop")

    solver.Add(2 * x[0] + x[1] + x[2] <= 1500)
    solver.Add(x[0] + 3 * x[1] + 2 * x[2] <= 3000)
    solver.Add(x[0] + 2 * x[1] + 3 * x[2] <= 4000)

    solver.Add(pop == x[0] + x[1] + x[2])

    solver.Maximize(pop)

    # book doesn't have this line
    solver.Solve()

    return pop.SolutionValue(), [e.SolutionValue() for e in x]


if __name__ == "__main__":
    pop, x = solve_coexistence()

    Table = [["Specie", "Count"]]

    for i in range(3):
        Table.append([["Toads", "Salamanders", "Caecilians"][i], x[i]])

    Table.append(["Total", pop])
    for key, value in Table:
        print(key, value)
