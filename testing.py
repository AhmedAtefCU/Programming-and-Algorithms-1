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

        
