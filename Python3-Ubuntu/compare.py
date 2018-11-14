import difflib
import os



os.system("tree > out1.txt")

with open('out.txt') as f1:
    f1_text = f1.read()
with open('out1.txt') as f2:
    f2_text = f2.read()
# Find and print the diff:
for line in difflib.unified_diff(f1_text, f2_text, fromfile='out.txt', tofile='out1.txt',lineterm=''):
    print(line)
