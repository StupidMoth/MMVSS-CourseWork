# Интенсивность исходящего трафика от каждого из узлов сети:
# y[i]=N[i]*y[0], i = 1..n
def calcNodeIntensity(N, y0, n):
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
