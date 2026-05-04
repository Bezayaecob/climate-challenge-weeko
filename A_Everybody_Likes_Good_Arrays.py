
t= int(input())
for _ in range(t):
    n= int(input())
    arr= list(map(int , input().split()))
    temp=0
    for i in range(arr):
        if arr[i]%2==0 and arr[i+1]%2==1:
            temp= arr[i]*arr[i+1]
            arr.insert(temp, arr[i])
    return arr



    



