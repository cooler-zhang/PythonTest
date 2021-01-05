'''
List
'''
print("--------------------------Fruits:---------------------------")
fruits = ["Apple", "Orange", "Banana"]
popItem = fruits.pop(0)
print(popItem)
fruits.remove("Banana")
fruits.append("WaterMelon")
for fruit in fruits:
    print(fruit)
print("Banana" in fruits)

'''
Tuple
'''
print("---------------------------Animals:---------------------------")
animals = ("Cat", "Dog")
for animal in animals:
    print(animal)

'''
Set
'''
print("---------------------------Menu:---------------------------")
menu = {"番茄炒蛋", "水煮肉片", "水煮牛肉", "水煮肉片"}
print(len(menu))
for item in menu:
    print(item)


'''
Dictionary
'''
print("---------------------------Properties:---------------------------")
properties = {"Name": "张三", "Age": 10, "Desciption": "好学生"}
print(properties)
print("Name in properties:{}".format(str("Name" in properties)))
print("Sex in properties:{}".format(str("Sex" in properties)))
properties["Sex"] = "男"
for item in properties:
    print("{} => {}".format(item, properties[item]))

print(properties.pop("Desciption"))
del properties["Sex"]

for key, value in properties.items():
    print("{}:{}".format(key, value))


listIter = iter(fruits)
print(next(listIter))
print(next(listIter))