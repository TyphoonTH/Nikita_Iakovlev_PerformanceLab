filename=input()
nums=[]
with open(filename,"r") as numbers:
    for line in numbers:
        nums.append(int(line))
sum=0 #сумма всех значений
res=0 #полученная сумма шагов
for i in nums:
    sum+=i
goal=round(sum/len(nums))
for i in nums:
    res+=(abs(goal-i))
print(res)    
