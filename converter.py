def to_decimal(number_str, base):
    """
    Convert a number from the given base to decimal (base 10)
    
    Args:
        number_str (str): The number as a string
        base (int): The base of the number (2-16)
    
    Returns:
        int: The decimal representation of the number
    """
    decimal_value = 0
    # Dictionary to map hexadecimal characters to their decimal values
    hex_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    # Convert the number to uppercase to handle both 'a' and 'A' inputs
    number_str = number_str.upper()
    
    # Process each digit from right to left
    for i, digit in enumerate(reversed(number_str)):
        # Convert the digit to its decimal value
        if digit.isdigit():
            digit_value = int(digit)
        else:
            digit_value = hex_map[digit]
        
        # Add the digit's contribution to the total
        decimal_value += digit_value * (base ** i)
    
    return decimal_value

def from_decimal(decimal_value, base):
    """
    Convert a decimal number to a number in the given base
    
    Args:
        decimal_value (int): The decimal number
        base (int): The target base (2-16)
    
    Returns:
        str: The representation in the target base
    """
    if decimal_value == 0:
        return '0'
    
    # Dictionary to map decimal values to hexadecimal characters
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    result = ""
    
    # Convert using the division-remainder method
    while decimal_value > 0:
        remainder = decimal_value % base
        
        # Convert the remainder to the appropriate character
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = hex_map[remainder] + result
        
        decimal_value //= base
    
    return result

def convert_base(number_str, from_base, to_base):
    """
    Convert a number from one base to another
    
    Args:
        number_str (str): The number as a string
        from_base (int): The base of the input number
        to_base (int): The base to convert to
    
    Returns:
        str: The number represented in the target base
    """
    # First convert to decimal, then to the target base
    decimal_value = to_decimal(number_str, from_base)
    return from_decimal(decimal_value, to_base)