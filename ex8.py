a = [11, 231, 231, 2312]
print('original a',a)

b = a
b[1] = 0
print('b changed b',b)
print('b changed a',a)

c = a[:]
print('original c',c)
c[2] = 10
print('c changed c',c)
print('c changed a',a)


def set_first_elem_to_zero(list):
    a[0] = 0
    print(a)
set_first_elem_to_zero(a)
