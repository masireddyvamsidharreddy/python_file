num=6
fcount=0
for fa in range(1,num+1):
	if(num%fa==0):
		fcount+=1
print("Prime" if fcount==2 else "Not Prime")