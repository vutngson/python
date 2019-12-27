total = 0
number = 100
while number >= 1:
    total += number
    number -= 1
print ("Tong 100 so nguyen dau tien: " + str(total))

fromNumber = 20
toNumber = 42
while fromNumber <= toNumber:
    if(fromNumber % 3 == 0):
        print(fromNumber)
    fromNumber += 1

fromNumber = 100
toNumber = 50
while fromNumber >= toNumber:
    if(fromNumber % 2 != 0):
        print(fromNumber)
    fromNumber -= 1