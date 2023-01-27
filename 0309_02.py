def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    dices =(a,b,c,d)

def comp(a,b):
    awin=0
    bwin=0
    for vala in a:
         for valb in b:
            if vala>valb:
                awin=awin+1
            elif vala<valb:
                bwin=bwin+1
            else:
                continue
    if awin>bwin:
        return 0
    elif awin<bwin:
        return 1
    else:
        return -1



def triple(ab,ac,bc):
    if ab==ac==0:
       return 0
    elif bc==0 and ab==1:
       return 1
    elif bc==ac==1:
       return 2
    else:
       return -1


a=[1, 1, 6, 6, 8, 8]
b=[2, 2, 4, 4, 9, 9]
c=[3, 3, 5, 5, 7, 7]
ab=comp(a,b)
bc=comp(b,c)
ac=comp(a,c)
result1=triple(ab,ac,bc)
print(result1)

d=[1, 1, 2, 4, 5, 7]
e=[1, 2, 2, 3, 4, 7]
f=[1, 2, 3, 4, 5, 6]
de=comp(d,e)
df=comp(d,f)
ef=comp(e,f)
result2=triple(de,df,ef)

print(result2)

def quar(ab,ac,ad,bc,bd,cd):
    if ab==ac==ad==0:
        return 0
    elif ab==1 and bc==bd==0:
        return 1
    elif ac==bc==1 and cd==0:
        return 2
    elif ad==bd==cd==1:
        return 3
    else:
        return -1

g=[3, 3, 3, 3, 3, 3]
h=[6, 6, 2, 2, 2,  2]
i=[4, 4, 4, 4, 0, 0]
j=[5, 5, 5, 1, 1, 1]
gh=comp(g,h)
gi=comp(g,i)
gj=comp(g,j)
hi=comp(h,i)
hj=comp(h,j)
ij=comp(i,j)
result3=quar(gh,gi,gj,hi,hj,ij)
print(result3)
