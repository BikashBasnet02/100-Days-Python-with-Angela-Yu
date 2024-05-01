import string

lowercase_alphabets = list(string.ascii_lowercase)
uppercase_alphabets = list(string.ascii_uppercase)

def get_shifted_index(index, shift):
    return (index + shift) % 26

def caesar_cipher(text, shift, direction):
    result = ""
    for letter in text:
        if letter.isalpha():
            alphabets = lowercase_alphabets if letter.islower() else uppercase_alphabets
            index = alphabets.index(letter)
            new_index = get_shifted_index(index, shift if direction == "encode" else -shift)
            result += alphabets[new_index]
        else:
            result += letter
    return result

def main():

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if 0 <= shift < 26:
        result = caesar_cipher(text, shift, direction)
        print(f"The {'encoded' if direction == 'encode' else 'decoded'} text is: {result}")
    else:
        print("Invalid shift number. Shift must be between 0 and 25.")

if __name__ == "__main__":
    main()
    
restart = input("type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
if restart == "yes":
    main()
else:
    print("Goodbye!")

