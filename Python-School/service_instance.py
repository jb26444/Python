
input_string = input("Enter a list of service instances separated by space ")
list  = input_string.split()
print(list)


control = input("Is the list above correct? Y/N: ")


if control == "Y":
  print("!")
  for p in list:
    print("service instance " + p + " ethernet")
    print("encapsulation dot1q " + p)
    print("bridge-domain " + p)
    print("!")
elif control == "y":
  print("!")
  for p in list:
    print("service instance " + p + " ethernet")
    print("encapsulation dot1q " + p)
    print("bridge-domain " + p)
    print("!")
else:
    print("Start again then :)")
