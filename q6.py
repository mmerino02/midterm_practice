# Write a function that forces the user to enter a multiple of 6 number. Use try,except to catch invalid inputs. Return that number

def get_multiple_of_6():
    while True:
        try:
            num = int(input("Please enter a multiple of 6: "))
            if num % 6 != 0:
                raise ValueError("Number is not a multiple of 6")
            return num
        except ValueError:
            print("Invalid input. Please enter a multiple of 6.")

num = get_multiple_of_6()
print("The multiple of 6 you entered is:", num)

