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

# Example usage:
base_lang = ["a", "bb"]
max_len = 4
result = kleene_closure_generator(base_lang, max_len)
print(result)