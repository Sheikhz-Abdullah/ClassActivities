#1 Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange", "Grape"]
print(fruits)


#2 Accessing Elements
colors = ['red', 'blue', 'green', 'yellow', 'purple']

first_color = colors[0]
third_color = colors[2]
last_color = colors[-1]
print(first_color, third_color, last_color)


#3 Modifying a list
digits = [10,20,30,40,50]

digits[1] = 25
digits.append(60)
print(digits)


#4 List Slicing
names = ['ALice', 'Bob', 'Charlie', 'David', 'Emma']

subset = names[:3]
print(subset)


#5 Looping through a list
numbers = list(range(1, 11))

for number in numbers:
    print(number ** 2)


#6 Appedn & Extend
shopping_cart = []

shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)


#7 Maximum & Minimum
nums = [45,22,88,56,92,33]

max_value = max(nums)
min_value = min(nums)
print('Maximum Value:', max_value)
print('Minimum Value:', min_value)


#8 Counting Occurrences
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']

count_a = letters.count('a')
print("The letter 'a' appear", count_a, "times.")


#9 List Comprehension
squares_of_evens = []

for x in range(11):
    if x % 2 == 0:
        squares_of_evens.append(x * x)
print(squares_of_evens)


#10 Removing Duplicates
numericals = [1,2,2,3,4,4,5,6,6,7]

unique_numericals = set(numericals)
print(unique_numericals)