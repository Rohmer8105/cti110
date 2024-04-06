def print_increments(start, end):
    if end < start:
        print("Second integer can't be less than the first.", end="")
    else:
        while start <= end:
            print(start, end=" ")
            start += 5

num1 = int(input())
num2 = int(input())

print_increments(num1, num2)
print()  # Print newline after the loop
