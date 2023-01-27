#寻找lists里面的元素
friend = ['lisa','jenny','chloe']
print(friend[1])#打印出来的就是jenny
print(friend[-1]#打印出来的就是chloe

#mutable：改变lists
#strings是不能改变的
a=[2,64,53,3,333,358]
a[0]=1000 #这样就把第一个数字变成1000了

# 关于range()
print(range(4)) #打印结果为[0,1,2,3]

#两种loops的方式
friends = ['lisa','jenny','chloe']
for friend in friends:
    print['happy new year:',friend]

#方法二
for i in range(len(friends)):
    friend = friends[i]
    print('happy new year:',friend)

#manipulating lists
#1/两个lists链接
a=[1,2,3,5]
b=[4,5,8]
c=a+b

#2/slice
t=[12,4,66,75,73]
t[1:4] #结果就是[4,66,75]

#3/创建一个lists
a=list()
a.append('chloe')
a.append(99)
a.apend('book')
print(a) #结果就是['chloe',99,'book']
#extend：用于添加一串元素
a.extend(["Angela","Melisa","Mark"])

#4查看某个元素是否在lists里？用‘in’
a=[12,4,66,75,73]
4 in a
#返回值为：True
10 in a
#返回值为：false
10 not in a
#返回值为：True

#5改变lsits的排序：sort
friends = ['lisa','jenny','chloe']
friends.sort()
#结果就是按照首字母从小到大排序了，sort排序不能自己定义怎么拍

#6其他用于lists的built-in functions
a=[12,4,66,75,73]
print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a)) #均值

#input
numlist=list()
while True:
    inp = input('Enter a number: ')
    if inp == "done":
        break
    value =float(inp)
    numlist.append(value)

print(sum(numlist)/len(numlist))

#split():把strings进行拆分
abc='with three words'
a=abc.split()
print(a)
#打印结果为：['with','three','words']

#split可以根据空格来切分strings，也可以指定
line = 'first;second;third'
a=line.split(';')
#打印出来的就是['first','second','third']

#list.pop(i)
'''删除给定位置的元素并且返回其值。
如果没有指定位置，则删除最后一位并返回值'''

#list.reverse()
#将list倒序排列
