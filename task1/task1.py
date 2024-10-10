import sys

n,m=int(sys.argv[1]), int(sys.argv[2])
if n>0 or m>0:  
    loop=[1]#массив для чисел
    last_num=0 #последнее число массива
    final=[]
    template=[i for i in range(1,n+1)] #массив значений числа
    while last_num!=1:
        for i in range(0,m-1):
            loop.append(loop[i]+1 if loop[i]<=n-1 else loop[i]-n+1)
        last_num=loop[len(loop)-1]
        final.append(loop[0])
        loop=[last_num]
        
    print(''.join([str(x) for x in final])) 
        
else:
    print('Введите положительные числа')
