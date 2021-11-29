sum=0
n=int(input("Enter number of student:"))
for i in range(n):
    s=int(input("Enter number of subjects:"))
    for j in range(s):
        print("enter the marks for student")
        m=int(input())
        sum=sum+m
        avg=sum/s
    print("Average marks is:", avg)
    temp1 = sum
    sum=sum-temp1
