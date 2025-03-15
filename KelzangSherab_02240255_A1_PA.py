import math

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if prime(num):
            total_sum += num
    return total_sum

def length_converter(value, direction):
    if direction == 'M':
        return round(value * 3.28084, 2)
    elif direction == 'F':

        return round(value / 3.28084, 2)
    else:
        raise ValueError("Invalid direction! Use 'M' for meters to feet, 'F' for feet to meters.")

def consonant_count(text):
    consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in text:
        if char in consonant:
            count += 1
    return count

def min_max(numbers):

    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

def is_palindrome(text):

    text = text.replace(" ", "").lower()
    return text == text[::-1]

def word_counter(path):
    target_words = ["the", "was", "and"]
    word_count = {word: 0 for word in target_words}
    
    try:
        with open(path, 'r') as file:
            text = file.read().lower()
            for word in target_words:
                word_count[word] = text.split().count(word)
    except FileNotFoundError:
        return "File not found. Please check the file path."
    
    return word_count

def display():
    print("Select an option:")
    print("1. calculate the sum of prime numbers")
    print("2. convert length units")
    print("3. count consonants in string")
    print("4. find Min and Max numbers")
    print("5. check for pelindrone")
    print("6. Word counter")
    print("7. Exit")

def main():
    while True:
        display()
        try:
            choice = int(input("Enter your choice (1-7): "))
            if choice == 1:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                print(f"Sum of prime numbers in range {start} to {end}: {prime_sum(start, end)}")
            elif choice == 2:
                value = float(input("Enter the length value: "))
                direction = input("Enter direction ('M' for meters to feet, 'F' for feet to meters): ").upper()
                print(f"Converted value: {length_converter(value, direction)}")
            elif choice == 3:
                text = input("Enter the text string: ")
                print(f"Number of consonants: {consonant_count(text)}")
            elif choice == 4:
                numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
                smallest, largest = min_max(numbers)
                print(f"Smallest: {smallest}, Largest: {largest}")
            elif choice == 5:
                text = input("Enter the text string: ")
                print(f"Is palindrome: {is_palindrome(text)}")
            elif choice == 6:
                path = input("Enter the file path: ")
                print(word_counter(path))
            elif choice == 7:
                print("I am exiting the program.")
                break
            else:
                print("Invalid choice. Please select a number (1-7).")
        except ValueError as e:
            print(f"Invalid input: {e}")
        
        continue_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if continue_choice != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()