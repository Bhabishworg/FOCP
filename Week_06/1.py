def intoBinary(num):
    """Calculates and returns its respective binary number."""

    remainder = []
    while True:
        remainder.append(str(num % 2))
        num //= 2
        if num == 0:
            break
    remainder.reverse()
    binaryNum = "".join(remainder)

    return binaryNum

while True:
    n = int(input("Enter a positive number: "))
    if n > 0:
        break

print(f"{n} in binary is {intoBinary(n)}")
