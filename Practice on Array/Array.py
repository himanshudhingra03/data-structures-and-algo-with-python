#Implementation of array


#initializing of array
a=[]

#Inserting values 
n=int(input("Enter the number of values You want to enter"))
for i in range(n):
    i=int(input("Enter values"))
    a.append(i)
print(a)    

# Traversal of array
b=[1,2,3,4,5,6,7]
for i in b:
    print(i)

#inserting values at desried positions

b.insert(0,5)
print(b)

#Removing values using pop function

b.pop()
print(b)

#Using remove function to remove values from desired place

b.remove(2)
print(b)


#Reverse the array

b.reverse()
print(b)

#Sort the array using in-built function

b.sort()
print(b)

