dict=[
    ["p1",5,7],
    ["p2",10,10],
    ["p3",7,5],
    ["p4",0,8],
    ["p5",3,6],
]

'''print(dict)
print(dict.values())
print(len(dict.values()))
print(dict.items())
for i in dict.items():
    print(i[1][1])
    print(sorted(dict,key=lambda x:x[i[1]])) 
print(len(dict))
print(len(dict[0]))
for i in range(len(dict)):
    
    for j in range(0,len(dict)-i-1):
        
        if dict[j][1]>dict[j+1][1]:
            temp=dict[i]
            dict[i]=dict[i+1]
            dict[i+1]=temp
            
        else:
            pass
print(dict)
ct=[]
sum=0
for i in range(dict):'''
for i in range(len(dict)-1):
   
    for j in range(len(dict)-1,0,-1):
        
        if dict[j][1]<dict[j-1][1]:
            temp=dict[j]
            dict[j]=dict[j-1]
            dict[j-1]=temp
            
        else:
            pass   

print(dict)

l=[]
ct=dict[0][1]+dict[0][2]
l.append(ct)
print(l)
dict.pop(0)
print(dict)

def test(dict,l):
    l3=[]
    for i in range(len(dict)):
        if dict[i][1]<l[len(l)-1]:
            l3.append(dict[i][1])
        else:
            pass
    l3=sorted(l3)
    print("hello")
    print(l3)
    print(dict)

    for i in l3:
        print(i+1)
        print(len(dict))
        for j in range(len(dict)):
            
            if (dict[j][1]==i):
            
                l.append(dict[j][2]+l[len(l)-1])
        
                dict.pop(j)
                l3.pop(j)
                
                test(dict,l)
       
            else:
                break
        print(l)       
    
    
    return dict
                  
            
print(test(dict,l))
print(dict)
print(l)

'''for i in l3:
    for j in range(len(dict)):
        
        if (dict[j][1]==i):
            l.append(dict[j][2])
            print(i)
            if dict[j][1]<l[len(l)-1]:
                l3.append(dict[j][1])
    
print(l)'''
