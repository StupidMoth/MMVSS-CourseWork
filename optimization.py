import random

def optimization(B, A, L, n):
    # Инициализируем необходимые матрицы
    DEL = [[0] * n for i in range(n)]
    DL = [[0] * n for i in range(n)]
    Bo = B

    # НЕОБХОДИМО ПОНЯТЬ, ЧТО ТАКОЕ next МАТРИЦА
    # ВРЕМЕННО ЗАПОЛНИМ СЛУЧАЙНЫМИ ВЕЛИЧИНАМИ ОТ 1 до 20
    _next = []
    for i in range(n):
        row = []
        for j in range(n):
            value = random.randint(1, 20)
            row.append(value)
        _next.append(row)
    # И СО СЛУЧАЙНЫМИ ЗНАЧЕНИЯМИ ЭТО, ПОХОЖЕ, НЕ РАБОТАЕТ
    
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
                    o[i][j] = sumO
                    
        mi = 0
        mj = 0
        m0 = o[mi][mj]
        
        for i in range(n):
            for j in range(n):
                if o[i][j] != 0:
                    tmp = o[i][j]
                    if tmp < m0:
                        m0 = tmp
                        mi = i
                        mj = j
        b = bo[mi][mj]
        bo[mi][mj] = b + dc
        
        if m0 < Oprev:
            pass
        else:
            break
        
    print("Оптимизация выполнена.") # Спорное утверждение
