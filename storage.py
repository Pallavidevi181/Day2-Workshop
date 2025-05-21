storage=[]
n=int(input("enter the no. of items: "))
for i in range(n):
    item=str(input("enter the items: "))
    storage.append(item)
print("list of items",storage)
brought=str(input("customer brought: "))
if brought in storage: 
    storage.remove(brought)
else:
    print("item not available")
print("list after purchase",storage)