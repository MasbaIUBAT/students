class Employee:
    increment = 1.5
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.9
    def increase(self):
        self.salary = self.salary * Employee.increment
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount

    @staticmethod
    def isopen(day):
        if day == 'sunday':
            return False 
        else:
            return True
#Raghib_Shahriar = Employee('harry','jack',4000)
print(Employee.isopen('sunday'))
print('bangladeh')
hfkjfhjfhdshfdsjhf



