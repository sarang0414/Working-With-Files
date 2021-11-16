f = open('file1.txt')
data = f.readlines()
str = "Lorem"
for i in data:
    if str in i:
        print(i)

f.close()