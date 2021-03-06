import math

# 1. Интенсивность исходящего трафика от каждого из узлов сети:
# y[i]=N[i]*y[0], i = 1..n
def calcTrafficNodeIntensity(N, y0, n):
    y = []
    for i in range(n):
        y.append(round(N[i] * y0))
    return y

# 2. Коэффициенты распределения трафика по направлениям связи:
# k[i][j] = y[i]/sum(y), j = 1..n, i = 1..n
def calcTrafficRatio(y, n):
    k = []
    for i in range(n):
        row = []
        for j in range(n):
            value = y[j]/sum(y)
            row.append(value)
        k.append(row)
    return k

# 3. Матрица интенсивностей трафика в направлениях связи
# Y = |y[i][j]|, i = 1..n, j = 1..n
# y[i][j] = k[i][j] * y[i], i = 1..n, j = 1..n
def calcTrafficMatrixIntensity(k, y, n):
    Y = []
    for i in range(n):
        row = []
        for j in range(n):
            value = k[i][j]*y[i]
            row.append(value)
        Y.append(row)
    return Y

# 4. Матрица кратчайших маршрутов между вершинами графа
# Алгоритм Флойда
# Принимает матрицу смежности как аргумент
# Элемент матрицы смежности может быть None
def calcByFloydsAlgorithm(R, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                R[i][j] = minNone(R[i][j], sumNone(R[i][k], R[k][j]))
    return R

sumNone = lambda a, b: a + b if (a != None and b != None) else None

None2Number = lambda a: a if (a != None) else float('inf')

def minNone(a, b):
    a = None2Number(a)
    b = None2Number(b)
    return min(a, b)    

# 4.5. Матрица восстановленных путей
# По S и D

ar3 = [[0] * 20 for i in range(20)]
ar2 = [[0] * 20 for i in range(20)]
ar1 = [[0] * 20 for i in range(20)]

def calcPath(_ar1, _ar2, n):
    ar1 = _ar1
    ar2 = _ar2
    for i in range(n):
        for j in range(n):
            calcDeykstra(i, j)
    return ar1

def calcDeykstra(k, l):
    for j in range(20):
        if ar1[k][j] == ((l+1)):
            ar3[k][l] += ar2[k][j]
        if ar1[l][j] == ((k+1)):
            ar3[k][l] += ar2[k][j]

# 5. Матрица интенсивностей нагрузок на линии связи
# Правильно ли я считаю?!!
# j = 1..n, i = 1..n
def calcIntensity(Y, R, n):
    Ytilda = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(Y[i][j])
            else:
                row.append(0)
        Ytilda.append(row)
    return Ytilda            

# 6. Матрица потоков
# j = 1..n, i = 1..n
def calcStreamMatrix(Ytilda, q, n):
    V = [[0] * 20 for i in range(20)]

    p0 = 1 - q / 100
    v = 0
    p = 1
    for i in range(n):
        for j in range(n):
            while p0 <= p:
                #print(str(p0) + " <= " + str(p))
                v += 1
                p = fErlang(Ytilda[i][j], v, n)
            V[i][j] = v - 1
            p = 1
            v = 0
    return V

def fErlang(yt, v, n):
    p = 1
    for i in range(v):
        if yt != 0:
            p = 1 + p * i / yt    # Деление на 0
        else:
            return 0
    return 1 / p

# 7. Интенсивность трафика ПД в линиях связи
# j = 1..n, i = 1..n
def calcTrafficLineIntensity(V, Codec, n):
    if Codec == 'G.711':
        a0 = 85600 # бит/с
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(V[i][j]*a0)
        A.append(row)
    return A    
    
# 8. Пропускнаяспособность линий связи
# j = 1..n, i = 1..n
def calcLinesCapacity(A, L, T0, n):
    B = []
    for i in range(n):
        row = []
        for j in range(n):
            if (A[i][j] != 0):
                row.append(A[i][j]+(L*8/T0))
            else:
                row.append(A[i][j])
        B.append(row)
    return B    
