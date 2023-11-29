# Test case creation library
import unittest

# Library for mocking
from unittest.mock import patch

# Library for capturing output
from io import StringIO

# Import the functions and dictionary from the Morse code translator script
from morsecodeapp import text_to_morse, morse_to_text, morse_code_dict, history, display_history