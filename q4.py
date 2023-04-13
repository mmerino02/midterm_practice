#Write a function that takes the name of a text file as parameter. Print out the 3-letter words that start with “b”
def print_b_words(filename):
    with open(filename, 'r') as file:
        text = file.read()  # read the contents of the file as a string
        words = text.split() # split the text into words
        # loop through the words and print those that start with "b" and have length 3
        for word in words:
            if len(word) == 3 and word[0] == "b":
                print(word)
