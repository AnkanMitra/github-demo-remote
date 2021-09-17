#add imple
def add(x,y):
    return x+y    
#subs imple
def subtract(x,y):
    return x-y      #on master branch
#multiply imple
def multiply(x,y):
    return x*y      #on Bug456 branch
#multiply imple
def divide(x,y):
    if y==0:
        return DIVIDE_BY_ZERO_ERROR
    else:
        return x/y      #On master branch

