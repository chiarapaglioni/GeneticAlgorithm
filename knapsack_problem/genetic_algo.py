import random
import item
import individual

# Genetic algorithm parameters
pop_size = 10
item_num = 5
simulations = 10
tournament_size = 3
mutation_rate = 0.1
crossover_rate = 0.5

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
def get_fitness(ind):
    fitness = 0
    for i in range(len(ind)):
        if ind[i] == '1':
            fitness = fitness + items[i].value
    return fitness


# TOURNAMENT SELECTION:
# 1. Select random subset of the population
# 2. Return fittest individual of the tournament
def tournament_selection(popul, size):
    tournament = random.sample(popul, size)
    # Order the individuals in ascending order = the first one is the least fit
    tournament.sort(key=lambda x: x.fitness)
    # print_population(tournament)
    return tournament[size-1]


# CROSSOVER
# 1. Define crossover point
# 2. Create child based on crossover point
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1.bitstring))
    first_part = parent1.bitstring[:crossover_point]
    second_part = parent2.bitstring[crossover_point:]
    child_bitstring = first_part + second_part
    child = individual.Individual(child_bitstring, get_fitness(child_bitstring))
    return child


# MUTATION
# 1. Retrieve two bits from the individual's bitstring
# 2. Swap the two bits of the bitstring
def mutation(ind):
    index1, index2 = random.sample(range(0, len(ind.bitstring)), 2)
    temp = list(ind.bitstring)
    temp[index1], temp[index2] = temp[index2], temp[index1]
    mutated_bitstring = ''.join(temp)
    mutated_ind = individual.Individual(mutated_bitstring, get_fitness(mutated_bitstring))
    return mutated_ind


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
    new_population = []
    while not len(new_population) == len(population):
        fittest1 = tournament_selection(population, tournament_size)
        fittest2 = tournament_selection(population, tournament_size)
        # print("Fittest individual: ", str(fittest.bitstring) + " fitness: " + str(fittest.fitness))
        child1 = fittest1
        child2 = fittest2

        # CROSSOVER
        if random.random() < crossover_rate:
            child1 = crossover(fittest1, fittest2)
            child2 = crossover(fittest2, fittest1)

            # MUTATION
            if random.random() < mutation_rate:
                child1 = mutation(child1)
                child2 = mutation(child2)

        new_population.append(child1)
        new_population.append(child2)

    print('New Population after Selection: ')
    print_population(new_population)
    print()
