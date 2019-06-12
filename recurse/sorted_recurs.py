def merge_sort(A):
    """Сортировка слиянием
    """
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]

def merge(A: list, B: list):
    """слияние двух упорядоченных массивов A и B
        Возвращает один упорядоченный массив 
    """
    C = [0]*(len(A)+len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1
        #можно через условие проверить какой массив кончился
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

def hoar_sort(A):   # Быстрая сортировка Тони Хоара
    """ Сортировка Хоара
    """
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)

    hoar_sort(L)
    hoar_sort(R)

    k = 0
    for x in L+M+R:
        A[k] = x
        k += 1

def check_sorted(A, ascending=True):
    """ Проверка массива на сортированность
        за O(len(A))
    """
    flag = True
    s = 2*int(ascending)-1
    for i in range(len(A)-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag

def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left+right)/2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left+right)/2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


A = [4, 6, 8, 9, 3, 6, 9, 4, 6, 8, 0, 4, 3, 6, 8]
print(check_sorted(A))
hoar_sort(A)
print(*A)
print(check_sorted(A))
print(check_sorted([4, 3, 2, 1]))
