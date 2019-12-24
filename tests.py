def printMatrix(M, n):
    print('\n  ', end = '')
    for i in range(n):
        print('{0:4.0f} '.format(i+1), end = ' ')
    print()
    for i in range(n):
        print('{0:2.0f} '.format(i+1), end = '')
        for j in range(n):
            print('{0:5.2f}'.format(M[i][j]), end = ' ')
        print()
    print()
