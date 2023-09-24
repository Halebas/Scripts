x, y = map(int, input("Enter two integers: ").split())

operators = ["~", "&", "|", "^", ">>", "<<"]
print(f"operators: {operators}\n")

for operator in operators:
    res = ~x if operator == "~" else eval(f"{x} {operator} {y}")
    width = max(len(str(num)) for num in [x, y, res])
    bin_width = max(len(f"{num:b}") for num in [x, y, res])

    print(f" x = {x:>{width}} {x:>{bin_width}b}")

    if operator != "~":
        print(f" y = {y:>{width}} {y:>{bin_width}b}")

    print(f"{operator:>2} = {res:>{width}} {res:>{bin_width}b}\n")
