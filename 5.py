def computepay(h,r):
	f =0
	if h<=40:
    	f = h*r
	else:
		f = 40*r + (h-40)*(r*1.5)
        
	return f

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate per hour:")
r = float(rate)
print computepay(h,r)

