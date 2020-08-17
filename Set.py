#một set kiểu numbers
set1={5,7,8,6}
print(set1)    #return {8, 5, 6, 7}
 
#một set kiểu string
set2={"hello", "hi", "xin chao"}
print(set2)    #return  {'hi', 'hello', 'xin chao'}
 
#set với kiểu dữ liệu hỗn hợp
set3 = {"hello", 5, (1,5,7)}
print(set3)    #return {(1, 5, 7), 5, 'hello'}
 
 
name = {'hieu', 'hieu'}#phần tử trùng nhau thì sẽ tự động loại bỏ các phần tử lặp
print(name)
#return {'hieu'}

 #truy cap phan tu trong set
myset = {5,7,6,4}
for item in myset:
   print(item)

   #them phan tu
myset1 = {4,8,7,5}
 
#thêm một số vào set
myset1.add(6)
print(myset) #return {4, 5, 6, 7, 8}
 
#thêm một chuỗi cũng làm như thêm một số vậy
myset1.add("hello")
print(myset1) #retrun {4, 5, 6, 7, 8, 'hello'}

#update set
name={'hieu', 'hoai', 'anh', 'loc'}
name.update(['john', 'lina', 'hary'])
print(name)
#return {'hoai', 'anh', 'loc', 'lina', 'john', 'hary', 'hieu'}

#loai bo phan tu
    #removed
    thisset = {"apple", "banana", "cherry"}
    #xóa phần tử "banana
    thisset.remove("banana")
    print(thisset)
    #return {'apple', 'cherry'}

    #discard
    thisset = {"apple", "banana", "cherry"}
    thisset.discard("banana")
    print(thisset)
    #return {'apple', 'cherry'}
    
    #pop
    thisset = {"apple", "banana", "cherry"}
 
    x = thisset.pop()
    print(x) # trong trường hợp này phần tử cuối cùng là 'apple'
    
    print(thisset)
    #return {'banana', 'cherry'}


    #clear
    thisset = {"apple", "banana", "cherry"}
    thisset.clear()
    print(thisset)
    #return set()

    #del
    thisset = {"apple", "banana", "cherry"}
    del thisset
    print(thisset)

    #kiem tra phan tu co trong set hay k
    thisset = {10,15,19,14}
 
    #kiểm tra xem số 10 có trong set hay không
    print(10 in thisset)   #return True
    
    #kiểm tra xem số 15 có mặt không
    print(15 not in thisset) # return False