import json
import mongo

my = mongo.database()



with open('json.json') as data_file:
    data = json.load(data_file)
    for x in data["students"]:
        student = mongo.Students(x["name"], x["age"], x["gender"], x["idclass"])
        data = {"name" : student.name, "age" : student.age, "gender" : student.gender, "class" : student.idclass}
        #data = (x["name"], x["age"], x["gender"],x["idclass"])
        my.insertStudent(data)

data_file.close()
