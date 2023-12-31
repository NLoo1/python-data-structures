def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    if isinstance(collection, (list, str, set, tuple)):
        if(start and not isinstance(collection, set)):
            for x in range(start, len(collection)): # Does NOT check for valid start
                if collection[x] == sought:
                    return True
            return False
        else:
            for char in collection:
                if char == sought:
                    return True
            return False
    elif isinstance(collection, dict):
        if(sought in collection.values()):
            return True
        return False
    return False
        

print(includes([1, 2, 3], 1)) # T
print(includes([1, 2, 3], 1, 2)) # F
print(includes("hello", "o")) #T
print(includes(('Elmo', 5, 'red'), 'red', 1)) #T
print(includes({1, 2, 3}, 1)) #T
print(includes({1, 2, 3}, 1, 3)) # T
print(includes({"apple": "red", "berry": "blue"}, "blue")) #T