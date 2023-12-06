def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'Aaaahhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    # [to_swap]-[current letter] 

    # phraseArray = list(phrase)
    # for x in range(len(phraseArray)):
    #     if(to_swap.isupper()): # A
    #         if(to_swap == phraseArray[x]): # A - A
    #             phraseArray[x] = to_swap.lower() # A-A -> A-a
    #         elif(to_swap.lower() == phraseArray[x]): # A - a
    #             phraseArray[x] = to_swap # A - A --> A-a
    #     elif(to_swap.islower()): # a
    #         if(to_swap == phraseArray[x]): # a-a
    #             phraseArray[x] = to_swap.upper() #a-a --> a-A
    #         elif(to_swap.upper() == phraseArray[x]): #a-A
    #             phraseArray[x] = to_swap #a-A --> a-a
    
    # phraseString = ""
    # for x in range(len(phraseArray)):
    #     phraseString += phraseArray[x]
    # return phraseString


    # Apparently this can all be done in one line instead of looping twice.
    return ''.join([c.lower() if c == to_swap.upper() else c.upper() if c == to_swap.lower() else c for c in phrase])


print(flip_case('Aaaahhh', 'a')) # 'aAAAhhh'
print(flip_case('Aaaahhh', 'A')) # 'Aaaahhh'
print(flip_case('Aaaahhh', 'h')) # 'AaaaHHH'



