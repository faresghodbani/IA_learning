import importlib
import random
import time

puzzle = importlib.import_module('8puzzle')
goal = puzzle.EightPuzzle('1 2 3 4 5 6 7 8 0')

nb_tests = 10     
n_moves = 10       

temps_manhatten = []
temps_misplaced = []

for _ in range(nb_tests):
    initial = goal
    for _ in range(n_moves):
        initial = random.choice(initial.neighbors())[0]

    h1 = puzzle.EightPuzzle.manhatten_distance
    start = time.time()
    initial.a_star(goal, h1, puzzle.EightPuzzle.state_transition)
    temps_manhatten.append(time.time() - start)

    h2 = puzzle.EightPuzzle.tile_switches_remaining
    start = time.time()
    initial.a_star(goal, h2, puzzle.EightPuzzle.state_transition)
    temps_misplaced.append(time.time() - start)

def stats(temps):
    return {
        "min": min(temps),
        "max": max(temps),
        "moyenne": sum(temps)/len(temps)
    }

stats_manhatten = stats(temps_manhatten)
stats_misplaced = stats(temps_misplaced)

print("Statistiques pour Manhattan :", stats_manhatten)
print("Statistiques pour Tiles misplaced :", stats_misplaced)
