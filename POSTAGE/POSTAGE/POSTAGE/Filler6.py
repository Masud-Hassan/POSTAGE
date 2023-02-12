import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_numbers(start, end, num):
    return [random.randint(start, end) for i in range(num)]

def generate_random_list(length, start, end):
    return [random.randint(start, end) for i in range(length)]

def shuffle_list(numbers):
    random.shuffle(numbers)
    return numbers

def main():
    str_length = int(input("Enter the length of the string: "))
    print("Random string:", generate_random_string(str_length))
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    num = int(input("Enter the number of random numbers: "))
    print("Random numbers:", generate_random_numbers(start, end, num))
    length = int(input("Enter the length of the list: "))
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    numbers = generate_random_list(length, start, end)
    print("Random list:", numbers)
    print("Shuffled list:", shuffle_list(numbers))