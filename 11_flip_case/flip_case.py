def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'Aaaahhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    return ''.join([c.lower() if c == to_swap.upper() else c.upper() if c == to_swap.lower() else c for c in phrase])


print(flip_case('Aaaahhh', 'a')) # 'aAAAhhh'
print(flip_case('Aaaahhh', 'A')) # 'Aaaahhh'
print(flip_case('Aaaahhh', 'h')) # 'AaaaHHH'



