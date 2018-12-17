numFound = 0;
x = 11;
while (numFound < 20):
    if (x % 5 == 0) & (x % 7 == 0) & (x % 11 == 0):
        print(x)
        numFound += 1
    x += 1
