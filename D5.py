'''
class Fun():
    def __init__(self):it__(self, vehicle_id, type1, cost, pre_amount):
        self.__vehicle_id = vehicle_id
        self.__type1 = type1
        self.__cost = cost
        self.__pre_amount = pre_amount

    def get_func(self):
        if (self.__type1 == "two wheelers"):
            pre_amount = (2 / 100) * self.__cost

        elif (self.__type1 == "Four wheelers"):
            pre_amount = (6 / 100) * self.__cost
        else:
            pre_amount = "error"
        return pre_amount

    def set_func(self):
        print(self.__pre_amount)

    def display(self):
        print("the vehicle details are", self.__type1)


F1 = Fun(50, "wheelers", 100, 0)
print(F1.get_func())
F1.display()
'''
class Fun():
    def __init__(self):
        self.__student_id = None
        self.__age = None
        self.__marks = None

    def set_id(self, id):
        self.__s_id = id

    def get_id(self):
        return self.__s_id

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def valid_age(self):
        if (self.__age > 20):
            return True
        else:
            return False

    def valid_marks(self):
        if (self.__marks >= 0 and self.__marks <= 100):
            return True
        else:
            return False

    def course(self, marks):
        d = {"CSE": 2554, "MECh": 2555}
        if (marks > 85):
            for i in d:
                d[i] = d[i] - d[i] * 0.25
            print("The course is offered to you after discount of 25%", d)
        else:
            print("The course offered to u:", d)

    def valid_qualification(self):
        if (self.__marks and self.valid_marks() and self.valid_age()):
            self.course(self.__marks)
            return True
        else:
            return False


s1 = Fun()
s1.set_id(9)
s1.set_age(21)
s1.set_marks(89)
if (s1.valid_qualification()):
    print("Admission can be done")
else:
    print("admission can not be done")