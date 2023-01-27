largest=None
smallest=None
while True:
    sval=input('Enter a number:')
    if sval =="done":
        break
    try:
        fval=float(sval)
    except:
        print('Invalid input')
    #刚开始漏了这一步，导致第一次迭代时，largest（None）和fval是无法比较的
    if largest == None:
        largest=fval
        smallest=fval
    elif largest<fval:
        largest = fval
    elif smallest >fval:
        smallest = fval
    else:
        continue

print("Maximum is",int(largest))
print('Minimum is',int(smallest))
