random_numbers = [12, 45, 7, 89, 23, 56, 34, 78, 91, 5,
67, 38, 49, 72, 16, 84, 29, 53, 61, 10,
95, 27, 41, 68, 3, 77, 50, 32, 88, 14, 80]

mean = sum(random_numbers) / len(random_numbers)

sorted_numbers = sorted(random_numbers)
n = len(sorted_numbers)
if n % 2 == 0:
    median = (sorted_numbers[n//2 -1] + sorted_numbers[n//2 + 1]) / 2
else:
    median = sorted_numbers[n//2]

variance = (sum((x-mean) ** 2 for x in random_numbers) / (len(random_numbers) - 1))
standard_deviation = variance ** 0.5