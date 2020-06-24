a = [10,20,15,45,25,36,90,58,96,87,36]
x = bytearray(a)
print(x[0])
print(x[4])
print(x[7])
x[0] = 23
x[4] = 23
x[7] = 23
print("--------------------")
print(x[0])
print(x[4])
print(x[7])
print("--------------------")
for i in x:
    print(i)