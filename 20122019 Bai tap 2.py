import math
print("Tinh chu vi, dien tich hinh chu nhat ---------------")
a = input("Nhap chieu dai: ")
b = input("Nhap chieu rong: ")
chuvi = 2*(float(a) + float(b))
dientich = float(a) * float(b)
print("Tinh chu vi hinh chu nhat: " + str(chuvi))
print("Tinh dien tich hinh chu nhat: " + str(dientich))

print("Tinh chu vi, dien tich hinh tam giac ---------------")
a = input("Nhap canh 1: ")
b = input("Nhap canh 2: ")
c = input("Nhap canh 3: ")
chuvi = float(a) + float(b) + float(c)
p = chuvi/2
dientich = math.sqrt(p * (p - float(a)) * (p - float(b)) * (p - float(c)))
print("Tinh chu vi hinh tam giac: " + str(chuvi))
print("Tinh dien tich hinh tam giac: " + str(dientich))

print("Tinh chu vi, dien tich hinh hinh tron ---------------")
a = input("Nhap ban kinh: ")
chuvi = float(a) * 2 * 3.14
dientich = float(a) * float(a) * 3.14
print("Tinh chu vi hinh tron: " + str(chuvi))
print("Tinh dien tich hinh tron: " + str(dientich))

