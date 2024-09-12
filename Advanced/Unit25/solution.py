from ortools.linear_solver import pywraplp

def solve_knapsack():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    if not solver:
        print("Solver not found.")
        return

    # Define data
    sizes = [1,1,1, 3,3,3, 7,7,7]        # Sizes of bread, meat, beer
    popularities = [3,3,3, 10,10,10, 26,26,26] # Popularity values of bread, meat, beer
    max_capacity = 19         # Max space available

    num_items = len(sizes)

    # Define variables
    x = [solver.IntVar(0, 1, f'x{i}') for i in range(num_items)]

    # Define constraints
    solver.Add(sum(x[i] * sizes[i] for i in range(num_items)) <= max_capacity)

    # Define objective
    solver.Maximize(solver.Sum(x[i] * popularities[i] for i in range(num_items)))

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution found:')
        total_size = 0
        total_popularity = 0
        for i in range(num_items):
            if x[i].solution_value() == 1:
                print(f'Item {i + 1} is included in the knapsack.')
                total_size += sizes[i]
                total_popularity += popularities[i]
        print(f'Total size: {total_size}')
        print(f'Total popularity: {total_popularity}')
    else:
        print('No solution found.')

if __name__ == '__main__':
    solve_knapsack()
