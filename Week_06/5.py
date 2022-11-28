from random import randint, choice

def encrypt(msg):
    """Encrypts the message.
    Encryption type: fill message with random letters with a random interval."""

    interval = randint(2, 20)
    encryptedMsg = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in msg:
        encryptedMsg += i
        if i == msg[-1]:
            break
        for j in range(interval):
            encryptedMsg += choice(alphabet)

    return encryptedMsg, interval

message = input("Enter a message: ")
result = encrypt(message)
print("Encrypted message:", result[0], "\nInterval used:", result[1])