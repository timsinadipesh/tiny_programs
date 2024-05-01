# prints pascal's triangle for the given height

def print_pascal_triangle(height):
    for i in range(height):
        space = " " * (height - (i + 1))
        print(space, end="")
        val = 1
        for j in range(i + 1):
            print(val, end=" ")
            val = val * (i - j) // (j + 1) # binomial coefficient
        print()

print_pascal_triangle(10)