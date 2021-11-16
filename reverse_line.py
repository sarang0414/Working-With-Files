f = open('file1.txt')
data = f.readlines()
for i in data:
    for j in reversed(i):
        print(j,end='')
f.close()