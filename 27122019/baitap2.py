#Viết một chương trình Python cho phép in ra tổng của các số nguyên nằm trong khoảng
#từ 200-600 và chia hết cho 3.
total = 0
for number in range(200, 600):
    if (number%3) == 0:
        total += number
print ("Tong so nguyen chia het cho 3 tu 200 den 600: " + str(total))

for number in range(200, 600):
    if (number%5) == 0:
        print(str(number))
