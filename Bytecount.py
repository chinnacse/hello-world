#It is a code about byte count in computer networks using python
n=input("enter the number of elements")
elements=[]
for i in range(0,n):
	s=input()
	elements.append(s)
a=0
f=1
c=0
sum=0
while(a<n):
	r=elements[c]
	if(sum+r<=n):
		print "frame",f,elements[c:c+r]
		a=a+r
		c=c+r
		f=f+1
		sum=sum+r
	else:
		print "chinna"
		break
