import pymongo
class database:
    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        global mydb
        mydb = myclient["mydatabase"]
        global mycol 
        mycol = mydb["students"]

    def createTable(self, nametb):     
        collist = mydb.list_collection_names()
        if nametb in collist:
            print("The collection exists.")
        else: 
            mycol = mydb[nametb]
        
    def deleteTable(self, nametb):
        collist = mydb.list_collection_names()
        if "nametb" not in collist:
            print("The collection not exists. ")
        else: 
            nametb.drop()
            print(" Xóa bảng thành công ")

    def insertStudent(self, student):
        mycol.insert_one(student)
        print("Thêm thành công")

    def insertAll(self, data):
        mycol.insert_many(data)
        print("Thêm thành công. ")

    def deleteStudent(self, idstudent):
        myquery = { "id" : "idstudent" }
        mycol.delete_one(myquery)
        print('xóa thành công')
    
    def getone(self, idstudent):
        myquery = { "id" : "idstudent" }
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)
    
    def updateStudent(self, idstudent):
        pass

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def setinfo(self, name, age):
        print("Xin chao {0} : {1}" + name, age)
class Students(Person):
    def __init__(self,name,age,gender,idclass):
        super().__init__(name,age,gender)
        self.id = id
        self.idclass = idclass

    def getclass(self,idclass):
        print("Class {0}" + idclass)

    def getall(self):
       return print("Sinh viên: ",self.name," tuoi ",self.age," gioi tinh ",self.gender," học lớp ",self.idclass)
