a = [1,2,3]
print(a)
a[2] = 4
print(a)

# 리스트 삭제
del a[1]
print(a)

# 리스트 값 추가
a.append(9)
print(a)

# 리스트 값 추가(insert)
a.insert(1,5)
print(a)

# 리스트 항목 삭제 remove('삭제할 값')
a.remove(5)
print(a)

# item = a.pop()
# print(a)
# print(item)


item = a.pop(1)
print(item)
print(a)

