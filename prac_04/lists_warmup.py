"""Warm-up activities revising list indexing and manipulation."""

numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] should produce 3
# numbers[-1] should produce 2
# numbers[3] should produce 1
# numbers[:-1] should produce [3, 1, 4, 1, 5, 9]
# numbers[3:4] should produce [1]
# 5 in numbers should produce True
# 7 in numbers should produce False
# "3" in numbers should produce False
# numbers + [6, 5, 3] should produce [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)
