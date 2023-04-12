a = 2
b = 3
c = "abc"
print(a, b, c)
print(a, b, c, sep=",")
a += 2
a == 5 #False as a = 4 not 5
print(a)
print(c*(a-b))
d = c.find("b") #1 as there is only one b
print(d)
print(d and b) #3 as both are true we take the value of the first, in this case b
print(d == True) #True non-zero
e = str(a) + str(b) + str(c) + str(d)
print(e) #43abc1
print(e[1::2]) #3b1
print(e+e[::1]) #43abc143abc1


