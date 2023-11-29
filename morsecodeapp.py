# Morse code dictionary containing mappings for letters, numbers, and symbols
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '
}

# List to store translation history
history = []

# Function to display the menu options
def display_menu():
    print("Menu:")
    print("1. Enter a Text to Translate from English to Morse Code")
    print("2. Enter a Text to Translate from Morse Code to English")
    print("3. Display Translation History")
    print("4. Exit")
    
# Function to convert text to Morse code
def text_to_morse(text):
    # Handling empty input error for encryption
    if text.strip() == '':
        raise ValueError("Cannot Encrypt Empty Space")
    
    morse_code = ""
    for char in text.upper():
        # Converts each character of the text to its Morse code representation
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        elif char == ' ':
            # For spaces, adds a space to maintain the distinction between words
            morse_code += " "
        else:
            # If an invalid character is encountered, prompts the user to enter a valid letter
            return "Please Enter a Valid Letter"
    return morse_code.strip()