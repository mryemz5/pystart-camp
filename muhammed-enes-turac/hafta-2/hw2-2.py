"""
number=int(input("enter a number"))
for num in range(1,11):
    x=number*num

    print(x)
"""
x=1
sum=0
s=0
while x>0:
    k=(input("enter a number"))
    if k=="q":
        break
    elif not k.isdigit():
        print("invalid input")
        continue
    number=int(k)
    sum=sum+number
    s+=1
average=sum/s
print(sum)
print(average)












