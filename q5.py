#Write a function that takes an integer as parameter and returns a list of all thedivisors of that number:ex: 47 -> [1,47], 28 -> [1,2,4,7,14,28]

def get_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Call the function
n = int(input("Write a number: "))
divisors = get_divisors(n)
print("The divisors of", n, "are:", divisors)

