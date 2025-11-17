# Using statistics module

import statistics

number = [6, 8, 80, 55, 70, 22, 55, 11, 11, 199, -5]

mean2 = statistics.mean(number)

print("Mean:", mean2)

median = sorted(number)[len(number) // 2]
print("Median:", median)

mode2 = statistics.mode(number)
print("Mode:", mode2)

print("Maximum:", max(number))
print("Minimum:", min(number))

