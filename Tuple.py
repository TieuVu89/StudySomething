day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')

a = ();#tuple trống

a = (10,)#tuple chỉ chứa duy nhất 1 giá trị

print(day[0]) # monday

print(day[-2]) # saturday

print(day[1:3]) # ('tuesday', 'wednesday')

del day # xóa tuple

#tuple lồng 
day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday', day1)

# day = day1 + day2

print(day2)
# ('thursday', 'friday', 'saturday', 'sunday', ('monday', 'tuesday', 'wednesday'))

print(day2[4][0]) 