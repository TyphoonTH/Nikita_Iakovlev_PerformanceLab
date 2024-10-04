import sys

n,m=int(sys.argv[1]), int(sys.argv[2])
loop=[i for i in range(1, n+1)] #круговой массив
final=[1] #массив для хранения последних чисел
last_num=m-1 #последнее число массива
while last_num!=0:
    final.append(loop[last_num])
    last_num=last_num+m-1
    if last_num>=n-1:
        last_num-=n
print(''.join([str(x) for x in final]))   
