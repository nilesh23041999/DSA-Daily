## factorial problem

def fact(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * fact(num-1) 
    
    
print(fact(5))



#                  factorial(5)
#                 /            \
#        factorial(4)           *
#       /           \         /   
#  factorial(3)      *      4
#       /           \      
#  factorial(2)      * 
#       /           \
#  factorial(1)      2



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(10):
    print(fibonacci(i))