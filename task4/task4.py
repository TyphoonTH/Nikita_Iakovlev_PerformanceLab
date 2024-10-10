def median(arr): #функция вычисления медианы
    srtd=sorted(arr)
    if len(arr)%2==0:
        med=round((srtd[len(arr)//2-1]+srtd[len(arr)//2])/2)
    else:
        med=srtd[len(arr)//2] 
    return med       

nums=[]
with open(input(),"r") as numbers:
    for line in numbers:
        nums.append(int(line))
res=0 #полученная сумма шагов
for i in nums:
    res+=abs(i-median(nums))
print(res)  
