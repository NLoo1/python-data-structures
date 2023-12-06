def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    ctLetter = 0;
    letter = letter.upper();
    word = word.upper();
    for char in word:
        if char == letter:
            ctLetter +=1
    return str(ctLetter)

print(single_letter_count("Hello World", "h") + " should be " + "1")
print(single_letter_count('Hello World', 'z') + " should be " + "0")
print(single_letter_count("Hello World", 'l') + " should be " + "3")