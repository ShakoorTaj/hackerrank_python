class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        first_element = self.__elements[0]  # b[0]
        next_elements = self.__elements[1::]  # b[1::]
        max_diff = [abs(first_element - element) for element in next_elements]
        maximumDifference = max(max_diff)
        return maximumDifference

a = [1,2,5,7]

d = Difference(a)
print(d.computeDifference())
