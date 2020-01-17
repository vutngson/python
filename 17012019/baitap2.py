def arearectangle(a, b):
    return int(a * b)
def square(a):
    return int(a * a)
def fractional(number):
    result = number
    while number > 1:
        number -= 1
        result *= number
    return float(result)

a = float(input("Nhap so a : "))
b = float(input("Nhap so b : "))


print("area rectangle: " + str(arearectangle(a,b)))
print("square: " + str(square(a)))
print("fractional: " + str(fractional(a)))

