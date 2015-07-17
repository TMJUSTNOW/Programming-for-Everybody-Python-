name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

dic = dict()
i = 0
words =list()

for line in fh:
    if not line.rstrip().startswith("From "):
		continue
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        if ':' in word:
            date = word.split(':')
            if len(date) == 3:
                hour = date[0]
                dic[hour] = dic.get(hour,0)+1


for k,v in sorted(dic.items()):
    print k, v


