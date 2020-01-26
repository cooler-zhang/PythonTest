import os

fileName = "1.txt"

result = open(fileName, "w")
result.write("abc")
result.close()

result = open(fileName, "r")
print(result.read())
result.close()

result = open(fileName, "a")
result.write("123")
result.close()

result = open(fileName, "r")
print(result.read())
result.close()

os.remove(fileName)
