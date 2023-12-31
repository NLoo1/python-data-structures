def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    output = []
    for x in range(num):
        if (not x == 0 and num%x == 0):
            output.append(x)
    output.append(num)
    return output

print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(321421))