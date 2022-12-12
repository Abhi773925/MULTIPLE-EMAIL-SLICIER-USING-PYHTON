
n=int(input("Number of emails you want to slice: "))
for i in range(1,n+1):
    n=str(input("\nEmail: "))
    l=len(n)
    d=0
    for i in range(1,l):
        if n[i]=='@':
            d=i
            break
    if d>0:
        a=""
        for i in range(0,d):
            a+=n[i]
        print("User Name: ",a,end="")
        q = ""
        for j in range(d+1,len(n)):
            q+=n[j]
        print("\nDomain: ",q,end="")
