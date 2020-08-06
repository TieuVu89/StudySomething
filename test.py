# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["mydatabase"]

# mycol = mydb["students"]

# mydict = { "name": "John", "age": "22", "gender": "nam", "class": "1"}

# x = mycol.insert_one(mydict)

class Foo:
    # Khai báo thuộc tính ở dạng public
    name = "Foo"
    # Khai báo phương thức ở dạng public
    def getName(self):
        # gọi thành phần trong class
        print(self.name)

# gọi thành phần ngoài class
print(Foo().name) # Foo
Foo().getName() # Foo

class Bar(Foo):
    pass

#test
Bar().getName()