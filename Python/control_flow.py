if 1==1 :
    if 1>4 :
        print('block one executed')
    elif 3==3 :
        print('this block excuted')
    else :
        print('no block ececuted')

# iteration
# 1
# list
mylist=[1,2,3,4,5,6,7,8,9]
for i in mylist :
    print(i)
# 2
# dictionary
d ={'sam':123,'kam':523,'jam':879}
for i in d :
    print(i) #kys
    print(d[i]) #vals
# دیکشنری ها متد val و key دارند

# توپل آنپیکینگ
t = [ (1,2),(3,4),(5,6),(7,8)]
for tup1 , tup2 in t :
    print(tup1)
    print(tup2)

# range
x =10
range(x)
# range یک جنریتور است که هر بار خالی میکند