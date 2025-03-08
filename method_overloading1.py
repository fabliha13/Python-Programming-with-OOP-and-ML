# Method Overloading

class Calculator:



    def product(self, num1, num2 = None, num3 = None):
        if num1 != None and num2 != None and num3 != None:
            result = num1 * num2 * num3
        elif num1 != None and num2 != None:
            result = num1 * num2

        else:
            result = num1


        print(result)


    # def product(self, num1, num2):
    #     result = num1 * num2
    #     pass


obj = Calculator()


obj.product(4)
obj.product(4,5)
obj.product(4,5,6)
