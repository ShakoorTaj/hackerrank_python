n = 2
name_phone = {}
for i in range(n):
    x = input().split()  # name phone
    name_phone[x[0]] = x[1]  # x[0] --> name : x[1] --> phone

while True:
    name = input()
    if name in name_phone:
        print(name, "=", name_phone[name], sep='')
    else:
        print('Not found')

# # Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# name_phone = {}
# for i in range(n):
#     x = input().split()  # name phone
#     name_phone[x[0]] = x[1]  # x[0] --> name : x[1] --> phone
#
# for i in range(n):
#     # while True:
#     # try:
#     name = input()
#     if name in name_phone:
#         print(name, "=", name_phone[name], sep='')
#     else:
#         print('Not found')
#     # except:
#     #     break
