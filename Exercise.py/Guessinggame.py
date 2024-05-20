def find_first_repeating_character(s):
    # Create an empty dictionary to store character counts
    char_count = {}
    
    # Iterate through each character in the string
    for char in s:
        # Check if the character is already encountered
        if char in char_count:
            # If the character is repeating, print its details and return it
            print(f"First repeating character: {char}, Memory address: {id(char)}")
            return char, id(char)
        
        # If the character is encountered for the first time, add it to the dictionary
        char_count[char] = 1
    
    # If no repeating character is found, return None
    return None

# Example usage:
input_string = "hello"
result = find_first_repeating_character(input_string)

# Check if a repeating character is found
if result is None:
    print("No repeating character found in the string.")
