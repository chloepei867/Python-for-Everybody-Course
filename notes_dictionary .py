#dictionaries像一个大袋子，可以装很多东西，没有顺序，要用"lookup tag"来索引里面的元素
purse=dict()
#money是标签
purse['money']=12
purse['candy']=3
purse['tissues']=33
print(purse)
#返回结果为：{'money':12,'candy':3,'tissue':33}
print(purse['money'])
#返回结果为：12
purse['candy']=purse['candy']+3
print(purse['candy'])
#返回结果是：6

#dic最经常用来count
ccc=dict()
ccc['a']=1
ccc['b']=1
ccc['a']=ccc['a']+1
#查找
'a' in ccc
#返回值为true

counts=dict()
names=['eesd','esgk','gkeo','oiec','deocs']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)

#the get method for dictionaries
#查看某个元素是否在dic里
if name in counts:
    x=counts[name]
else:
    x=0

#等同于：
x=counts.get(name,0)

#所以(上面一段代码的简化版)：
counts=dict()
names=['eesd','esgk','gkeo','oiec','deocs']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)

#loops and dictionaries
#迭代的是key，不是value
counts={'money':12,'candy':3,'tissue':33}
for key in counts:
    print(key,counts[key])

#从dictionaries中分别获得keys和values
counts={'money':12,'candy':3,'tissue':33}
print(list(counts))
#返回值为：['money','candy','tissue']
print(counts.value())
#返回值为：[12,3,33]
print(counts.items())
#返回值是：[('money':12),('candy':3),('tissue':33)]

#同时有两个迭代变量
counts={'money':12,'candy':3,'tissue':33}
for a,b in counts.items():
    print(a,b)

a = list()
#等同于：
a = []

b = str()
#等同于：
b = ""

c = dict()
#等同于：
c = {}

#docstring:给你自己定义的function加注释(下面绿色的一行就是docstring)
def format_name(f_name,l_name):
    """Take a first and last name and format it to
    return the title case version of the name."""
    #下面具体写函数内容
