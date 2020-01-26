import re

txt = "Hello World!"
result = re.search("^Hello.*World$", txt)
print(result is None)


findResult = re.findall("\\w", txt)
print(findResult)


splitResult = re.split("\\s", txt)
print(splitResult)

subResult = re.sub("\\s", "-", txt)
print(subResult)
