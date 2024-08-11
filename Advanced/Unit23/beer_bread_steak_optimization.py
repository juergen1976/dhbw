from ortools.sat.python import cp_model

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

# 1. Variables
capacity = 19
bread = model.NewIntVar(0, capacity, 'bread')
meat  = model.NewIntVar(0, capacity, 'meat')
beer  = model.NewIntVar(0, capacity, 'beer')

# 2. Constraints
model.Add(1 * bread
        + 3 * meat
        + 7 * beer <= capacity)

# 3. Objective
model.Maximize(3  * bread
             + 10 * meat
             + 26 * beer)

# Solve problem
status = solver.Solve(model)

# If an optimal solution has been found, print results
if status == cp_model.OPTIMAL:
    print('================= Solution =================')
    print(f'Solved in {solver.WallTime():.2f} milliseconds')
    print()
    print(f'Optimal value = {3*solver.Value(bread)+10*solver.Value(meat)+26*solver.Value(beer)} popularity')
    print('Food:')
    print(f' - 🥖Bread = {solver.Value(bread)}')
    print(f' - 🥩Meat  = {solver.Value(meat)}')
    print(f' - 🍺Beer  = {solver.Value(beer)}')
else:
    print('The solver could not find an optimal solution.')