def perm(N,M=-1,prefix=None):
    prefix = prefix or []
    M=N if (M==-1) else M
    if M==0:
        print(prefix)
        return
    for num in range(M):
        prefix.append(num)
        perm(N,M-1,prefix)
        prefix.pop()    


perm(2,3)   
print("end")