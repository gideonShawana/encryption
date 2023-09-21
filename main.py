import pyperclip

def caesar_cipher(message, key, mode):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            if mode == 1:  # Change 'encrypt' to 1
                translatedIndex = (symbolIndex + key) % len(SYMBOLS)
            elif mode == 2:  # Change 'decrypt' to 2
                translatedIndex = (symbolIndex - key) % len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    return translated

def main():
    while True:
        message = input("Enter the message: ")
        key = int(input("Enter the key: "))
        mode = int(input("1 for encryption or 2 for decryption: "))  # Input 1 or 2

        if mode not in [1, 2]:  # Check for 1 or 2
            print("Invalid mode. Please enter 1 for encryption or 2 for decryption.")
            continue  # Restart the loop to get valid input

        result = caesar_cipher(message, key, mode)

        print("Result:")
        print(result)
        pyperclip.copy(result)
        print("Result has been copied to the clipboard.")

        another_op = input("Perform another operation? (yes/no): ").lower()
        if another_op != 'yes':
            break  # Exit the loop if the user doesn't want to perform another operation

if __name__ == "__main__":
    main()