from ortools.algorithms.python import knapsack_solver


def main():
    # Create the solver.
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_BRUTE_FORCE_SOLVER,
        "KnapsackExample",
    )

    values = [
        # fmt:off
      3,3,3,10,10,10,26,26,26
        # fmt:on
    ]
    weights = [
        # fmt: off
      [1, 1, 1, 3, 3, 3, 7, 7,7],
        # fmt: on
    ]
    capacities = [19]

    solver.init(values, weights, capacities)
    computed_value = solver.solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    print("Total value =", computed_value)
    for i in range(len(values)):
        if solver.best_solution_contains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print("Total Stellplätze:", total_weight)
    print(":", packed_items)
    print("Stellplätze:", packed_weights)


if __name__ == "__main__":
    main()