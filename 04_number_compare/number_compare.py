def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    return "First is greater" if a > b else "Second is greater" if a < b else "Both are equal"

print(number_compare(1,2) + " should be " + "Second is greater")
print(number_compare(2,1) + " should be " + "First is greater")
print(number_compare(1,1) + " should be " + "Both are equal")