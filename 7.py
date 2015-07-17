text = "X-DSPAM-Confidence:    0.8475";
number = text.find(':')
n = text[number+1:].strip()
print float(n)