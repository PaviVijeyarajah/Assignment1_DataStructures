import time

product_data = []

with open('product_data.txt') as file:
    lines = [i.strip() for i in file]
for i in range(len(lines)):
    product_data.append(lines[i].split(","))
file.close()

     
def Insert():
    id=input("What is the id of the new product: ")
    name=input("What is the name of the new product: ")
    price=input("What is the price of the new product: ")
    cat=input("What category does the new product belong: ")
    product=[id," "+name," "+price," "+cat]
    product_data.append(product)


def Update(value):
    for i in range(len(product_data)):
        if product_data[i][0] == value:
            num=i
    id=input("What is the id of the modified product: ")
    name=input("What is the name of the modified product: ")
    price=input("What is the price of the modified product: ")
    cat=input("What category does the modified product belong: ")
    product=[id," "+name," "+price," "+cat]
    product_data[num]= product 


def Delete(value):
    for i in range(len(product_data)):
        if product_data[i][0] == value:
            num=i
    product_data.pop(num)


def Search(value):
    for i in range(len(product_data)):
        if product_data[i][0] == value:
            return print("Product id found", product_data[i][0])
        if product_data[i][1] == value:
            return print("Product name found", product_data[i][1])
    return print("Not in the database")


def bubbleSort(list):
    n = len(list)
    for i in range(n):
        swapped=False
        for j in range(0, n-i-1):
            a=float(list[j][2])
            b=float(list[j+1][2])
            if a>b:
                swapped=True
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
            print(product_data)
            print()
        if not swapped:
            return
    

while True:
    UI=int(input("What operation would you like to perform (Type number chosen)\n0. Product List\n1. Insert\n2. Update\n3. Delete\n4. Search\n5. Sort\n"))
    if UI==0:
        print()
        print(product_data)
        print()
    if UI==1:
        Insert()
        print()
    if UI==2:
        value=input("Enter the product id of the item you would like to update: ")
        Update(value)
        print()
    if UI==3:
        value=input("Enter the product id of the item you would like to delete:  ")
        Delete(value)
        print()
    if UI==4:
        choice=int(input("Would you like to search by (Type number) \n1. ID\n2. Name\n"))
        if choice==1:
            value=input("Enter the id you would like to search: ")
            Search(value)
            print()
        if choice==2:
            value=input("Enter the name you would like to search: ")
            Search(" "+value)
            print()
    if UI==5:
        break

 
while True:
    #Average Case
    start1=time.time()
    bubbleSort(product_data)
    end1=time.time()

    #Best Case
    start2=time.time()
    bubbleSort(product_data)
    end2=time.time()

    #Worst Case
    worstSort=product_data[::-1]
    start3=time.time()
    bubbleSort(worstSort)
    end3=time.time()

    print("Average case time taken: ",end1-start1)
    print("Best case time taken: ",end2-start2)
    print("Worst case time taken: ",end3-start3)
    break