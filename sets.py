#1 Filtering duplicates out of other collections
list3=[1,2,3,4,4,4,5,6,6,6]
list3=list(set(list3))
print(list3)

#2 Isolating difference in 2 iterable objects
list1=[1,2,3,4,5]
list2=[1,2,4,6,7]

ld=list(set(list1)-set(list2))
print(ld)

#3 Order-neutral equality
a=[1,2,3]
b=[1,3,2]
if a==b:
    print("List are equal")
else:
    print("Lists not equal")

if set(a)==set(b):
    print("Sets are not order sensitive")
else:
    print("The lists converted weren't Equal")


