def mutiply(x):
    return x * x


result = map(mutiply, [1, 2, 3, 4])

print(list(result)) # [1, 4, 9, 16]



result = filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 22])

print(list(result))  # [1, 3, 5, 7, 9]
