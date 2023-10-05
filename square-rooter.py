a, b, c = map(int, input("Enter a, b and c: ").split())
print(f"\n{a}x^2 + {b}x + {c} = 0")

D = b**2 - 4 * a * c
print(f"{D = }")

x1 = (-b + D**0.5) / (2 * a)
x2 = (-b - D**0.5) / (2 * a)

if D == 0:
    print(f"x = {x1}")
elif D > 0:
    print(f"{x1 = }\n{x2 = }")
else:
    print("No real roots...")
    print(f"Complex roots:\n{x1 = :.5f}\n{x2 = :.5f}")
