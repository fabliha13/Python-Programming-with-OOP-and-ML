class Student:

    def __init__(self,num1,num2,name):
        self.n1 = num1
        self.n2 = num2
        self.n = name

    def add(self):
        result = self.n1+ self.n2

        print(result)

    def name(self):
        print(self.n)
        print(self.n1)
    

s1 = Student(5,3,"Fbliha")
s2 = Student(6,1, "Arman")

s1.add()
s2.add()
s1.name()

#to create more then one objects of a class, we must use the __init__ function at the beginning to inialize it

