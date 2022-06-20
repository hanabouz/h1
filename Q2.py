decimal = int(input('Enter decimal number: '))
binaryList = []
while decimal > 0:
    b = decimal % 2
    decimal = int(decimal / 2)
    binaryList.append(b)

binaryList.reverse()
result = ''
for bit in binaryList:
    result = result + str(bit)
print(result)
