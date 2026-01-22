a = range(20)
print(type(a))

for i in range(10):
    print(i)

for i in range(10,1,-2):
    print(i)

# 1~100 까지의 합을 구하시오.
sum = 0
for i in range(1,101):
    print(i,end=" ")
    sum += i

print('1~100 까지의 합 :', sum)
