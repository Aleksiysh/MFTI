#*******************************************************************
def fib(n):
    """Число фибоначи рекурсия
    """
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

def fib1(n):
    """Число фибоначи динамическое
    """
    fib=[0,1] + [0]*(n-1)
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]   
    return fib[n]

def count_trajectories(N,allowed:list):
    """ +1 +2 +3
    """
    k=[0,1,int(allowed[2])]+[0]*(N-3)
    for i in range(3,N+1):
        if allowed[i]:
            k[i]=k[i-1]+k[i-2]+k[i-3]
    return k[N]  
#-------------------------------------------    
def count_min_cost(N,price:list):
    """ минимальная стоимость 
        стоимость пути
        cost 
        шаги +1 +2
    """
    C=[float("-inf"),price[1],price[2]]+ [0]*(N-2)
    for i in range(3,N+1):
        C[i]=price[i]+ min(C[i-1],C[i-2])
    return C[N]    

#********************************************************************    
# for i in range(30):
#     print("begin ",i)
#     print(fib(i))
#     print(fib1(i))

    #   A[i][j] -> A[i*M+j] # Линеаризация массива

N=2
M=3

A=[[0]*M for i in range(N)] # N строк M столбцов
print ("aa")
print(A[0]==A[1])
print(A[0] is A[1])

B=[[0]*M]*N     # одна размноженная строка
print ("b")
print(B[0]==B[1])
print(B[0] is B[1])

    