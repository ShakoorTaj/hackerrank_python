if __name__ == '__main__':
    n = int(input())

    arr = ['1','2','3','4']#list(map(int, input().rstrip().split()))
    for i in arr[::-1]:
        pass
        # print(i, end=' ')

# second method to do
print(' '.join(map(str, arr[::-1])))