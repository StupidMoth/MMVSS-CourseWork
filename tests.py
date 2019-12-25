def printMatrix(M, n):
    print('\n  ', end = '')
    for i in range(n):
        print('  {0:2.0f}  '.format(i+1), end = '')
    print()
    for i in range(n):
        print('{0:2.0f} '.format(i+1), end = '')
        for j in range(n):
            print('{0:5.2f}'.format(M[i][j]), end = ' ')
        print()
    print()

def printArr(A):
    print()
    for i in range(len(A)):
        print('{0:6.0f}'.format(i+1), end = ' ')
    print()
    for i in range(len(A)):
        print('{0:6.2f}'.format(A[i]) if A[i] != None else 'None', end = ' ')
    print('\n')
