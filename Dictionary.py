person = {
    'name': 'Tieu Vu',
    'age': 22,
    'male': True,
    'status': 'single'        
    }

print(person['name']) # Tieu Vu
person['status'] = 'alone'
print(person)

del person['status'] #xóa phần tử 
person.clear() # xóa tất cả các phần tử trong dictionary person

del person # xóa hẳn dictionary person

#dictionary lồng nhau
person = {
    'name': 'Tiêu Vũ',
    'option': {
                'age': 22,
                'male': True,
                'status': 'alone'
            }        
    }

print(person['option']['age'])