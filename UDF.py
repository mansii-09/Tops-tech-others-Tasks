def oddeven(a):
    if a %2 == 0:
        print(a, "Is Even..")
    else :
        print(a, "Is Odd..")

def maxoftwo(a, b):
    if a> b:
        print(a, "Is max..")
    else:
        print(b, "Is max..")

def maxofthree(a, b,c):
    if a> b and a >c:
        print(a, "Is max..")
    elif b > a and b > c:
        print("b, Is max")
    else:
        print(c, "Is max..")


def prime(n):
    if n % 2 != 0:
        for i in range(3, (n/2) + 1,2):
            if n % i == 0:
                print(n, "Is not an prime...")
                break
        else :
            print(n, "Is prime")
    else :
        print(n, "Is Not an prime")

def febonacci(n):
    a, b=0,1
    prime(a)
    while b <= n:
        print(b)
        a,b=b, a+ b