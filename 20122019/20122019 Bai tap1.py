param1 = input("Nhap phan tu 1: ")
param2 = input("Nhap phan tu 2: ")
pheptinh = input("Nhap vao phep tinh muon thuc hien (+-*/): ")
if pheptinh == "+":
    ketqua = int(param1) + int(param2)
    print("Result: " + str(ketqua))
elif pheptinh == "-":
    ketqua = int(param1) - int(param2)
    print("Result: " + str(ketqua))
elif pheptinh == "*":
    ketqua = int(param1) * int(param2)
    print("Result: " + str(ketqua))
elif pheptinh == "/":
    ketqua = int(param1) / int(param2)
    print("Result: " + str(ketqua))
else:
    print("Khong co phep tinh nay")

