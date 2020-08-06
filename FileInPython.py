# mo file
file = open('Vong lap.py')
# doc file
data = file.read();
# dong file
file.close()
# in du lieu doc duoc
print(data)

# mo file o che do ghi
file = open('Vong lap.py','w')
# ghi file
file.write('#Tieu Vu')
# dong file
file.close()