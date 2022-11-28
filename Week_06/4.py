def encrypt(msg):
    """Encrypts the message.
    Encryption type: removing space and reversing the string."""

    characters = [character for character in msg if character != " "]
    characters.reverse()
    encryptedMsg = "".join(characters)
    
    return encryptedMsg

message = input("Enter a message: ")
print(encrypt(message))