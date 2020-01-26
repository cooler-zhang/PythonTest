x = 10


def test():
    x = 20
    print(x)


print(x)
test()


def main():
    x = 5
    print(x)

    def sub():
        x = 15
        print(x)
    sub()


main()


def gobalTest():
    global go 
    go = "a"
    print(go)

gobalTest()

print(go)
