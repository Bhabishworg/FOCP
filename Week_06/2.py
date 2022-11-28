def giveFactor(n):
    """Returns the factors of the integer."""
    factors = [i for i in range(1, n+1) if n % i == 0]
    return factors

num = int(input("Enter a number: "))

print(f"Factors of {num} : {giveFactor(num)}")
