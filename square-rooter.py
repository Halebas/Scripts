a, b, c = map(int, input("Enter a, b and c: ").split())

D = b**2 - 4 * a * c

if D == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
elif D > 0:
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    print(f"x1 = {x1}\nx2 = {x2}")
else:
    print("No real roots...")
