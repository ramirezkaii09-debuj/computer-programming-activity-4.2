# Activity 1: Times Table
# Read a number and print its multiplication table from 1 to 10.

n = int(input("Number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
