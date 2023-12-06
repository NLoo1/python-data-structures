def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    return None if len(lst)==0 else 0op[]\eiqrtuwy list[-1]
    if(len(lst) == 0):
        return None;
    else:
        return lst[-1]
    
print(str(last_element([])) + " should be " + "None");
print(str(last_element([1,2,3])) + " should be " + "3");
print(str(last_element([1,2,3,4,5])) + " should be " + "5");