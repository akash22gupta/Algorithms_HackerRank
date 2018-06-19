n,k = map(int,input().split())

a = list(map(int,input().split()))

b = int(input())
j=0
sum1=0
sum2=0

for i in a:
    if j!=k:
        sum1+=i
    j+=1
    sum2+=i
sum1=sum1/2
sum2=sum2/2
if b == sum1:
    print('Bon Appetit')
else:
    print(int(sum2-sum1))
        
