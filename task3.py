
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
    
    

# Example usage:


max_depth = 0
result = generate_recursive_language_M(max_depth)
print(result)  # Should print "x"

max_depth = 1
result = generate_recursive_language_M(max_depth)
print(result)  # Should print "yxz"

max_depth = 2
result = generate_recursive_language_M(max_depth)
print(result)  # Should print "yyxzz"

max_depth = 3
result = generate_recursive_language_M(max_depth)
print(result)  # Should print "yyyxzzz"
