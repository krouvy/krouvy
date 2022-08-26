random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]
for i in range(len(random_matrix)):
    maxim = max(random_matrix[i])
    minum = min(random_matrix[i])
    print('Max - ', maxim, 'index - ', random_matrix[i].index(maxim))
    print('Min - ', minum, 'index - ', random_matrix[i].index(minum))
    print()
