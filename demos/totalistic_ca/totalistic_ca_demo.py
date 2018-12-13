from netomaton import *


if __name__ == '__main__':

    adjacencies = AdjacencyMatrix.cellular_automaton(n=200)

    initial_conditions = [0]*100 + [1] + [0]*99

    activities, connectivities = evolve(initial_conditions, adjacencies, timesteps=100,
                                        activity_rule=lambda n, c, t: ActivityRule.totalistic_ca(n, k=3, rule=777))

    plot_grid(activities)
