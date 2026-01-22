# 단어의 길이가 3인 단어가 몇개인지 출력하세요

test_list = ['one','two','three', 'bc']
count=0

for i in test_list:
    print(i,':',len(i))
    if len(i) == 3:
       count += 1

print("결과 : ",count)

a = [(1,2), (3,4), (5,6)]
# 리스트 합을 구하시오.
tot=0

for i,j in a:
    #tot += k[0]+k[1]
    tot += (i+j)
print(tot)


