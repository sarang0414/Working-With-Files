f = open('file1.txt')
data = f.readlines()
for dt in reversed(data):
    print(dt)
f.close()