a=[1,2,3,4,5,3,2,1,6]
pos = a.index(3)
print(pos)

pos = a.index(3,pos+1,len(a))
print(pos)
