def TestPass():
    pass


TestPass()


def Add(a, b):
    return a+b


print("Add:" + str(Add(1, 2)))


def AddList(list):
    result = 0
    for item in list:
        result += item
    return result


list = [1, 2, 3]
print("AddList:" + str(AddList(list)))


def AddParams(*args):
    result = 0
    for item in list:
        result += item
    return result


print(AddParams(1))
print(AddParams(1, 2))
print(AddParams(1, 2, 3))


def KeywordAdd(a, b):
    print("KeywordParamsAdd: %s+%s=%s" % (a, b, a+b))


KeywordAdd(a=1, b=2)
KeywordAdd(b=1, a=2)


def KeywordParamsAdd(**kwargs):
    for key, value in kwargs.items():
        print("%s => %r" % (key, value))


KeywordParamsAdd(Test1="Hello", Test2="Hello2")


def TestPrint(a, b, format):
    result = a+b
    print(format(a, b, result))


TestPrint(1, 2, lambda a, b, c: "%s+%s=%s" % (a, b, c))
