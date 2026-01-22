t1 = ()
print(t1)
print(type(t1))
t2 = (1,)
print(t2)
print(type(t2))
t3 = (1, 2, 3)
t3[0] = 9  # 값의 변경
t4 = 1, 2, 3
print(t4)
t5 = ('a', 'b', ('ab', 'cd'))
print(t5[2][1][1])

# del t5[0]
