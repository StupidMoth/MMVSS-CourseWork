def calcNodeIntensity(N, y0, n):
    y = [y0]
    for i in range(1, n):
        y.append(round(N[i] * y0))
    return y
