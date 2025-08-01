def trivial_division(n):
    factors = []
    divisor = 2 

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

composite_number = int(input("Enter the Number: "))
result = trivial_division(composite_number)
if len(result) > 0:
    print(f"Factors found: {result}")
else:
    print("The number is prime.")
