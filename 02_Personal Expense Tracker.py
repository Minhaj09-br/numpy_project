import numpy as np 

arr=[]
porduct=int(input("how product you in daily by: "))

for i in range(porduct):
    product=int(input(f"all product  price{i+1}: "))
    arr.append(product)
exp=np.array(arr)


total_spending=np.sum(exp)
print(f"Total spending:{total_spending}")
average=np.mean(exp)
print(f"Average of all:{average}")
highest_pro=np.max(exp)
print(f"Highest rated pro:{highest_pro}")
lowest_pro=np.min(exp)
print(f"lowest rated pro:{lowest_pro}")
shory=np.sort(exp)
print(f"all product price:{shory}")
most_ex=np.argmax(shory)
print(f"most expensive product posison:{most_ex}")
count=np.count_nonzero(exp>100)
print(f"greater than 100:{count}")
filtaring=exp[exp>200]
print(f"product greater then 200:{filtaring}")

