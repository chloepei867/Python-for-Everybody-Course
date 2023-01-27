a = list(range(0,11,2))
#则 a =[0,2,4,6,8,10]


index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

#enumerate()
word = 'abcde'
for item in enumerate(word):
    print(item)

#打印结果为五个tuples：
#(0,'a')
#(1,'b')
#(2,'c')
#(3,'d')
#(4,'e')

#zip()：返回的也是tuples
mylist1 =[1,2,3]
mylist2 =['a','b','c']
for item in zip(myliest1,mylist2):
    print(item)

#打印结果为：
#(1,'a')
#(2,'b')
#(3,'c')

a = list(zip(myliest1,mylist2))
#则 a = [(1,'a'),(2,'b'),(3,'c')]
