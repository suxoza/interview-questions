matrix = [
    [1, 0, 0 ,1, 0],
    [1, 0, 1 ,0, 0],
    [0, 0, 1 ,0, 1],
    [1, 0, 1 ,0, 1],
    [1, 0, 1 ,1, 0],
]
founded = set()
def riverSizes(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current_pos = 0
            current = matrix[i][j]
            if current == 1 and is_saved(i, j):
                current_pos = get_next(matrix, i, j)
                result.append(current_pos)
                
    return result

def is_saved(first, second):
    if (first, second) not in founded:
        founded.add((first, second))
        return True
    return False

def get_next(matrix, i, j):
    count = 1
    if j < len(matrix[i]) - 1 and matrix[i][j + 1] == 1 and is_saved(i, j + 1):
        count += get_next(matrix, i, j + 1)
    if i < len(matrix) - 1 and matrix[i + 1][j] == 1 and is_saved(i + 1, j):
        count += get_next(matrix, i + 1, j)
    return count

print(riverSizes(matrix))

# 40 min