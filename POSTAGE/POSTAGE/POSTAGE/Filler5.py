# import required libraries
import random
import string

# function to generate random strings
def random_string_generator(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# list to store generated strings
generated_strings = []

# generate 100 random strings and store them in the list
for i in range(100):
    generated_strings.append(random_string_generator())

# print the generated strings
for i in range(100):
    print(f"Generated string {i+1}: {generated_strings[i]}")

# function to count the number of vowels in a string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# list to store the number of vowels in each generated string
vowel_counts = []

# count the number of vowels in each generated string and store the results in the list
for i in range(100):
    vowel_counts.append(count_vowels(generated_strings[i]))

# print the number of vowels in each generated string
for i in range(100):
    print(f"Generated string {i+1} has {vowel_counts[i]} vowels.")

# function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# list to store prime numbers
prime_numbers = []

# find all prime numbers between 1 and 100 and store them in the list
for i in range(1, 101):
    if is_prime(i):
        prime_numbers.append(i)

# print the prime numbers
print("Prime numbers between 1 and 100:")
print(prime_numbers)

# function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# list to store the factorials of the prime numbers
factorials = []

# calculate the factorials of the prime numbers and store the results in the list
for i in range(len(prime_numbers)):
    factorials.append(factorial(prime_numbers[i]))

# print the factorials of the prime numbers
print("Factorials of the prime numbers between 1 and 100:")
print(factorials)

# function to generate random numbers
def random_number_generator(minimum=1, maximum=100):
    return random.randint(minimum, maximum)

# list to store the generated random numbers
random_numbers = []

# generate 100 random numbers and store them in the list
for i in range(100):
    random_numbers.append(random_number_generator())
