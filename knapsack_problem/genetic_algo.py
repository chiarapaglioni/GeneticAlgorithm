import random
import item

# Genetic algorithm parameters
pop_size = 10
item_num = 5
simulations = 10
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
        population.append(new_individual)
    return population


# Calculate the fitness of one individual based on the items (0 = excluded, 1 = included)
def get_fitness(individual):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == '1':
            fitness = fitness + items[i].value
    return fitness


def get_population_fitness(popul):
    fitness_vals = []
    for i in range(len(popul)):
        fitness = get_fitness(popul[i])
        fitness_vals.append(fitness)
    return fitness_vals


def print_items(item_list):
    for i in range(len(item_list)):
        ind = "value: " + str(item_list[i].value) + " | weight: " + str(item_list[i].weight)
        print(ind)


def print_population(popul):
    for i in range(len(popul)):
        print("Individual " + str(i) + ": ", popul[i])


if __name__ == '__main__':
    items = initialize_items(item_num)
    population = initialize_population(pop_size, item_num)
    fitness_values = get_population_fitness(population)

    print('Items: ')
    print_items(items)
    print()
    print('Population: ')
    print_population(population)
    print()
    print('Fitness Values: ')
    print_population(fitness_values)
