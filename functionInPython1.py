


def greet() :
    print("Hello")
    print("Good Morning")

def add(x,y):
    c = x+y
    return c

def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

greet()
result1 = add(5,4)    
result2,result3 = add_sub(5,4)  
print("sum 5,4: ",result1)
print("add_sub 5,4: ",result2,result3)