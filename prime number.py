Python 3.7.0a2 (v3.7.0a2:f7ac4fe, Oct 17 2017, 17:06:29) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Python program to print all
# prime number in an interval
# number should be greater than 1
start = 11
end = 25

for i in range(start, end+1):
if i>1:
	for j in range(2,i):
		if(i % j==0):
			break
	else:
		print(i)
