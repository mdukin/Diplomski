import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def evaluate(self, variables):
        """Procjenjuje vrijednost stabla za zadane varijable."""
        if isinstance(self.value, str):  # Ako je operator
            left_val = self.left.evaluate(variables)
            right_val = self.right.evaluate(variables)
            if self.value == '+':
                return left_val + right_val
            elif self.value == '-':
                return left_val - right_val
            elif self.value == '*':
                return left_val * right_val
            elif self.value == '/':
                return left_val / right_val if right_val != 0 else 1  # Izbjegavanje dijeljenja s nulom
        else:
            # Ako je konstanta ili varijabla
            return variables.get(self.value, self.value)
        

def random_tree(depth, variables):
    if depth == 0 or (depth > 1 and random.random() < 0.3):
        # List - konstanta ili varijabla
        if random.random() < 0.5:
            return Node(random.choice(variables))  # Varijabla
        else:
            return Node(random.uniform(-10, 10))  # Konstanta
    else:
        # Operator
        operator = random.choice(['+', '-', '*', '/'])
        return Node(operator, random_tree(depth - 1, variables), random_tree(depth - 1, variables))

def crossover(tree1, tree2):
    if random.random() < 0.5:
        return tree1
    if tree1 is None or tree2 is None:
        return tree1 if tree2 is None else tree2
    new_tree = Node(tree1.value if random.random() < 0.5 else tree2.value)
    new_tree.left = crossover(tree1.left, tree2.left) if tree1.left or tree2.left else None
    new_tree.right = crossover(tree1.right, tree2.right) if tree1.right or tree2.right else None
    return new_tree

def mutate(tree, depth, variables, mutation_rate=0.1):
    if tree is None or random.random() > mutation_rate:
        return tree
    if random.random() < 0.5:  # Zamijeni cijeli čvor novim pod-stablom
        return random_tree(depth, variables)
    tree.left = mutate(tree.left, depth - 1, variables, mutation_rate)
    tree.right = mutate(tree.right, depth - 1, variables, mutation_rate)
    return tree

def fitness(tree, target_function, data):
    error = 0
    for vars_set, target in data:
        prediction = tree.evaluate(vars_set)
        error += abs(prediction - target)
    return -error  # Niži error, bolja prilagodba

def genetic_programming(target_function, variables, data, population_size=50, generations=100):
    # Generiraj početnu populaciju
    population = [random_tree(4, variables) for _ in range(population_size)]

    for generation in range(generations):
        # Izračunaj fitness populacije
        fitness_scores = [(tree, fitness(tree, target_function, data)) for tree in population]
        fitness_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Ispis najboljeg rješenja
        print(f"Generacija {generation}: Najbolji fitness = {fitness_scores[0][1]}")

        # Selektiraj najbolje jedinke
        selected = [tree for tree, score in fitness_scores[:population_size // 2]]

        # Generiraj novu populaciju
        new_population = selected[:]
        while len(new_population) < population_size:
            if random.random() < 0.7:  # Križanje
                parent1 = random.choice(selected)
                parent2 = random.choice(selected)
                new_population.append(crossover(parent1, parent2))
            else:  # Mutacija
                new_population.append(mutate(random.choice(selected), 4, variables))

        population = new_population

    # Vraća najbolje rješenje
    return fitness_scores[0][0]

# Definiraj ciljnu funkciju i podatke
target_function = lambda x: x**2
variables = ['x']
data = [({'x': x}, x**2) for x in range(-10, 11)]

# Pokreni genetsko programiranje
best_tree = genetic_programming(target_function, variables, data)

# Prikaz najboljeg rješenja
print("Najbolje stablo:", best_tree)
