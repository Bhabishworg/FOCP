def checkPrime(n):
    """Determines if the integer is prime."""
    if n <= 1:
        print(f"{n} is not a prime number")
    else:
        factors = [i for i in range(1, n+1) if n % i == 0]
        print(f"{n} is a prime number" if len(factors) == 2 else f"{n} is not a prime number")

num = int(input("Enter a number: "))

checkPrime(num)