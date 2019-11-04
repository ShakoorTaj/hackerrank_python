import sys


class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []  # list type stack
        self.queue = []  # list type queue

    def pushCharacter(self, char):  # for stack
        self.stack.append(char)  # used append because type of stack is list

    def enqueueCharacter(self, char):  # for queue
        self.queue.append(char)  # used append because type of queue is list

    def popCharacter(self):  # for stack pop first element on stack LIFO
        return self.stack.pop(0)

    def dequeueCharacter(self):  # for queue pop last element from queue FIFO
        return self.queue.pop(-1)


# read the string s
s = 'racecar' # input() # racecar
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
