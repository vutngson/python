luong = float(input("Nhap luong : "))
phucap = float(input("Phu cap : "))
tongthunhap = luong + phucap
giamtru = 9000
thunhapchiuthue = tongthunhap - 9000
thuesuat = 0
if(thunhapchiuthue > 0):
    if(thunhapchiuthue <= 5000):
        thuesuat = 0.05
    elif ( 5000 <thunhapchiuthue <= 10000):
        thuesuat = 0.1
    elif (5000 <thunhapchiuthue <= 10000):
        thuesuat = 0.15
    elif (10000 <thunhapchiuthue <= 15000):
        thuesuat = 0.2
    elif (thunhapchiuthue > 20000):
        thuesuat = 0.25
else:
    thuesuat= 0
tienthue = thunhapchiuthue * thuesuat
thucnhan = tongthunhap - tienthue
print ("Thuc nhan: " + str(thucnhan))