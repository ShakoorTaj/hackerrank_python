# solution code for HR editor...

n = 13 #int(input())
num_in_binary = bin(n)
binary = num_in_binary[2:]
list_of_ones = num_in_binary[2:].split('0')

print(binary)
print(len(max(list_of_ones))) # max --> first check max element, len check length of max element

