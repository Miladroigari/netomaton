import netomaton as ntm


if __name__ == '__main__':

    adjacency_matrix = ntm.network.cellular_automaton(n=200)

    initial_conditions = [0] * 100 + [1] + [0] * 99

    activities, adjacencies = ntm.evolve(initial_conditions, adjacency_matrix, timesteps=100,
                                         activity_rule=lambda ctx: ntm.rules.nks_ca_rule(ctx, 30))

    ntm.plot_grid(activities)
