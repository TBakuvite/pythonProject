def myfunc(a,b,c=0,d=0,e=0):
    #Returns 5% of the sum of a and b
    return sum((a,b,c,d,e))*0.05

print(myfunc(1,4,5,9,10))

def myfunc(*args):
    return sum(args)*0.05

print(myfunc(40,60,67,89,100,234))

def myfunc(**kwargs):
    print(kwargs)





