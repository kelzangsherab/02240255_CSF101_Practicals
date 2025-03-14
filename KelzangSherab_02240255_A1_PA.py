import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(start, end):
    """Calculate the sum of prime numbers within a given range."""
    total_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total_sum += num
    return total_sum

def length_converter(value, direction):
    """Convert length between meters and feet."""
    if direction == 'M':
        # Convert meters to feet
        return round(value * 3.28084, 2)
    elif direction == 'F':
        # Convert feet to meters
        return round(value / 3.28084, 2)
    else:
        raise ValueError("Invalid direction! Use 'M' for meters to feet, 'F' for feet to meters.")

def consonant_count(text):
    """Count the number of consonants in a string."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in text:
        if char in consonants:
            count += 1
    return count

def min_max(numbers):
    """Find the smallest and largest number in a list."""
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

def is_palindrome(text):
    """Check if a text is a palindrome."""
    text = text.replace(" ", "").lower()
    return text == text[::-1]

def word_counter(file_path):
    """Count the occurrences of specific words in a text file."""
    target_words = ["the", "was", "and"]
    word_count = {word: 0 for word in target_words}
    
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
            for word in target_words:
                word_count[word] = text.split().count(word)
    except FileNotFoundError:
        return "File not found. Please check the file path."
    
    return word_count

def display_menu():
    """Display the main menu."""
    print("Select an option:")
    print("1. calculate the sum of prime numbers")
    print("2. convert length units")
    print("3. count consonants in string")
    print("4. find Min and Max numbers")
    print("5. check for pelindrone")
    print("6. Word counter")
    print("7. Exit")

def main():
    """Main function to run the program."""
    while True:
        display_menu()
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
                file_path = input("Enter the file path: ")
                print(word_counter(file_path))
            elif choice == 7:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        
        continue_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if continue_choice != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()