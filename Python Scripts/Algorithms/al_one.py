list_one = [125,100,67,150,75,122]

list_max_1 = 0
list_max_2 = 0
idx1 = 0
idx2 = 0
f1 =[]
f2=[]
for k in range(2):
    for i in range(0,len(list_one)):
        for j in range(i+2,len(list_one)):
            addition = list_one[i] + list_one[j]
            if addition > list_max_1:
                list_max_1 = addition
                idx1 = list_one.index(list_one[i])
                idx2 = list_one.index(list_one[j])
    print(list_one)

    list_max_1 = 0
    if k ==0:
        f1.append(list_one[idx1])    
        f1.append(list_one[idx2]) 
        list_one[idx1] = 0  
        list_one[idx2] = 0  
    else:
        if k==1:
            f2.append(list_one[idx1])    
            f2.append(list_one[idx2]) 
 


print("List one",list_one)

print("The first set of fights has the prizes", f1)
print("The second set of fights has the prizes", f2)
        
        

        

