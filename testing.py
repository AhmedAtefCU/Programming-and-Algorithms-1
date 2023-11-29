# Test case creation library
import unittest

# Library for mocking
from unittest.mock import patch

# Library for capturing output
from io import StringIO

# Import the functions and dictionary from the Morse code translator script
from morsecodeapp import text_to_morse, morse_to_text, morse_code_dict, history, display_history

class TestMorseCodeTranslator(unittest.TestCase):

    # Test case 1: Valid English text to Morse code conversion
    def test_english_to_morse(self):
        english_text = "COVENTRY UNIVERSITY"
        expected_morse_code = "-.-. --- ...- . -. - .-. -.--   ..- -. .. ...- . .-. ... .. - -.--"
        self.assertEqual(text_to_morse(english_text), expected_morse_code)
        
    # Test case 2: Valid Morse code to English text conversion
    def test_morse_to_english(self):
        morse_code = ".... . .-.. .-.. ---"
        expected_english_text = "Hello"
        self.assertEqual(morse_to_text(morse_code), expected_english_text)

    # Test case 3: Empty input error for encryption
    def test_empty_input_encryption(self):
        english_text = ""
        with self.assertRaises(ValueError) as context:
            text_to_morse(english_text)
        self.assertEqual(str(context.exception), "Cannot Encrypt Empty Space")

    # Test case 4: Empty input error for decryption
    def test_empty_input_decryption(self):
        morse_code = ""
        with self.assertRaises(ValueError) as context:
            morse_to_text(morse_code)
        self.assertEqual(str(context.exception), "Cannot Decrypt Empty Space")

    # Test case 5: Invalid character error for encryption (using a Chinese letter)
    def test_invalid_character_encryption(self):
        # Using a Chinese character not included in the dictionary
        invalid_char = '你'  # Replace this with any Chinese character not in the dictionary
        english_text = f"HELLO{invalid_char}"
        with self.assertRaises(ValueError) as context:
            text_to_morse(english_text)
        self.assertEqual(str(context.exception), "Please Enter a Valid Letter")
        
    # Test case 6: Invalid Morse code sequence error for decryption (using an invalid Morse code sequence)
    def test_invalid_morse_sequence_decryption(self):
        # Using an invalid Morse code sequence
        invalid_morse = ".--.-.---.-.--"  # Replace this with any invalid Morse code sequence
        with self.assertRaises(ValueError) as context:
            morse_to_text(invalid_morse)
        self.assertEqual(str(context.exception), "Please Enter a Valid Letter")
        
