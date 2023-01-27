largest=None
counts=dict()
name=input('Enter file: ')
if len(name)<1:
    name='mbox-short.txt'
fh=open(name)
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        word=line.split()
        mailadd=word[1]
        counts[mailadd]=counts.get(mailadd,0)+1
for a,b in counts.items():
    if largest is None or b>largest:
        largest=b
        x=a
    else:
        continue
print(x,largest)
