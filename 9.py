fname = raw_input("Enter file name: ")
fh = open(fname)
average = 0 
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    
    number = line.split()
    sum = sum + float(number[1])
    count = count +1
    average = sum / count    
print "Average spam confidence:", average
