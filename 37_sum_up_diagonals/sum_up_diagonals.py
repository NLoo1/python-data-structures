def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    n = len(matrix)
    
    diagonal1_sum = 0
    diagonal2_sum = 0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                diagonal1_sum += matrix[i][j]
            
            if i + j == n - 1:
                diagonal2_sum += matrix[i][j]
    
    return diagonal1_sum + diagonal2_sum

    # sum = 0;
    # for x in range(0,len(matrix)):
    #     currentListlength = len(matrix[x])
    #     sum+= matrix[x]


m1 = [
    [1,   2],
    [30, 40],
    ]

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]
print(sum_up_diagonals(m1))
print(sum_up_diagonals(m2))