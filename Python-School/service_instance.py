input_string = input("Enter a list element separated by space ")
list  = input_string.split()
print(list)

print("!")

for p in list:
    print("service instance " + p + " ethernet")
    print("encapsulation dot1q " + p)
    print("bridge-domain " + p)
    print("!")
