from converter import convert_base
from validator import is_valid_base, is_valid_number

def print_welcome():
    """Display welcome message and program info"""
    print("=" * 60)
    print("MULTI-BASE NUMERICAL CONVERTER".center(60))
    print("=" * 60)
    print("This program converts numbers between different bases (2-16).")
    print("Base 2: Binary (0-1)")
    print("Base 8: Octal (0-7)")
    print("Base 10: Decimal (0-9)")
    print("Base 16: Hexadecimal (0-9, A-F)")
    print("=" * 60)

def get_valid_input(prompt, validator_func, *args):
    """
    Get and validate user input
    
    Args:
        prompt (str): The message to display to user
        validator_func (function): Function to validate input
        *args: Additional arguments for validator_func
    
    Returns:
        The validated input
    """
    while True:
        user_input = input(prompt)
        if validator_func(user_input, *args):
            return user_input
        print("Invalid input. Please try again.")

def main():
    """Main program function"""
    print_welcome()
    
    while True:
        # Get from base
        from_base_str = get_valid_input("Enter the original base (2-16): ", is_valid_base)
        from_base = int(from_base_str)
        
        # Get number in the original base
        number = get_valid_input(
            f"Enter the number in base {from_base}: ", 
            is_valid_number, 
            from_base
        )
        
        # Get to base
        to_base_str = get_valid_input("Enter the target base (2-16): ", is_valid_base)
        to_base = int(to_base_str)
        
        # Perform conversion
        result = convert_base(number, from_base, to_base)
        
        # Display result
        print("\nResult:")
        print(f"{number} (base {from_base}) = {result} (base {to_base})")
        
        # Ask if user wants to do another conversion
        another = input("\nDo you want to perform another conversion? (y/n): ")
        if another.lower() != 'y':
            break
    
    print("Thank you for using the Multi-Base Numerical Converter!")

if __name__ == "__main__":
    main()