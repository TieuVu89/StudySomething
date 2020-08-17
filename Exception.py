def sum(a, b):
    return a / b

try :
    print(sum(6, 0))
except ZeroDivisionError:
    print('Co loi xay ra!')
finally:
    print('finally duoc goi!')
# Ket qua:
# Co loi xay ra!
# finally duoc goi!