import time
nam = int(input('Ban hãy nhập năm sinh của mình: '))
x=time.localtime() 
year=x[0]
print('Tuổi của bạn là:',year-nam)
