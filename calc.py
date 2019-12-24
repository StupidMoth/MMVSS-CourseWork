# Интенсивность исходящего трафика от каждого из узлов сети:
# y[i]=N[i]*y[0], i = 1..n
def calcTrafficNodeIntensity(N, y0, n):
    y = [y0]
    for i in range(1, n):
        y.append(round(N[i] * y0))
    return y

# Коэффициенты распределения трафика по направлениям связи:
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

# Матрица интенсивностей трафика в направлениях связи
# Y = |y[i][j]|, i = 1..n, j = 1..n
# y[i][j] = k[i][j] * y[i], i = 1..n, j = 1..n
def calcTrafficMatrixIntensity(k, y, n):
    Y = []
    for i in range(n):
        row = []
        for j in range(n):
            value = abs(k[i][j]*y[i])
            row.append(value)
        Y.append(row)
    return Y

#Матрица кратчайших маршрутов между вершинами графа
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

None2Number = lambda a: a if (a != None) else -1

def minNone(a, b):
    a = None2Number(a)
    b = None2Number(b)
    return min(a, b)    
        



    
