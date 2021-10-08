
# Pass By value 
# Pass By Reference 
# python is different

def update1(x):
    x = 8
    print("x ",x)

a =10
update1(a)
print("a ",a)

##############################
##############################
print("################################")
print("################################")
print("################################")

def update2(lst):
    
    print(id(lst))

    lst[1] = 25
    print(id(lst))
    print("x ",lst)

lst = [10,20,30]
update2(lst)
print("lst ",lst)

