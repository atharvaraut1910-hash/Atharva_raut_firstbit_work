##Write a program to input any alphabet and check whether it is vowel or consonant.

ch = input("Enter any alphabet: ")

# Convert to lowercase to handle both upper and lowercase

if ch.isalpha() and len(ch) == 1:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("It is a vowel.")
    else:
        print("It is a consonant.")
else:
    print("Invalid input! Please enter a single alphabet.")
