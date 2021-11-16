import textwrap
f = open('file3.txt')
data = f.read()
info = str(data)
print(info)
wrapper = textwrap.TextWrapper(width=40)
result = wrapper.fill(text=info)
print(result)
f.close()