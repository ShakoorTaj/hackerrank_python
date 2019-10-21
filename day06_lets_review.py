name = 'Hacker'
even = ''
odd = ''
for i, k in enumerate(name):
    if i % 2 == 0:
        # print(k, i)
        even = even + k
    else:
        # print(k, i)
        odd = odd + k
print(f'{even} {odd}')

        # even   odd
print(name[::2], name[1::2])
