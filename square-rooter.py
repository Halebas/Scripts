def solve_quadratic_equation(a: int, b: int, c: int, is_silent=False):
    D = b**2 - 4 * a * c

    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)

    if not is_silent:
        print(f"\n{a}x^2 + {b}x + {c} = 0")
        print(f"{D = }")

        if D == 0:
            print(f"x = {x1}")
        elif D > 0:
            print(f"{x1 = }\n{x2 = }")
        else:
            print("No real roots...")
            print(f"Complex roots:\n{x1 = :.5f}\n{x2 = :.5f}")

    return (x1, x2)


if __name__ == "__main__":
    a, b, c = map(int, input("Enter a, b and c: ").split())
    print(solve_quadratic_equation(a, b, c))
