import matplotlib.pyplot as plt
import numpy as np

# Genetic algorithm parameters
population_size = 500
num_generations = 100
plot_interval=10

# Define the city class
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        return np.sqrt((self.x - city.x)**2 + (self.y - city.y)**2)

    def __repr__(self):
        return f'({self.x}, {self.y})'

# Define a fixed list of cities with specific coordinates
cities = [
    City(20, 30), City(40, 20), City(35, 10), City(50, 40), City(10, 5),
    City(55, 25), City(60, 45), City(30, 20), City(25, 30), City(5, 25),
    City(15, 35), City(45, 15), City(40, 10), City(55, 35), City(20, 5),
    City(50, 30), City(65, 40), City(35, 25), City(20, 35), City(10, 20),
    City(25, 45), City(50, 25), City(30, 15), City(45, 40), City(15, 10),
    City(60, 30), City(70, 50), City(40, 25), City(35, 30), City(15, 20),
    City(25, 10), City(55, 20), City(45, 5),  City(65, 35), City(30, 10),
    City(50, 45), City(75, 40), City(45, 30), City(25, 40), City(20, 15),
    City(35, 50), City(60, 20), City(40, 35), City(55, 45), City(25, 5),
    City(70, 30), City(80, 45), City(50, 20), City(45, 25), City(30, 40)
]

# Create a function to generate a fixed path
def generate_fixed_path(cities):
    # Example of a fixed path: sorted by x-coordinate
    return sorted(cities, key=lambda city: city.x)

# Define the crossover function
def crossover(path1, path2):
    crossover_point = np.random.randint(1, len(path1))
    new_path1 = path1[:crossover_point] + [city for city in path2 if city not in path1[:crossover_point]]
    new_path2 = path2[:crossover_point] + [city for city in path1 if city not in path2[:crossover_point]]
    return new_path1, new_path2

# Define the mutation function
def mutate(path):
    idx1, idx2 = np.random.randint(0, len(path), 2)
    path[idx1], path[idx2] = path[idx2], path[idx1]

# Define the total distance function
def total_distance(path):
    return sum([path[i].distance(path[i+1]) for i in range(len(path) - 1)])

# Define the plot_path helper function
def plot_path(ax, path, generation=None, is_final=False):
    ax.clear()
    path_distance = total_distance(path)
    for i in range(len(path)):
        x_coords = [path[i-1].x, path[i].x]
        y_coords = [path[i-1].y, path[i].y]
        ax.plot(x_coords, y_coords, 'b')
        ax.plot(path[i].x, path[i].y, 'ro')

    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')

    if is_final:
        title = f'Final Traveling Salesman Path - Total Distance: {path_distance:.4f}'
    else:
        title = (
            f'Traveling Salesman Path - Generation {generation} - '
            f'Total Distance: {path_distance:.4f}'
        )
    ax.set_title(title)

# Define the genetic algorithm function
def genetic_algorithm(population_size, num_generations, plot_interval):
    plt.ioff()  # Turn off interactive mode for the final plot
    fig, ax = plt.subplots(figsize=(10, 5))

    # Initialize population with a fixed path
    population = [generate_fixed_path(cities) for _ in range(population_size)]
    for generation in range(num_generations):
        population = sorted(population, key=total_distance)
        if generation % plot_interval == 0:
            plot_path(ax, population[0], generation=generation)
            plt.draw()
            plt.pause(0.1)
        
        next_generation = population[:2]  # Elitism
        while len(next_generation) < population_size:
            parent_indices = np.random.choice(len(population[:10]), 2, replace=False)
            parent1, parent2 = population[parent_indices[0]], population[parent_indices[1]]
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            next_generation.extend([child1, child2])
        population = next_generation

    # Display the final plot in a blocking mode
    plot_path(ax, population[0], is_final=True)
    plt.show()

# Main genetic algorithm
best_route = genetic_algorithm(population_size, num_generations, plot_interval)
