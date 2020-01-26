import json

try:
    print(x)
except NameError as e:
    print(str(e))
else:
    print("Unknow error")
finally:
    print("Try Catch Finally")


def Dev(x, y):
    if y == 0:
        raise Exception("y is zero")
    return x/y


print(Dev(2, 1))

try:
    Dev(2, 0)
except Exception as ex:
    print(str(ex))
