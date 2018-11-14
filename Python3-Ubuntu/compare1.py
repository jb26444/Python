import os
import filecmp



os.system("tree > out1.txt")


p=filecmp.cmp('/home/jan/Desktop/Python3-Ubuntu/out.txt', '/home/jan/Desktop/Python3-Ubuntu/out1.txt')

print(p)



