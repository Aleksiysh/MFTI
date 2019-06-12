def generate_numbers(N: int, M: int, prefix=None):
    """ генерирует все числа в N ричной системе с лидирующими нулями
        длины M
    """
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

def gen_string(M, prefix=""):
    """ Генерирует все двоичные числа длины M:int
    """
    if M == 0:
        print(*prefix)
    else:
        gen_string(M-1, prefix+"0")
        gen_string(M-1, prefix+"1")

def gen_string_dict(M, dict="", prefix=""):
    """     Генерирует слова длины M:int
        из набора символов dict:string
    """
    if M == 0:
        print(*prefix,sep="")
    else:
        for a in dict:
            gen_string_dict(M-1,dict,prefix+a)

def gen_string_for(M, prefix=""):
    if M == 0:
        print(*prefix)
    else:
        for ch in "0", "1":
            gen_string_for(M-1, prefix+ch)

def generate_permutations(N: int, M: int = -1, prefix=None):
    """ Генерирует все  перестановки N чисел
        в M позициях, начиная с prefix
    """
    # if M==-1 :
    #     M=N     # по умолчанию N чисел в M позициях
    M = N if (M == -1 or M > N) else M  # по умолчанию N чисел в M позициях

    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

def find(x, a):
    """функция ищет x в а и возвращает True, если такой есть
        иначе False
    """
    for i in a:
        if i == x:
            return True
    return False

# print("*"*15,"\n",generate_numbers.__doc__)
# a,b= int(input()),int(input())
# generate_numbers(a,b)
# print("*"*15,"\n",gen_string.__doc__)
# a=int(input())    
# gen_string(a)
# print("*"*15,"\n",gen_string_for.__doc__)
# gen_string(a)
# gen_string_for(a)
# print("*"*15,"\n",generate_permutations.__doc__)
# a,b= int(input()),int(input())    
# generate_permutations(a,b)
print("*"*15,"\n",gen_string_dict.__doc__)
a,b= int(input()),input()
gen_string_dict(a,b)
