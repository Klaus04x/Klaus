# Bài 1
# a = int(input('Nhập số tuổi của bạn:'))
# if a>0:
#     if 0<=a<=30:
#         print('Bạn vẫn còn trẻ')
#     elif 30<a<=60:
#         print('Ban đang ở độ tuổi trung niên')
#     elif a>60:
#         print('Bạn đang ở tuổi già')
# else:
#     print('? Bạn không phải là người')


# Bài 2


# a = int(input('Nhập số nguyên a:'))
# if a == 0:
#     print('Số 0 không phải là số chẵn cũng không phải là số lẻ')
# elif a < 0:
#     print('Số không phải là số nguyên dương')
# elif a % 2 == 1:
#     print('Số là số lẻ')
# else:
#     print('Số là số dương')


# Bài 3
# a = int(input('Nhập cạnh a:'))
# b = int(input('Nhập cạnh b:'))
# c = int(input('Nhập cạnh c:'))
# if a>b>c>0 or a+b>c or b+c>a or a+c>b:
#     print('3 cạnh của tam giác')
# else:
#     print('Không là 3 cạnh của tam giác')

# Bài 4
# import time
# nam = int(input('Ban hãy nhập năm sinh của mình: '))
# x=time.localtime() 
# year=x[0]
# print('Tuổi của bạn là:',year-nam)

# Bài 5
# import math
# a = int(input('Nhập vào số nguyên a:'))
# if 20 <= a <= 70:
#     print('False')
# else:
#     if a % 5 ==0:
#         print('True')


# Bài 6
# import math
# a = int(input('Nhập số a:'))
# if math.sqrt(a) == int(math.sqrt(a)):
#     print('a là số chính phương')
# else:
#     print('a không phải là số chính phương')


# Bài 7

# import math
# print('Phương trình bậc nhất có dạng ax+b=0')
# a = float(input('Nhập số a:'))
# b = float(input('Nhập số b:'))
# print('Phương trình bậc nhất có dạng:{0}x+{1}=0'.format(a,b))
# if a == 0:
#     print('x={0}'.format(-b))
# else:
#     x = -b/a
#     print('x=',x)

#Bài 8
import math
print('Phương trình bậc 2 có dạng: ax^2+bx+c=0')
a = float(input('Nhập số a:'))
b = float(input('Nhập số b:'))
c = float(input('Nhập số c:'))
print('Phương trình bậc 2 có dạng: {0}x^2+{1}x+{2}=0'.format(a,b,c))
if a == 0:
    print('Nghiệm của x là:',-c/b)
else:
    delta = b*b-4*a*c
    if delta < 0:
        print('Phương trình vô nghiệm')
    elif delta == 0:
        print('Phương trình có nghiệm kép x1=x2=',-b/(2*a))
    elif delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print('Phương trình có 2 nghiệm phân biệt:x1={0},x2={1}'.format(x1,x2))


