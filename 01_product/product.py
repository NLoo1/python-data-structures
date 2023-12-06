def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """
    return a*b

print(str(product(1,2)) + " --> should be 2")
print(str(product(3,4)) + " --> should be 12")
print(str(product(5,6)) + " --> should be 30")