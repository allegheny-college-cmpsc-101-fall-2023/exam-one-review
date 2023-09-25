"""Practice Implementing from Scratch"""

# TODO: implement from scratch. Add imports as needed. Add type annotations

def compute_square_while(n):
    return

def compute_square_for(n):
    return

def primality_test_exhaustive(n):
    return

def primality_test_efficient(n):
    return

def compute_square_root_exhaustive(n):
    return

def compute_square_root_efficient(n):
    return

# bonus 1
def get_minimum(first: int, second: int, third: int) -> int:
    """Determine the smallest of the three provided values."""
    # TODO: write a function body that will return the smallest of
    # the three formal parameters to this function
    # There are multiple possible solutions.

# bonus 2
def get_largest_odd(first: int, second: int, third: int) -> Tuple[int, bool]:
    """Determine the largest odd number among the provided values."""
    # This function's job is to determine the largest odd number among
    # the provided three input values called first, second, and third.
    # If none of the numbers are odd, then determine the smallest of
    # the three values.
    # TODO: implement the body of the function.
    # Ultimately, make sure that the function returns two values in the
    # form (answer, found_odd), fitting the function's signature.
    # Be able to answer to yourself, what is the type of "found_odd"
    # Think about "found_odd" as asking: did your algorithm find the 
    # the largest odd number among the three inputs?

    # Use this exact line of code somewhere in the function
    # Call the get_minimum function to determine the smallest number
    answer = get_minimum(first, second, third)
    
    # The return below is a placeholder
    return (0, False)