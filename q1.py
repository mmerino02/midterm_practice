print(type(2+3))
#int (5)
print(type(6/2))
#float (3.0)
print(type(2!=3))
#bool (true)
print(type(5 or 6))
#int (5 or 6)
print(type(5 and 7))
#int (7)
print(type(2*2))
#int (4)
print(type("abc".find))
#Function
print(type("bubu"*2))
#string ("bubububu")
print(type("bubu"*(4/2)))
#string ("bubububu")
print(type("abc", 2))
#tuple as it is a ordered collection of elements in parenthesis
print(type({2:1, "John":"Mary"}))
#dictionary *We haven't seen it*
print(type(2))
#int (2) -> if it only has one value it's not a tuple. For it to be one it must be (2, )