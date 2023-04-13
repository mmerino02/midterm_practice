#Suppose you can only do additions. Write a program that reads two positive, integer numbers a and b. It computesa**b.

a = int(input("Write a positive integer (base): "))
b = int(input("Write another positive integer (exponent): "))

def power (a, b):
    result = 1
    for i in range(b):
        temp = 0
        for j in range(a):
            temp += result
        result = temp
    return result
print("Your answer is:", power(a, b))

