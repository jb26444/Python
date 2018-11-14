import pandas as pd
data = pd.read_csv('IP.csv', header=None)
list_lines = data.read().splitlines()
print list_lines


