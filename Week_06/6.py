def decrypt(encryptedMsg, interval):
    """Decrypts the message.
    Encryption type: fill message with random letters with a random interval."""

    decryptedMsg = ""
    for i in range(0, len(encryptedMsg), interval + 1):
        decryptedMsg += encryptedMsg[i]
    
    return decryptedMsg

msg = input("Enter the encrypted message: ")
intrvl = int(input("Enter the interval: "))

print("Decrypted Message:", decrypt(msg, intrvl))