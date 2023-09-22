from ortools.linear_solver import pywraplp

"""this is an example module for sphinx 123abc """


def solve_coexistence():
    """
    Solves for coexistence of some animals.

    Each species uses different amounts of some shared resources.
    This function maximizes total population without over utilizing those
    resources.

    :return: total population value, and a list of values for each species pop

    :rtype: float, list(float)
    """
    title = "Amphibian coexistence"
    solver = pywraplp.Solver(title, pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # 'answer' variables, represents a single group of amphibians
    species = [solver.NumVar(0, 1000, "species[%i]" % i) for i in range(3)]

    # total population, one of the constraints defines it
    pop = solver.NumVar(0, 3000, "pop")

    # constraints
    solver.Add(2 * species[0] + species[1] + species[2] <= 1500)
    solver.Add(species[0] + 3 * species[1] + 2 * species[2] <= 3000)
    solver.Add(species[0] + 2 * species[1] + 3 * species[2] <= 4000)

    solver.Add(pop == species[0] + species[1] + species[2])

    solver.Maximize(pop)

    # book doesn't have this line
    solver.Solve()

    total_pop = round(pop.SolutionValue(), 1)
    species_pops = [round(e.SolutionValue(), 1) for e in species]

    return total_pop, species_pops


if __name__ == "__main__":
    pop, x = solve_coexistence()

    Table = [["Specie", "Count"]]

    for i in range(3):
        Table.append([["Toads", "Salamanders", "Caecilians"][i], x[i]])

    Table.append(["Total", pop])
    for key, value in Table:
        print(key, value)
