letters = [chr(int('0x30a0', 16) + i) for i in range(96)]
print(letters)

for i in range(96):
    symbol = chr(int('0x30a0', 16) + i)
    print(symbol, end=' ')