# a --- list here
a = [10,20,15,45,25,36,90,58,96,87,36]
x = bytes(a)
print(x[0])
print(x[1])
print(x[2])
print(x[3])
# x[0]=11
# print(x[0])
# TypeError: 'bytes' object does not support item assignment
print("------------------")
for i in x:    
    print(i)
# in java for loop is like the following
# for(int i=0; i<5; i++)
# {
#     System.out.println(x[i]);
# }