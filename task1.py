## make function that determines if a string belongs to the language
## L = {a*b* | n>=1} over alphabet {a,b}
## where number of 'a's equals number of 'b's
## and all 'a's come before all 'b's
## and there is at least 1 'a' and 1 'b'
    



def is_in_language_L(string):
    """
    Check if a string belongs to language L = {a^n b^n | n >= 1}
    
    Args:
        string (str): Input string to check
    
    Returns:
        bool: True if string is in L, False otherwise
    
    Examples:
        is_in_language_L("ab") -> True
        is_in_language_L("aabb") -> True  
        is_in_language_L("aaabbb") -> True
        is_in_language_L("aba") -> False
        is_in_language_L("") -> False
    """
    count_a = 0
    count_b = 0
    for char in string:
        if char == 'a':
            count_a += 1
        if char == 'b':
            count_b += 1

    if count_a != count_b or count_a == 0 or count_b == 0:
        return False
    
    seen_b = False
    for char in string:
        if char == 'a' and seen_b:
            return False
        if char == 'b':
            seen_b = True
    return True
    pass
# Example usage:


print(is_in_language_L("ab"))  # True
print(is_in_language_L("aabb"))  # True
print(is_in_language_L("aaabbb"))  # True
print(is_in_language_L("aba"))  # False
print(is_in_language_L(""))  # False   