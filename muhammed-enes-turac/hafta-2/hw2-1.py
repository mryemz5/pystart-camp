kg=int(input("enter a kg"))
km=int(input("enter a distance"))
sk=input("do you want speed cargo: yes/no")
price=0
if kg>0 and kg<=2:
    price=50
elif kg>2 and kg<=5:
    price=80
elif kg>5 and kg<=10:
    price=120
elif kg>10:
    price=120+((kg-10)*10)    
if km>500:
    price=price+(price/5)
if sk=="yes":
    price=(price*1.5)
if km==0 or kg==0:
    print("invalid weight or invalid distance")
else:
 print(kg)
 print(km)
 print(sk)
 print(price)