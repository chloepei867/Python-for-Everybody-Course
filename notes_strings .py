#slice
mystring = "abcdef"
a = mystring[::-1]
print(a)
#打印结果为：'fedcba'

letter = "z"
a = letter * 5
print(a)
#打印结果为：'zzzzz'

#format() method
print('This is a string {}'.format('INSERTED'))
#打印结果为： This is a string INSERTED

print('The {} {} {}'.format('fox','brown','quick'))
#打印结果为：The fox brown quick

print('The {2} {1} {0}'.format('fox','brown','quick'))
#打印结果为：The quick brown fox

print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
#打印结果为：The quick brown fox

#float formatting follows "{value:width.precision f}"
result = 100/777
print("The result was {r:1.3f}".format(r=result))
#width表示你希望这个number有多长，不够就用空格凑
#打印结果为：The result was 0.129
