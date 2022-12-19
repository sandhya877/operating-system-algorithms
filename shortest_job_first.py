a=int(input("enter a number:"))
at=[]
bt=[]
pid=[]
for i in range(0,a):
    pid.append(i)
print(pid)
print("enter arrival times:")
for i in range(0,a):
    c=int(input())
    at.append(c)

print(at)
print("enter burst times:")
for i in range(0,a):
    b=int(input())
    bt.append(b)
print(bt)
at=sorted(at)
print(at)
ct=[]

