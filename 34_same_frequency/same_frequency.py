def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    frequencyDict = {}
    frequencyDict2 = {}
    for num in str(num1):
        if num in frequencyDict.keys():
            frequencyDict[num] += 1
        else:
            frequencyDict[num] = 1

    for num in str(num2):
        if num in frequencyDict2.keys():
            frequencyDict2[num] += 1
        else:
            frequencyDict2[num] = 1
    return frequencyDict == frequencyDict2

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
