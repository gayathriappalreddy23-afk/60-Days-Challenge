fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#2
items = ["Task 1", "Task 2", "Task 3"]

for index, item in enumerate(items):
    print(f"Index {index}: {item}")

#3
prices = {"apple": 50, "banana": 20, "cherry": 80}

for item, price in prices.items():
    print(f"The price of {item} is {price} rupees.")

#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)  # Output: [2, 4, 6, 8]

#5
duplicate_words = ["apple", "banana", "apple", "cherry", "banana"]
unique_words = set(duplicate_words)

for word in unique_words:
    print(word)  # Prints apple, banana, cherry (order may vary)

#6

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score} points.")
