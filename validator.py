def is_valid_base(base_str):
    """
    Check if the input is a valid base between 2 and 16
    
    Args:
        base_str (str): The base as a string input
    
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        base = int(base_str)
        return 2 <= base <= 16
    except ValueError:
        return False

def is_valid_number(number_str, base):
    """
    Check if the number is valid for the given base
    
    Args:
        number_str (str): The number as a string
        base (int): The base to check against
    
    Returns:
        bool: True if valid, False otherwise
    """
    valid_digits = "0123456789ABCDEF"[:base]
    return all(digit.upper() in valid_digits for digit in number_str)
