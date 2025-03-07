class Calculator:

    def product(self, *nums):
        result = 1

        for el in nums:
            result = result * el


        print(result)


    # def product(self, num1, num2, num3):


obj = Calculator()


obj.product(4)
obj.product(4,5)
obj.product(4,5,6)
obj.product(4,5,6,7,8,10)

