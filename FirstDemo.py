
def test():
    print("Hello World!")


def test2(name):
    print("Hello " + name)


def test3(a, b):
    return a+b


a, b = 1, 2
print("%d+%d=%d" % (a, b, test3(a, b)))

for index in range(1, 5):
    print(index)

list = ["orange", "apple", "pear"]

for item in list:
    if item == "apple":
        print("red "+item)
    else:
        print(item)

"""
For While
"""
i = 0
length = 10
while i < length:
    i = i+2
    print(i)

'''
For string
'''
string = " HeLLo world & go"

print("{}-{}".format("Cooler", "Zhang"))
print(string.lower())
print(string.upper())
print(len(string))
print(string.strip())
print(string.split("&"))
