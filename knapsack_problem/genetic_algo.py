import random
import item
import individual

# Genetic algorithm parameters
pop_size = 10
item_num = 5
simulations = 10
tournament_size = 3
mutation_rate = 0
crossover_rate = 0

# Knapsack problem parameters
max_knapsack_weight = 15

# Population
items = []
population = []


# Initialize n items randomly
def initialize_items(n):
    for i in range(n):
        weight = random.randint(1, 10)
        new_item = item.Item(i+1, weight)
        items.append(new_item)
    return items


# Initialize individuals of the population randomly
def initialize_population(size, n):
    for i in range(size):
        new_individual = ''
        for j in range(n):
            bit = random.randint(0, 1)
            new_individual = new_individual + str(bit)
        population.append(individual.Individual(new_individual, get_fitness(new_individual)))
    return population


# Calculate the fitness of one individual based on the items (0 = excluded, 1 = included)
def get_fitness(individual):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == '1':
            fitness = fitness + items[i].value
    return fitness


# Tournament selection:
# 1. Select random subset of the population
# 2. Return fittest individual of the tournament
def tournament_selection(popul, size):
    tournament = random.sample(popul, size)
    # Order the individuals in ascending order = the first one is the least fit
    tournament.sort(key=lambda x: x.fitness)
    # print_population(tournament)
    return tournament[size-1]


def print_items(item_list):
    for i in range(len(item_list)):
        it = "value: " + str(item_list[i].value) + " | weight: " + str(item_list[i].weight)
        print(it)


def print_population(popul):
    for i in range(len(popul)):
        ind = "Individual " + str(i) + ": " + str(popul[i].bitstring) + " | fitness: " + str(popul[i].fitness)
        print(ind)


if __name__ == '__main__':
    items = initialize_items(item_num)
    population = initialize_population(pop_size, item_num)

    print('Items: ')
    print_items(items)
    print()
    print('Population: ')
    print_population(population)
    print()

    # SELECTION
    fittest = tournament_selection(population, tournament_size)
    print("Fittest individual: ", str(fittest.bitstring) + " fitness: " + str(fittest.fitness))