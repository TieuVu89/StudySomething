def my_function(): #ham k co tham so truyen vao
  print("Hello from a function")

my_function()

def my_function2(fname, lname): #ham co 2 tham so truyen vao
  print(fname + " " + lname)

my_function2("Tieu", "Vu")

def my_function3(*kids): #k xac dinh dc bnhiu doi so truyen vao thi de * 
  print("The youngest child is " + kids[2])

my_function3("Emil", "Tobias", "Linus")

def my_function4(country = "Norway"): #neu k truyen tham so khi goi ham thi se dung gia tri tham so mac dinh
  print("I am from " + country)

my_function4("Sweden")
my_function4("India")
my_function4()
my_function4("Brazil")

#tham so truyen vao la 1 list
def my_function5(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function5(fruits)

#neu dinh nghia function xong ma k co noi dung thi can dua key 'pass' vao de k bi loi
def myfunction6():
  pass
#ham đệ quy
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        #print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
print(tri_recursion(6))