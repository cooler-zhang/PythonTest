import json
import datetime
import platform
import ClassDemo as CD

student = CD.Student(10, "Cooler", "二班")

print(student.Output())


print(platform.system())
print(platform.version())


print(datetime.datetime.now())

testJsonStr = '{"Name":"张三","Age":10}'
testJson = json.loads(testJsonStr)
print(testJson["Name"])


properties = {"Name": "张三", "Age": 10, "Desciption": "好学生"}
testProperties = json.dumps(properties)
print(testProperties)
