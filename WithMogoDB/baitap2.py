import json
import mongo

my = mongo.database()



# with open('d:/Python/WithMogoDB/json.json') as data_file:
#     data = json.load(data_file)
#     for x in data["students"]:
#         student = mongo.Students(x["name"], x["age"], x["gender"], x["idclass"])
#         data = {"name" : student.name, "age" : student.age, "gender" : student.gender, "class" : student.idclass}
#         #data = (x["name"], x["age"], x["gender"],x["idclass"])
#         my.insertStudent(data)

# data_file.close()

# # lay ra thong tin cua 1 hoc sinh
# namestudent = "Nguyen Van A"
# my.getone(namestudent)

# #xoa 1 hoc sinh
# namestudent = "Nguyen Van A"
# my.deleteStudent(namestudent)