def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if(day_of_week < 1 or day_of_week > 7):
        return "None"
    elif(day_of_week == 1):
        return "Sunday"
    elif(day_of_week == 2):
        return "Monday"
    elif(day_of_week == 3):
        return "Tuesday"
    elif(day_of_week == 4):
        return "Wednesday"
    elif(day_of_week == 5):
        return "Thursday"
    elif(day_of_week == 6):
        return "Friday"
    elif(day_of_week == 7):
        return "Saturday"
    else:
        return "Invalid input"
    
print(weekday_name(1) + " should be " + "Sunday")
print(weekday_name(2) + " should be " + "Monday")
print(weekday_name(3) + " should be " + "Tuesday")
print(weekday_name(4) + " should be " + "Wednesday")
print(weekday_name(5) + " should be " + "Thursday")
print(weekday_name(6) + " should be " + "Friday")
print(weekday_name(7) + " should be " + "Saturday")
print(weekday_name(8) + " should be " + "None")