import random
import output as OUT

def optimization(B, A, L, _next, n):
    # Инициализируем необходимые матрицы
    DEL = [[0] * n for i in range(n)]
    DL = [[0] * n for i in range(n)]
    O = [[0] * n for i in range(n)]
    Bo = B
    
    dc = 10000 # Шаг

    m0 = float('inf')
    Oprev = float('inf')

    cycles = 0
    
    while True: # Базовый цикл
        Oprev = m0
        cycles += 1
        
        for i in range(n):
            for j in range(n):
                if Bo[i][j] != 0:
                    L = 200 * 8
                    
                    for x in range(n):
                        for y in range(n):
                            
                            if Bo[x][y] != 0:
                                bm = Bo[x][y]
                                am = A[x][y]
                                
                                if (i == x) and (j == y):
                                    bm += dc;
                                    
                                DEL[x][y] = L / (bm - am)
                    for x in range(1, n+1):
                        for y in range(1, n+1):
                            _sum = 0
                            
                            if x == y:
                                _sum = DEL[x-1][y-1]
                            else:
                                k = x
                                nextK = y
                                
                                while (k != y):
                                    nextK = _next[k-1][y-1]
                                    _sum += DEL[k-1][int(nextK-1)]
                                    k = nextK                    
                                    
                            DL[x-1][y-1] = _sum

                    Topt = 0.05
                    sumO = 0
                    for x in range(n):
                        for y in range(n):
                            sumO += (DL[x][y] - Topt) * (DL[x][y] - Topt)
                    O[i][j] = sumO
        
        mi = 0
        mj = 0
        m0 = O[mi][mj]
        
        for i in range(n):
            for j in range(n):
                if O[i][j] != 0:
                    tmp = O[i][j]
                    if tmp < m0:
                        m0 = tmp
                        mi = i
                        mj = j
        b = Bo[mi][mj]
        Bo[mi][mj] = b + dc

        if m0 < Oprev:
            pass
        else:
            break
        
    print("Оптимизация выполнена.") # Спорное утверждение

    print("DEL: ")
    OUT.printMatrix(DEL, n)
    print("DL: ")
    OUT.printMatrix(DL, n)
    print("O: ")
    OUT.printMatrix(DEL, n)
    print("Bo: ")
    OUT.printMatrix(DEL, n)

    
