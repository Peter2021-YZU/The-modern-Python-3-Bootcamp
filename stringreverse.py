str = input("")
n = int(input(""))
rev = str[slice(n-1,None,-1)]
i = n
j = 0
while i < len(str):
	j += 1
	i += 1
	if j == n:
		rev += str[slice(i-1,i-n-1,-1)]
		j = 0
	
print(rev)