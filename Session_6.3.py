#7.	Read an int number. Check if the number is a palindrome. (A palindrome number read backwards has the same value.Example of palindrome numbers: 123454321, 999, 15989

def is_palindrome(num):
    num_str = str(num) # Convert the integer to a string
    return num_str == num_str[::-1] # Check if the string is the same backwards and forwards

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
