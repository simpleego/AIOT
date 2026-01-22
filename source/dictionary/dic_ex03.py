a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
keys = a.keys()
print(type(keys))

for key in a.keys():
    print(key,'-->',a[key])

list_key = list(a.keys())
print(list_key)

print(a[list_key[2]])

# 딕셔너리의 모든 값 출력
print(type(a.values()))

for value in a.values():
    print(value)

# 키와 값의 쌍을 구하기
# 
items = a.items()    
print(items)

# 키로 값을 구하는 함수
val = a.get('name1')e
print(val)
print(a['name'])



# 값의 존재 여부 확인
print("pey" in a)

# key로 값을 얻기
val = a.pop('phone')
print(val)
print(a)


