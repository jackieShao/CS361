L=[1, 3, 5, 7, 9, 131, 123132, 1023921]

def list_print(list):
    for items in list:
        print(items)
list_print(L)
print()


def reverse_print(list):
    for items in reversed(list):
        print(items)
reverse_print(L)
print()


def len(list):
    elements = 0
    for num in list:
        elements = elements + 1
    print('You have', elements, 'elements.')
len(L)
