import random
import math
import path
import city

# Genetic algorithm parameters
pop_size = 20
city_num = 5
simulations = 10
tournament_size = 3
mutation_rate = 0.1
crossover_rate = 0.5

# TSP parameters
city_locations = []

# Population
cities = []
population = []


# Initialize n items randomly
# Name of a city = a single character
# Location of a city = its position in the unit circle (starting from 0 and moving counter clockwise)
# TODO: correct function such that the same angle does not appear twice
def initialize_cities(n):
    for i in range(n):
        new_city = city.City(chr(i+1 * 64 + 1), i)
        cities.append(new_city)
    return cities


# Initialize individuals of the population randomly
def initialize_population(size, n):
    for i in range(size):
        new_individual = ''
        for j in range(n):
            bit = random.randint(64, 64+n)
            new_individual = new_individual + chr(bit)
        population.append(path.Path(new_individual, get_fitness(new_individual)))
    return population


# TODO: do i consider the smallest angle in the unit circle between two cities or just the one counter clockwise?
def get_distance(city1, city2):
    angle = abs(city1.location - city2.location) * (360/city_num)
    distance = math.sqrt(2 - 2 * math.cos(angle))
    return distance


# Calculate the fitness of one individual based on the items (0 = excluded, 1 = included)
# TODO: adapt fitness function to the distance of the cities
def get_fitness(path_string):
    fitness = 0
    for i in range(len(path_string)-1):
        for j in range(len(cities)):
            fitness = fitness + 1
    return fitness


# Compute average fitness of the population
def get_average_fitness(popul):
    avg_fitness = 0
    for i in range(len(popul)):
        avg_fitness = avg_fitness + popul[i].fitness
    return avg_fitness/len(popul)


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
    child = path.Path(child_bitstring, get_fitness(child_bitstring))
    return child


# MUTATION
# 1. Retrieve two bits from the individual's bitstring
# 2. Swap the two bits of the bitstring
def mutation(ind):
    index1, index2 = random.sample(range(0, len(ind.bitstring)), 2)
    temp = list(ind.bitstring)
    temp[index1], temp[index2] = temp[index2], temp[index1]
    mutated_bitstring = ''.join(temp)
    mutated_ind = path.Path(mutated_bitstring, get_fitness(mutated_bitstring))
    return mutated_ind


def print_cities(city_list):
    for i in range(len(city_list)):
        it = "name: " + str(city_list[i].name) + " | location: " + str(city_list[i].location)
        print(it)


def print_population(popul):
    for i in range(len(popul)):
        ind = "Individual " + str(i) + ": " + str(popul[i].bitstring) + " | fitness: " + str(popul[i].fitness)
        print(ind)


if __name__ == '__main__':
    cities = initialize_cities(city_num)
    population = initialize_population(pop_size, city_num)

    print('Cities: ')
    print_cities(cities)
    print()
    # print('Population: ')
    # print_population(population)
    print()
    print('Average fitness original population: ', get_average_fitness(population))
    print()

    # GENETIC ALGORITHM
    # for i in range(simulations):
    #     new_population = []
    #     while not len(new_population) == len(population):
    #         fittest1 = tournament_selection(population, tournament_size)
    #         fittest2 = tournament_selection(population, tournament_size)
    #         # print("Fittest individual: ", str(fittest.bitstring) + " fitness: " + str(fittest.fitness))
    #         child1 = fittest1
    #         child2 = fittest2
    #
    #         # CROSSOVER
    #         if random.random() < crossover_rate:
    #             child1 = crossover(fittest1, fittest2)
    #             child2 = crossover(fittest2, fittest1)
    #
    #             # MUTATION
    #             if random.random() < mutation_rate:
    #                 child1 = mutation(child1)
    #                 child2 = mutation(child2)
    #
    #         new_population.append(child1)
    #         new_population.append(child2)
    #
    #     population = new_population
    #     average_fitness = get_average_fitness(new_population)
    #
    #     print('New average fitness simulation' + str(i) + ': ', average_fitness)
    #     print()
    #
    #     # Stop when the average fitness is equal to the maximum capacity of the knapsack
    #     if average_fitness == max_knapsack_weight:
    #         print('Success!!!')
    #         print('Optimal Solution: ', new_population[0].bitstring)
    #         break
