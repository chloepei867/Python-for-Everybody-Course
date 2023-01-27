fname=input('Enter file name: ')
fh=open(fname)
lst=list()
count=0
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '):continue #from后面要加一个空格。看了txt里的数据才发现有from和from：
    count=count+1
    words=line.split()
    print(words[1])

print('There were',count,'lines in the file with From as the first word')



#mbox-short.txt
