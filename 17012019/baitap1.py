def sum(a, b):
    return a + b
def minus(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

a = float(input("Nhap so a : "))
b = float(input("Nhap so b : "))

print("Tong hai so: " + str(sum(a,b)))
print("Hieu hai so: " + str(minus(a,b)))
print("Nhan hai so: " + str(multiply(a,b)))
print("Chia hai so: " + str(divide(a,b)))


