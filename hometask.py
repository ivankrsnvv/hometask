def count_repeated_elements(matrix):
    unique_elements = set()
    repeated_counts = {}
    
    for row in matrix:
        for element in row:
            if element not in unique_elements:
                unique_elements.add(element)
            else:
                if element in repeated_counts:
                    repeated_counts[element] += 1
                else:
                    repeated_counts[element] = 1
    
    print("Повторяющиеся элементы:")
    for key, value in repeated_counts.items():
        print(f"{key}: {value}")

def find_main_diagonal_product(matrix):
    product = 1
    for i in range(min(len(matrix), len(matrix[0]))):
        product *= matrix[i][i]
    return product

def count_unique_elements(matrix):
    flattened = []
    for row in matrix:
        for item in row:
            flattened.append(item)
            
    return len(set(flattened))

example_matrix = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

count_repeated_elements(example_matrix)
print("Произведение элементов главной диагонали:", find_main_diagonal_product(example_matrix))
print("Количество уникальных элементов:", count_unique_elements(example_matrix))
