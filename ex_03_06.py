xh = input("Enter Hours:")
xr = input("Enter Rate:")
xp = float(xh)*float(xr)
print("Pay:",xp)

#3.2 conditional statement
num = input('Enter your number:')
try:
    inum = int(num)
except:
    inum = -1
if inum > 0:
    print('Nice work!')
else:
    print('Not a number')

#assignment 3.1
hrs = input('Enter Hours:')
rt = input('Enter Rate:')

if float(hrs)<=40:
    pay = float(hrs)*float(rt)
else:
    pay = (40+(float(hrs)-40)*1.5)*float(rt)

print(pay)


#assignment 3.3
#想要用range（）函数失败。。。
score = input('Enter Score:')
fscore = float(score)
if fscore >1:
    print('error')
elif fscore <0:
    print('error')
else:
    if fscore >=0.9:
        print('A')
    elif fscore >=0.8:
        print('B')
    elif fscore >=0.7:
        print('C')
    elif fscore >=0.6:
        print('D')
    else:
        print('F')

#assignment 4.6
def computepay(h,r):
    p = h*r
    return(p)

hrs = input('Enter Hours:')
rt = input('Enter Rate:')
fhrs = float(hrs)
frt = float(rt)

if fhrs>40:
    Pay = computepay((fhrs-40)*1.5+40,frt)
else:
    Pay = computepay(fhrs,frt)

print('Pay',Pay)

#5.3 lecture:找最大数
largest_so_far = -1000
for my_num in [34,56,3,345,4]:
    if my_num > largest_so_far:
        largest_so_far=my_num
print('the larget number:',largest_so_far)

#sum in a loop
sum=0
count=0
for thing in [34,56,3,345,4]:
    count=count+1
    sum = sum+thing
print('sum:',sum)
#loop中的均值
print('average:',sum/count)


#找最小值
smallest = None
for value in [445,123,76,897,145,56789]:
    if smallest == None ：
       smallest = value
    elif value < smallest :
        smallest = value

print('the smallest number is:',smallest)

#worked exercise:5.1
num = 0
tot = 0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
    num = num+1
    tot = tot+fval

print(tot,num,tot/num)
