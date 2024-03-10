from random import randint

class Vector:
    def __init__(self, components):
        self.components = components
    def copy(self):
        return Vector(self.components.copy())
    def dimension(self):
        return len(self.components)
    def lenght(self):
        return sum(comp**2 for comp in self.components)**0.5
    def average(self):
        return sum(self.components) / len(self.components)
    def max_component(self):
        if not self.components:
            return None
        return max(self.components)
    def min_component(self):
        if not self.components:
            return None
        return min(self.components)
    def __str__(self):
        return f"({', '.join(map(lambda x: str(int(x)), self.components))})"

def read_vectors(file_path):
    vectors = []
    with open(file_path, 'r') as file:
        for line in file:
            components = list(map(float, line.split()))
            vectors.append(Vector(components))
    return vectors

def max_dimension(vectors):
    max_dimension_vector = min_lenght_vector = vectors[0]
    max_dimension = min_lenght_vector.dimension()
    min_lenght = min_lenght_vector.lenght()
    for vector in vectors[1:]:
        dimension = vector.dimension()
        lenght = vector.lenght()
        if dimension > max_dimension or (dimension == max_dimension and lenght < min_lenght):
            max_dimension_vector = vector
            max_dimension = dimension
            min_lenght = lenght
    return max_dimension_vector

def max_len(vectors):
    max_lenght_vector = vectors[0]
    max_lenght = max_lenght_vector.lenght()
    min_dimension = vectors[0].dimension()
    for vector in vectors[1:]:
        lenght = vector.lenght()
        dimension = vector.dimension()
        if lenght > max_lenght or (lenght == max_lenght and dimension < min_dimension):
            max_lenght_vector = vector
            max_lenght = lenght
            min_dimension = dimension
    return max_lenght_vector

def average_len(vectors):
    total_lenght = sum(vector.lenght() for vector in vectors)
    return total_lenght / len(vectors)

def above_average_len(vectors):
    avg_lenght = average_len(vectors)
    return sum(1 for vector in vectors if vector.lenght() > avg_lenght)

def max_component(vectors):
    max_comp_vector = None
    for vector in vectors:
        comp_value = vector.max_component()
        if comp_value is not None and (max_comp_vector is None or comp_value > max_comp_vector.max_component()):
            max_comp_vector = vector
    return max_comp_vector

def min_component(vectors):
    min_comp_vector = vectors[0]
    for vector in vectors[1:]:
        comp_value = vector.min_component()
        if comp_value is not None and (min_comp_vector.min_component() is None or comp_value < min_comp_vector.min_component()):
            min_comp_vector = vector
    return min_comp_vector

if __name__ == "__main__":
    COMP_RANGE = 1000
    def generate(fname, vector_num, max_dim):
        with open(fname, "w", encoding='utf-8') as f_out:
            for i in range(vector_num):
                dim = randint(1, max_dim)
                for i in range(dim):
                    v = randint(-COMP_RANGE, COMP_RANGE)
                    print("%5d" % v, end=" ", file=f_out)
                print(file=f_out)
            print(file=f_out)

    generate("input01.txt", 10, 10)
    generate("input02.txt", 100, 50)
    generate("input03.txt", 500, 100)
    generate("input04.txt", 5000, 1000)

    file_paths = ["input01.txt", "input02.txt", "input03.txt", "input04.txt"]
    for file_path in file_paths:
        vectors = read_vectors(file_path)

        print(f"\nFile: {file_path}")
        print(f"Вектор з найбільшою розмірністю: {max_dimension(vectors)}")
        print(f"Вектор, що має найбільшу довжину: {max_len(vectors)}")
        print(f"Середня довжина серед векторів: {round(average_len(vectors), 3)}")
        print(f"Кількість векторів з довжиною вище середньої: {above_average_len(vectors)}")
        print(f"Вектор з максимальною компонентою: {max_component(vectors)}")
        print(f"Вектор з мінімальною компонентою: {min_component(vectors)}")
