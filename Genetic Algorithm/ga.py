import random

# Define the fitness function
def fitness(x, y):
    return 100 * (x**2 - y)**2 + (1 - x)**2

# Genetic algorithm parameters
population_size = 10
num_generations = 5
mutation_rate = 0.01

# Initialize the population
def initialize_population():
    return [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(population_size)]

# Perform tournament selection
def select_parents(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    return parent1, parent2

# Define the crossover (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Perform mutation
def mutate(child):
    child = list(child)  # Convert tuple to list
    for i in range(len(child)):
        if random.random() < mutation_rate:
            child[i] = random.uniform(0, 1)
    return tuple(child)  # Convert list back to tuple if needed

# Evaluate fitness for each individual
def evaluate_population(population):
    return [fitness(x, y) for x, y in population]

# Main genetic algorithm loop
population = initialize_population()
for generation in range(num_generations):
    fitness_scores = evaluate_population(population)
    best_individual = population[fitness_scores.index(min(fitness_scores))]
    new_population = [best_individual]  # Elitism: Keep the best individual

    print(f"generation-{generation}")
    
    print(f"population: ")
    for x, y in population:
      print(f"({x:.4f}, {y:.4f})")
    
    print(f"fitness score: ")
    for score in fitness_scores:
      print(f"{score:.4f}")
    
    print(f"best individual: ({best_individual[0]:.4f}, {best_individual[1]:.4f})")
    
    while len(new_population) < population_size:
        parent1, parent2 = select_parents(population)
        child1, child2 = crossover(parent1, parent2)
        mutate(child1)
        mutate(child2)
        new_population.extend([child1, child2])

    population = new_population

# Extract the optimal solution
x_optimal, y_optimal = best_individual
best_fitness_score = fitness(x_optimal, y_optimal)

print(f"Optimal solution: x = {x_optimal:.4f}, y = {y_optimal:.4f}")
print(f"Best fitness score: {best_fitness_score:.4f}")
