a=[1,2,3]
result = [i*3 for i in a]

# 열거형 자료
fruits = ['apple', 'banana', 'orange']

for i, fruit in enumerate(fruits):
     print(f"{i}: {fruit}")


for fruit in fruits:
     print(f"{fruit}")

# zip 함수로 여러 리스트 함께 순회하기
#      
names = ['홍길동','김철수','이영희','이하나']
scores = [85,92,78,90,78]

for name, score in zip(names,scores):
     print(f"{name}님 {score}점")
