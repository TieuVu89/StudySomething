name = ['Tieu Vu', 'Nguyen Van A', 'Nguyen Van B']
print(name[0]) #in ra phẩn tử đầu tiên
print(name[1]) 
print(name[2]) 

print(name[-3]) 
print(name[-2])
print(name[-1])# in ra phần tử cuối cùng

print(name[0:1]) # in ra phần tử từ index 0 đến index 1
name[1] = 1998
print(name)

del name[2] #xóa phần tử t2 của mảng
print(name)

option = [12,5,1996] 
myList = ['Vu Thanh Tai', option] # mảng lồng nhau
print(myList)
# ['Vu Thanh Tai', [12, 5, 1996]]

subList = myList[1] # [12, 5, 1996]
print(subList[0]) # 12

# hoặc có thể viết ngắn gọn như sau
print(myList[1][0]) # 12