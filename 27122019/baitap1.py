#tinh tong 100 so nguyen dau tien
total = 0
totalSquare = 0
count = 0
for number in range(1, 100):
    total += number
    totalSquare += number*number
    count += 1


print ("Tong 100 so nguyen dau tien: " + str(total))
print ("Tong binh phuong 100 so nguyen dau tien: " + str(totalSquare))
print ("Trung binh cong so nguyen dau tien: " + str(totalSquare/count))
print (": " + str(totalSquare/count))

number = int(input("Nhap giai thua: "))
result = number
while number > 1:
    number -= 1
    result *= number
print ("Giai thua: " + str(result))


