#assignment 7.2
count = 0
tot = 0
fname = input('Enter file name: ')
fh = open(fname)
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count+1
        len_ =len('X-DSPAM-Confidence:')+1
        target_part=line[len_:]
        fval = float(target_part.strip())
        tot = tot + fval
    else:
        continue

print("Average spam confidence:",tot/count)
