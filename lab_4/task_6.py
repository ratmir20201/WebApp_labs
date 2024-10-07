my_str = "X-DSPAM-Confidence:0.8475"
pos = my_str.find(':')
num = my_str[pos + 1:]
print(float(num))