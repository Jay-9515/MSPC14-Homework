# -------------------------------
#  Setup data
# -------------------------------
fruits  = ['mango', 'kiwi', 'strawberry',
           'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

vowels = set('aeiou')        # handy for vowel counting


# -------------------------------------------------
#  FRUIT‑BASED EXERCISES
# -------------------------------------------------

# 1) upper‑cased fruit names
uppercased_fruits = [fruit.upper() for fruit in fruits]

# 2) capitalized fruit names (first letter upper‑case only)
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

# 3) fruits with **more than two** vowels
def count_vowels(word):
    return sum(1 for ch in word if ch in vowels)

fruits_with_more_than_two_vowels = [
    fruit for fruit in fruits if count_vowels(fruit) > 2
]

# 4) fruits with **exactly two** vowels
fruits_with_only_two_vowels = [
    fruit for fruit in fruits if count_vowels(fruit) == 2
]

# 5) fruits with more than 5 characters
fruits_more_than_five_chars = [fruit for fruit in fruits if len(fruit) > 5]

# 6) fruits with exactly 5 characters
fruits_with_five_chars = [fruit for fruit in fruits if len(fruit) == 5]

# 7) fruits with fewer than 5 characters
fruits_with_less_than_five_chars = [fruit for fruit in fruits if len(fruit) < 5]

# 8) list of the **lengths** of each fruit
fruit_name_lengths = [len(fruit) for fruit in fruits]

# 9) fruits containing the letter “a”
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit.lower()]


# -------------------------------------------------
#  NUMBER‑BASED EXERCISES
# -------------------------------------------------

# 10) even numbers
even_numbers = [n for n in numbers if n % 2 == 0]

# 11) odd numbers
odd_numbers = [n for n in numbers if n % 2 != 0]

# 12) positive numbers
positive_numbers = [n for n in numbers if n > 0]

# 13) negative numbers
negative_numbers = [n for n in numbers if n < 0]

# 14) numbers with **two or more numerals**
#     (absolute value 10 or greater)
numbers_with_two_or_more_digits = [n for n in numbers if abs(n) >= 10]

# 15) numbers squared
numbers_squared = [n**2 for n in numbers]

# 16) numbers plus five
numbers_plus_five = [n + 5 for n in numbers]

# 17) prime numbers (simple check)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [n for n in numbers if is_prime(n)]


# -------------------------------------------------
#  Quick print‑out so you can see the results
# -------------------------------------------------
if __name__ == "__main__":
    print("1  uppercased_fruits =", uppercased_fruits)
    print("2  capitalized_fruits =", capitalized_fruits)
    print("3  >2 vowels          =", fruits_with_more_than_two_vowels)
    print("4  =2 vowels          =", fruits_with_only_two_vowels)
    print("5  >5 chars           =", fruits_more_than_five_chars)
    print("6  =5 chars           =", fruits_with_five_chars)
    print("7  <5 chars           =", fruits_with_less_than_five_chars)
    print("8  name lengths       =", fruit_name_lengths)
    print("9  letter 'a'         =", fruits_with_letter_a)
    print("10 even_numbers       =", even_numbers)
    print("11 odd_numbers        =", odd_numbers)
    print("12 positive_numbers   =", positive_numbers)
    print("13 negative_numbers   =", negative_numbers)
    print("14 ≥2 digits          =", numbers_with_two_or_more_digits)
    print("15 numbers_squared    =", numbers_squared)
    print("16 numbers_plus_five  =", numbers_plus_five)
    print("17 prime_numbers      =", prime_numbers)
