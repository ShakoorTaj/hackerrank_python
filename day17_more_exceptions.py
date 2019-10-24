class Calculator:
    def power(self, n, p):
        if n >= 0:
            if p >= 0:
                print(n**p)
            else:
                print('n and p should be non-negative')
        else:
            print('n and p should be non-negative')


cal = Calculator()
cal.power(0,10)