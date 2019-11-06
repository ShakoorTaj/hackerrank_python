class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        # return sum([i for i in range(1, n+1) if n % i == 0])
        return sum([i for i in range(1, n//2 + 1) if n % i == 0]) + n
        # sum_list = []
        # for i in range(1, n+1):
        #     if n%i == 0:
        #         sum_list.append(i)
        # return sum(sum_list)


n = 8 # int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)