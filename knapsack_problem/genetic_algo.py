import random
import individual

# Genetic algorithm parameters
pop_size = 10
simulations = 10
mutation_rate = 0
crossover_rate = 0

# Knapsack problem parameters
max_knapsack_weight = 10

# Population
population = []


# Initialize random population
def initialize_population(size):
    n = 5

    for i in range(size):
        value = ""
        for j in range(n):
            bit = random.randint(0, 1)
            value += str(bit)

        weight = random.randint(1, 10)
        new_individual = individual.Individual(i, value, weight)
        population.append(new_individual)

    return population


def print_population(popul):
    for i in range(len(popul)):
        ind = "id : " + str(popul[i].id) + " | value: " + str(popul[i].value) + " | weight: " + str(popul[i].weight)
        print(ind)


if __name__ == '__main__':
    population = initialize_population(pop_size)
    print_population(population)

