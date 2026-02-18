# Name: Aedan Leavitt
# Student ID: W01430157
# Date: 2/18/2026


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

## make function that generates all strings from Kleene closure (L*) of a given base language up to a specified length
def kleene_closure_generator(base_language, max_length):
    """
    Generate all strings in L* (Kleene closure) up to max_length
    
    Args:
        base_language (list): List of strings representing the base language
        max_length (int): Maximum length of generated strings
    
    Returns:
        set: Set of all strings in L* with length <= max_length
    
    Example:
        kleene_closure_generator(["a", "bb"], 4) should include:
        - "" (empty string, always in L*)
        - "a", "bb" (from L¹)
        - "aa", "abb", "bba", "bbbb" (from L²)
        - etc.
    """
    # Your implementation here
    result = set()
    result.add("")  # Include the empty string
    def generate(current_string):
        if len(current_string) > max_length: # check length constraint
            return
        if current_string != "": # check if the string is not empty, if it is, it is already in the set from before generate function
            result.add(current_string)
        for word in base_language: # iterate through each word in the base language
            generate(current_string + word) # add the word to the current string
    generate("") # start with an empty string
    return result
    pass

## make a recursive function to generate strings from a recursively defined language
##Base case: "x" ∈ M
##Recursive case: If w ∈ M, then "y" + w + "z" ∈ M
##
##This generates strings like: "x" or "yxz" or "yyxzz" or "yyyxzzz", etc.
def generate_recursive_language_M(max_depth):
    """
    Generate the nth string in language M using recursive definition
    
    Args:
        max_depth (int): Maximum depth of recursion (0 = base case)
    
    Returns:
        str: The string generated at recursion depth n
    
    Examples:
        generate_recursive_language_M(0) -> "x"
        generate_recursive_language_M(1) -> "yxz"
        generate_recursive_language_M(2) -> "yyxzz"
        generate_recursive_language_M(3) -> "yyyxzzz"
    """
    # Your implementation here
    # return a single string generated at depth max_depth
    if max_depth == 0:
        return "x"
    else: 
        return "y" + generate_recursive_language_M(max_depth - 1) + "z"
    

# implement a basic regular expression matcher to validate strings against patterns using concatentation, union(|), and kleene star (*)
# no external regex libraries allowed, implement parsing
def regex_match(pattern, string):
    """
    Check if string matches the given regular expression pattern
    Support basic operations: concatenation, | (union), * (Kleene star)
    
    Args:
        pattern (str): Regular expression pattern
        string (str): String to match against pattern
    
    Returns:
        bool: True if string matches pattern, False otherwise
    
    Supported patterns:
        - Single characters: 'a' matches "a"
        - Union: 'a|b' matches "a" or "b"  
        - Kleene star: 'a*' matches "", "a", "aa", "aaa", etc.
        - Concatenation: 'ab' matches "ab"
        - Combined: 'a*b|c' matches strings of a's followed by b, or just c
    
    Examples:
        regex_match("a*", "aaa") -> True
        regex_match("a*b", "aab") -> True
        regex_match("a|b", "a") -> True
        regex_match("a|b", "c") -> False
    """
    # Your implementation here
    # check if pattern and string are valid, only contain supported characters
    def validate_input(pattern, string):
        for char in pattern:
            if char not in ['a', 'b', '|', '*']:
                #print(f"Unsupported character in pattern: {char}")
                return False
        for char in string:
            if char not in ['a', 'b']:
                #print(f"Unsupported character in string: {char}")
                return False
        if pattern == "" or string == "":
            #print("Empty pattern or string, returning False")
            return False
    validate_input(pattern, string)
    # now check for the pattern matching
    # do it via recursion
    def match_helper(pat, s):
        #print(pat, s)
        if pat == "":
            return s == ""
        if pat[0] == '|':
            # '|' can match either the left or right side
            left_pat = pat[:pat.find('|')]
            right_pat = pat[pat.find('|') + 1:]
            return match_helper(left_pat, s) or match_helper(right_pat, s)
        elif pat[0] == 'a' or pat[0] == 'b':
            # must be regular character, so check if next character is '*' for kleene star
            if len(pat) > 1 and pat[1] == '*':
                # try matching one or 0 occurrences of the character recursively
                if s and pat[0] == s[0]:
                    # try matching one occurrence, if it matches, continue matching but with the same pattern and string without the first character, or try matching zero occurrences by skipping the character and '*' in the pattern
                    return match_helper(pat, s[1:]) or match_helper(pat[2:], s)
                else:
                    return match_helper(pat[2:], s) # try matching zero occurrences
            if s and pat[0] == s[0]:
                return match_helper(pat[1:], s[1:])
            return False
     
            
    result = match_helper(pattern, string)
    #print(f"regex_match('{pattern}', '{string}') -> {result}")
    return result


def test_assignment():
    # Test Task 1: Language L membership
    assert is_in_language_L("ab") == True
    assert is_in_language_L("aabb") == True
    assert is_in_language_L("aaabbb") == True
    assert is_in_language_L("aabbb") == False
    assert is_in_language_L("aba") == False
    assert is_in_language_L("") == False
    assert is_in_language_L("a") == False
    assert is_in_language_L("b") == False
    
    # Test Task 2: Kleene closure
    result = kleene_closure_generator(["a"], 3)
    expected = {"", "a", "aa", "aaa"}
    assert result == expected
    
    result2 = kleene_closure_generator(["ab"], 4)
    assert "" in result2
    assert "ab" in result2
    assert "abab" in result2
    assert len([s for s in result2 if len(s) <= 4]) >= 3
    
    # Test Task 3: Recursive language
    assert generate_recursive_language_M(0) == "x"
    assert generate_recursive_language_M(1) == "yxz"
    assert generate_recursive_language_M(2) == "yyxzz"
    assert generate_recursive_language_M(3) == "yyyxzzz"
    
    # Test Task 4: Regular expressions
    assert regex_match("a*", "") == True
    assert regex_match("a*", "aaa") == True
    assert regex_match("a*b", "aaab") == True
    assert regex_match("a|b", "a") == True
    assert regex_match("a|b", "c") == False
    assert regex_match("ab", "ab") == True
    assert regex_match("ab", "a") == False
    
    print("All tests passed!")

if __name__ == "__main__":
    test_assignment()