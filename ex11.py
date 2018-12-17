List = [2, 4, 6, 8, 10]

def iterative(L):
    if len(L) == 0:
        return 0
    product = 1
    for elements in L:
        product = product * elements
    return product

def recurs(L):
    if len(L) == 0:
        return 0
    if len(L) == 1:
        return L[0]
    else:
        return recurs([L[0]]) * recurs(L[1:])
print('The product is', iterative(List))
print('Recursively, the product is', recurs(List))
