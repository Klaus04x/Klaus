a = float(input('Nhập số điểm của bạn:'))
print('Số điểm bạn vừa nhập là:',a)
if 0<=a<=10:
    if a>=8.5:
        print("Điểm loại A")
    elif a>=6:
        print("Điểm loại B")
    elif a>=5:
        print('Điểm loại C')
    elif a<4:
        print('Trượt rồi bé ơi :))')
else:
    print('Số điểm bạn nhập không hợp lệ.')