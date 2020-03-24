import math

def cached(func):
    previous_args = [None, None]
    file = open("result.txt",'w')
    def wrapper(*args, **kwargs):
        if(previous_args[0] == args):
            returned = previous_args[1]
            file.write(str(returned))
            return returned
        else:
            previous_args.clear()
            previous_args.append(args)
            previous_args.append(func(*args, **kwargs))
            returned = previous_args[1]
            file.write('\n' + str(returned))
            return returned
    return wrapper

@cached
def add(a, b):
     return  a + b

@cached 
def plusandpow(a, b, n):
    return math.pow(a + b, n)     


add(5,10)
plusandpow(3,2,3)