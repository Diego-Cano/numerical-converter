import unittest
from converter import to_decimal, from_decimal, convert_base

class TestConverter(unittest.TestCase):
    
    def test_to_decimal(self):
        """Test conversion from various bases to decimal"""
        # Test binary to decimal
        self.assertEqual(to_decimal("1010", 2), 10)
        
        # Test octal to decimal
        self.assertEqual(to_decimal("17", 8), 15)
        
        # Test hexadecimal to decimal
        self.assertEqual(to_decimal("1A", 16), 26)
        self.assertEqual(to_decimal("1a", 16), 26)  # Test case-insensitivity
        
        # Test base 3 to decimal
        self.assertEqual(to_decimal("21", 3), 7)
        
        # Edge cases
        self.assertEqual(to_decimal("0", 16), 0)
        self.assertEqual(to_decimal("FF", 16), 255)
    
    def test_from_decimal(self):
        """Test conversion from decimal to various bases"""
        # Test decimal to binary
        self.assertEqual(from_decimal(10, 2), "1010")
        
        # Test decimal to octal
        self.assertEqual(from_decimal(15, 8), "17")
        
        # Test decimal to hexadecimal
        self.assertEqual(from_decimal(26, 16), "1A")
        
        # Test decimal to base 3
        self.assertEqual(from_decimal(7, 3), "21")
        
        # Edge cases
        self.assertEqual(from_decimal(0, 2), "0")
        self.assertEqual(from_decimal(255, 16), "FF")
    
    def test_convert_base(self):
        """Test direct conversion between different bases"""
        # Binary to hexadecimal
        self.assertEqual(convert_base("1010", 2, 16), "A")
        
        # Hexadecimal to binary
        self.assertEqual(convert_base("A", 16, 2), "1010")
        
        # Octal to binary
        self.assertEqual(convert_base("17", 8, 2), "1111")
        
        # Base 3 to base 5 - FIXED: changed expected result from "14" to "31"
        self.assertEqual(convert_base("121", 3, 5), "31")
        
        # Edge cases
        self.assertEqual(convert_base("0", 8, 2), "0")
        self.assertEqual(convert_base("FFFF", 16, 2), "1111111111111111")

if __name__ == "__main__":
    unittest.main()