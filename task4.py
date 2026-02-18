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
                print(f"Unsupported character in pattern: {char}")
                return False
        for char in string:
            if char not in ['a', 'b']:
                print(f"Unsupported character in string: {char}")
                return False
        if pattern == "" or string == "":
            print("Empty pattern or string, returning False")
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


print(regex_match("a*", "aaa")) # -> True
print(regex_match("a*b", "aab")) # -> True
print(regex_match("a|b", "a")) # -> True
print(regex_match("a|b", "c")) # -> False