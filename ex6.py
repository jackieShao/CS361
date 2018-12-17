def is_prime(n):
    if n >1:
        for x in range(2, n):
            if (n % x) ==0:
                print(False)
                break
        else:
            print(True)
    else:
        print(False)
is_prime(6)


def is_prime2(n):
    if n == 2 or n == 3:
        print(True)
    if n %2 == 0 or n % 3 == 0:
        print(False)
    i = 5
    x = 2
    sqr = int(n ** 0.5) + 1
    while i <= sqr:
        if n % i ==0:
            print(False)
        i = i + x
        x = 6 - x
        print(True)
is_prime2(6)


def prime_num(n):
    prime_list =[]
    for num in range (1,n+1):
        if all(num%i!=0 for i in range(2, num)):
               prime_list.append(num)
    print(prime_list)
prime_num(10)


def first_n(n):
    prime_list=[]
    i = 2
    while len(prime_list) != n:
        for num in range(2, 1//2+1):
            if i % num ==0:
                break
        else:
            prime_list.append(i)
        i = i +1
    print(prime_list)
first_n(10)

