import re
import webbrowser

l1 = []
with open("Data.txt") as file:
    for line in file:
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        l1.append(urls)

flatten_matrix = []
for sublist in l1:
    for val in sublist:
        flatten_matrix.append(val)

print(flatten_matrix)


for i in flatten_matrix:
   webbrowser.open(i)
