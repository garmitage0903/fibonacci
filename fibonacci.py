import csv

def fibonacci(n):
    """Return a list of the first n Fibonacci numbers."""
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# How many Fibonacci numbers to generate
N = 50  # change this if you want more/less

# Generate the sequence
fib_numbers = fibonacci(N)

# Write to CSV
with open("fibonacci.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["index", "value"])  # header
    for i, value in enumerate(fib_numbers):
        writer.writerow([i, value])

print("fibonacci.csv created!")
