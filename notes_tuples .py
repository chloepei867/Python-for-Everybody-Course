#tuples和strings一样，immutable

#tuples和list很像，但是一个用（），一个用[]

#赋值
(x,y)=(4,'chloe')
print(x)
#返回值为：4

#比较
(0,1,2)<(5,1,2)
#返回值为：true。只比较第一个元素的大小
(0,1,2)<(0,4,2)
#返回值为：true。第一个元素相等，就比较第二个元素，以此类推。
('Jones','Sally')<('Jones','Sam')
#返回值为：true。因为‘Sally’中的第三个元素'l'在‘Sam’的第三个元素'm'之前

#sorting lists of tuples
d={'a':10,'b':1,'c':22,}
d.items()
#返回值为：dict_items([('a':10),('c':22),('b':1)])

#sorted by key
sort(d.items())
#返回值为：[('a':10),('b':1),('c':22)]
for k,v in sort(d.items()):
    print(k,v)

#sorted by 不是value
c={'a':10,'b':1,'c':22,}
tmp=list()
for k,v in c.items():
    tmp.append((v,k))

tmp=sort(tmp,reverse=True)
print(tmp)
#返回值为：[(22:'c'),(10:'a'),(1:'b')]#value按由高到低排列

#the top 10 most common words
fhand=open('romeo.txt')
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst=list()
#key/value翻转
for k,v in counts.items():
    newtup=(v,k)
    lst.append(newtup)
lst=sort(lst,reverse=True)

for v,k in lst[:10]:
    print(k,v)


#简易办法翻转
c={'a':10,'b':1,'c':22,}
print(sort([(v,k)for k,v in c.items()]))
#返回值为：[(1,'b'),(10,'a'),(22,'c')]

#tuple只有两个methods：count（）和index（）


#tuple.count("element")
t = ('a','a','b')
x = t.count('a')
#则x = 2

y = t.index('a')
#则y = 0
