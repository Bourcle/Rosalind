#Wascally Wabbits
#Fibonacci

#basic function of Fibonacci
def fib(n) : 
    if n == 1 or n == 2:
        return 1
    else : 
        return fib(n-1) + fib(n-2)
    

def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)

#n-2 means born kids, n-1이 the number of rabbits on ferfile


n = 33
k = 4

result = rabbit_pairs(n, k)
print(result)

