def head(data):
    for lines in data[0:10:1]:
        print(lines)
def tail(data):
    new_data = data[::-1]
    for line in new_data[0:10:1]:
        print(line)
f = open('file2.txt')
data = f.readlines()

#head(data)
tail(data)

f.close()