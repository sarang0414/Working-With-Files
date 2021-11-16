f = open('file1.txt')
data = f.readlines()
for i in data:
    print(i.center(100))
f.close()