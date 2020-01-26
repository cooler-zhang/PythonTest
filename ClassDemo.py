from abc import abstractmethod

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def Output(self):
        print("姓名：{}, 年龄: {}".format(self.name, str(self.age)))

    def Work(self):
        print("Do work")
    
    @abstractmethod
    def Test(self):
        pass


class Student(Person):

    def __init__(self, age, name, className):
        super().__init__(age, name)
        self.className = className

    def Output(self):
        print("姓名：{}, 年龄: {}, 班级：{}".format(
            self.name, str(self.age), self.className))

    def Test(self):
        print("Test")


student = Student('Cooler', 33, "一班")
student.Output()
student.Test()
student.Work()
