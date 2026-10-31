def find_gcd(a, b):
    while b != 0:
        remainder = a % b
        print(f"{a} = {a//b} * {b} + {remainder}")
        a = b
        b = remainder
    return a

print(f"GCD is {find_gcd(120, 25)}")
print(f"GCD is {find_gcd(45, 30)}")