from submission import getSanJoseShortestPathProblem
from util import UniformCostSearch
import json

   # Run the search algorithm
problem = getSanJoseShortestPathProblem()
ucs = UniformCostSearch()
solution = ucs.solve(problem)

if solution:
       # Extract path from solution
    path = [problem.startLocation] + [action for action, state, cost in solution]
    print(path)
       # Save to JSON file
    data = {"path": path, "waypointTags": []}
    with open("path.json", "w") as f:
        json.dump(data, f, indent=2)
       
    print(f"Solution found! Path saved to path.json")
    print(f"Path length: {len(path)}")
else:
    print("No solution found!")