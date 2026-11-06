# Activity 2: Class Scores
# Read student scores, then display the total, average, and highest score.

students = int(input("Students: "))

total = 0
highest = None

for i in range(1, students + 1):
    score = float(input(f"Score {i}: "))
    total += score

    if highest is None or score > highest:
        highest = score

if students > 0:
    average = total / students
else:
    average = 0

print(f"Total: {total:.0f}   Avg: {average:.2f}")

if highest is not None:
    print(f"Highest: {highest:g}")
else:
    print("Highest: N/A")
