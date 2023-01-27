lst=list()
counts=dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if not line.startswith('From '):
        continue
    else:
        word=line.split()
        time=word[5]
        newtime=time.split(':')
        hour=newtime[0]
    counts[hour]=counts.get(hour,0)+1
for a,b in counts.items():
    newtup=(a,b)
    lst.append(newtup)
list.sort()
for v,k in lst:
    print(v,k)
