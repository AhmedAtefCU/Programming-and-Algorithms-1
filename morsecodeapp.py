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
            raise ValueError("Please Enter a Valid Letter")
    return morse_code.strip()

# Function to convert Morse code to text
def morse_to_text(morse_code):
    # Handling empty input error for decryption
    if morse_code.strip() == '':
        raise ValueError("Cannot Decrypt Empty Space")
    
    # Conversion of Morse code to English text
    text = ""
    morse_code = morse_code.split(" ")
    for code in morse_code:
        if code == '':
            # Adds a space for spaces in Morse code
            text += ' '
        else:
            # Converts Morse code to respective characters of the English alphabet
            for key, value in morse_code_dict.items():
                if code == value:
                    text += key
                    break
            else:
                # If an invalid Morse code sequence is encountered, prompts the user to enter a valid letter
                raise ValueError("Please Enter a Valid Letter")

    # Capitalizing the first letter of each word in the decrypted text
    words = text.split(" ")
    decrypted_text = " ".join(word.capitalize() for word in words)
    return decrypted_text

# Function to display translation history
def display_history():
    # Checking and displaying the translation history
    if not history:
        print("Translation History is Empty")
    else:
        print("Translation History:")
        for entry in history:
            # Prints the translation history including English text and corresponding Morse code
            print(f"English: {entry.get('English', '')}, Morse Code: {entry.get('Morse Code', '')}")

# Main program logic
def main():
    global history

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            # User input for text to be converted to Morse code
            english_text = input("Enter the English text: ")
            try:
                # Tries to convert the entered text to Morse code and handles empty space error
                translated_text = text_to_morse(english_text)
                print("Translated Morse Code:", translated_text)
                history.append({"English": english_text, "Morse Code": translated_text})
            except ValueError as e:
                # Prints an error message if empty space is attempted for encryption
                print("Error:", e)
                
        elif choice == "2":
            # User input for Morse code to be converted to English text
            morse_code_text = input("Enter the Morse code: ")
            try:
                # Tries to convert the entered Morse code to English text and handles empty space error
                translated_text = morse_to_text(morse_code_text)
                print("Translated English Text:", translated_text)
                history.append({"Morse Code": morse_code_text, "English": translated_text})
            except ValueError as e:
                # Prints an error message if empty space is attempted for decryption
                print("Error:", e)
                
        elif choice == "3":
            # Displays the translation history
            display_history()
            
        elif choice == "4":
            # Exits the program
            print("Exiting the Program.")
            break

        else:
            # Handles invalid user input
            print("Invalid choice. Please enter a valid option.")
            
        print()
        
# Run the main program
if __name__ == '__main__':
    main()
