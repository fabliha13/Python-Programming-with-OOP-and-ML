class Student:

    # def __init__(self,name, ID):
    #     self.name = name
    #     self.id = ID

    #     print("I am the first init")

    def __init__(self, *info): #info = (name, id, class)
        if len(info)==3:

            self.name = info[0]
            self.id = info[1]
            self.cls = info[2]

        elif len(info)==2: #info=(name,id)
            self.name = info[0]
            self.id = info[1]
        else:
            self.name = info[0]
            

        print("I am the second init")


b1 = Student("fab", 214)

b2= Student("tah", 245, 9)
