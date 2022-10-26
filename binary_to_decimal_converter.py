class DecToBin:
    def __init__(self, num):
        self.num = num
        self.ans = ''
        if isinstance(self.num, int):
            self.whole_num_converter()
        elif isinstance(self.num, float):
            self.floating_converter()

    def whole_num_converter(self, val=None):
        value = self.num if val is None else val
        if value == 0:
            self.ans = '0'
        while value != 0:
            if value % 2 == 0:
                self.ans += '0'
                value /= 2
            else:
                self.ans += '1'
                value = (value - 1) / 2
        self.ans = self.ans[::-1]
        return self.ans

    def floating_converter(self):
        value = self.num
        temp = str(value)
        ind = temp.index('.')
        self.whole_num_converter(int(temp[:ind]))
        mantissa = ''
        while True:
            if (len(mantissa) == 20) or (temp[ind + 1:] == '0' and len(temp[ind + 1:]) == 1):
                break
            if int(temp[ind + 1:][0]) >= 5:
                mantissa += '1'
            else:
                mantissa += '0'
            value *= 2
            temp = str(value)
            ind = temp.index('.')
        self.ans += f".{mantissa}"
        return self.ans

    def __repr__(self):
        return f"{self.num} in binary is: {self.ans}"


test_values = [0.6953125, 0.859375, 5.5, 8.24434, 5, 10]
for values in test_values:
    print(DecToBin(values))
    print('')

'''
Expected Outputs
0.6953125 => 1011001
0.859375 => 110111
5.5 => 101.1
8.24434 => 1000.00111110100011010001
5 => 101
10 => 1010
'''
