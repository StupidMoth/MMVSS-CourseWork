import calculation as C
import optimization as O
import output as OUT

'''
    1. Как правильно считать Y~?
    
    2. Деление на 0 при вычислении матрицы потоков?

    3. Как находить значения для транспонированной матрицы
    восстановления путей (Флойд)?
    
    4. Оптимизация не работает, пока нет транспонированной матрицы
    восстановления путей.
    
    5. Пояснительная записка не написана.
'''

def main():
    
    # --- Входные данные:
    
    # Матрица расстояний
    # None - нет пути
    D = [[0, 24.33963418, None, None, 57.96404481, 63.28330636, 92.04159379, 97.41273522, 34.13305879, 8.501392603, None, None, 43.92023683, 13.11889291, None, 94.92898583, 40.45057893, 30.26080728, 84.720999, None],
         [24.33963418, 0, None, 73.85107875, None, 72.56256938, 92.0316875, None, 14.01893497, 65.85347056, 67.89705157, 54.96413112, None, None, 85.38839221, 91.94399714, None, None, None, None],
         [None, None, 0, 49.04459119, 40.96282125, None, 53.19741368, None, 39.55920339, None, 75.43881536, None, 61.22687459, None, 22.31400609, None, None, 19.07089353, 96.94798589, 68.55219007],
         [None, 73.85107875, 49.04459119, 0, 61.08250022, None, 4.982894659, 29.04109359, 78.52806449, None, 60.23363471, 43.33114028, None, 39.18160796, 87.18847632, None, None, None, None, 48.74228835],
         [57.96404481, None, 40.96282125, 61.08250022, 0, 10.12077928, 32.69773126, None, 61.20582223, None, None, 61.52334809, 57.69343972, 47.02911973, 13.95421624, None, 76.08047128, None, None, None],
         [63.28330636, 72.56256938, None, None, 10.12077928, 0, 86.94083095, 94.44400668, 42.9277122, None, None, 99.59403872, 97.64439464, None, 90.90544581, 19.80754733, None, 81.85216784, None, 33.2095325],
         [92.04159379, 92.0316875, 53.19741368, 4.982894659, 32.69773126, 86.94083095, 0, 0.494223833, None, None, 2.063733339, None, 36.42662168, None, 58.00264478, None, 79.68242764, 42.0504868, None, 42.74333119],
         [97.41273522, None, None, 29.04109359, None, 94.44400668, 0.494223833, 0, None, 1.947158575, None, None, 48.47936034, None, 82.70263076, None, None, 28.87930274, None, 81.40396476],
         [34.13305879, 14.01893497, 39.55920339, 78.52806449, 61.20582223, 42.9277122, None, None, 0, 81.9386065, None, None, 74.06826615, None, 42.4292624, None, 44.19479966, 65.73415399, 48.50550294, None],
         [8.501392603, 65.85347056, None, None, None, None, None, 1.947158575, 81.9386065, 0, 15.85895419, 57.43348002, None, None, None, None, 88.36366534, None, 95.32405734, None],
         [None, 67.89705157, 75.43881536, 60.23363471, None, None, 2.063733339, None, None, 15.85895419, 0, None, 3.607875109, None, None, 71.37306333, None, None, 38.88342977, 79.96090055],
         [None, 54.96413112, None, 43.33114028, 61.52334809, 99.59403872, None, None, None, 57.43348002, None, 0, None, None, 10.83549857, 77.0598352, None, None, None, None],
         [43.92023683, None, 61.22687459, None, 57.69343972, 97.64439464, 36.42662168, 48.47936034, 74.06826615, None, 3.607875109, None, 0, 18.74819398, 5.097728968, None, 5.193954706, None, 54.12440896, 19.87610459],
         [13.11889291, None, None, 39.18160796, 47.02911973, None, None, None, None, None, None, None, 18.74819398, 0, 16.07987285, None, 78.85996699, None, 43.64811778, None],
         [None, 85.38839221, 22.31400609, 87.18847632, 13.95421624, 90.90544581, 58.00264478, 82.70263076, 42.4292624, None, None, 10.83549857, 5.097728968, 16.07987285, 0, None, None, None, None, 96.07403874],
         [94.92898583, 91.94399714, None, None, None, 19.80754733, None, None, None, None, 71.37306333, 77.0598352, None, None, None, 0, 28.11259627, 96.32515311, 31.03093505, 38.13814521],
         [40.45057893, None, None, None, 76.08047128, None, 79.68242764, None, 44.19479966, 88.36366534, None, None, 5.193954706, 78.85996699, None, 28.11259627, 0, None, None, None],
         [30.26080728, None, 19.07089353, None, None, 81.85216784, 42.0504868, 28.87930274, 65.73415399, None, None, None, None, None, None, 96.32515311, None, 0, 51.32429004, None],
         [84.720999, None, 96.94798589, None, None, None, None, None, 48.50550294, 95.32405734, 38.88342977, None, 54.12440896, 43.64811778, None, 31.03093505, None, 51.32429004, 0, None],
         [None, None, 68.55219007, 48.74228835, None, 33.2095325, 42.74333119, 81.40396476, None, None, 79.96090055, None, 19.87610459, None, 96.07403874, 38.13814521, None, None, None, 0]]
    # Захадкодить матрицу смежностей
    #Смежности почему то Y
    # В восстановление путей передавать ее и D
    # Проверить на точность переноса алгоритма дейкстры
    # Матрицу посчитать в екселе
    
    # Количество узлов связи
    n = 20
    
    # Длина пакета
    L = 200 # байт

    # Codec
    Codec = 'G.711'

    # Интенсивность  удельной  абонентской нагрузки
    y0 = 0.1 # Эрл


    # --- Требования к качеству обслуживания:
    
    # Начальное требование к величине задержки T0
    T0 = 0.1 # 100ms = 0.1s
    
    # Доля вызовов, обслуженных с гарантированным качеством 
    q = 98 # 98%
    
    # Распределение абонентов по узлам связи (количество)
    N = [7916, 9084, 7295, 6958, 8765, 
         4897, 9029, 9484, 7254, 2479, 
         3384, 4371, 9992, 7318, 5953,
         1647, 5455, 7300, 4146, 5903]


    # --- Рассчеты:
    
    # Интенсивность исходящего трафика от каждого из узлов сети:
    y = C.calcTrafficNodeIntensity(N, y0, n)
    print("1. Интенсивность исходящего трафика от каждого из узлов сети была вычислена.")
    #OUT.printArr(y)
    
    # Коэффициенты распределения трафика по направлениям связи:
    k = C.calcTrafficRatio(y, n)
    print("2. Коэффициенты распределения трафика по направлениям связи были вычислены.")
    #OUT.printMatrix(k, n)
    
    # Матрица интенсивностей трафика в направлениях связи:
    Y = C.calcTrafficMatrixIntensity(k, y, n)
    print("3. Матрица интенсивностей трафика в направлениях связи была вычислена:")
    #OUT.printMatrix(Y, n)
    
    # Матрица кратчайших маршрутов между вершинами графа:
    R = C.calcByFloydsAlgorithm(D, n)
    print("4. Матрица кратчайших маршрутов между вершинами графа была вычислена:")
    #OUT.printMatrix(D, n)

    # --- Мы здесь

    _next = C.calcPath(D, Y, n)
    #OUT.printMatrix(_next, n)
    print(_next)




    # Матрица интенсивностей нагрузок на линии связи:
    Ytilda = C.calcIntensity(Y, R, n)
    print("5. Матрица интенсивностей нагрузок на линии связи была вычислена:")

    #Ytilda = k # ВРЕМЕННАЯ ЗАГЛУШКА, ПОКА НЕ БУДЕТ ДАНА Y~
    
    OUT.printMatrix(Ytilda, n)

    # Матрица потоков:
    #print("6. Матрица потоков была вычислена:")    
    #V = C.calcStreamMatrix(Ytilda, q, n)
    #OUT.printMatrix(V, n)

    # Интенсивность трафика ПД в линиях связи:
    #print("7. Интенсивность трафика ПД в линиях связи была вычислена:")
    #A = C.calcTrafficLineIntensity(V, Codec, n)
    #OUT.printMatrix(A, n)

    # Пропускная способность линий связи:
    #print("8. Пропускная способность линий связи была вычислена:")
    #B = C.calcLinesCapacity(A, L, T0, n)
    #OUT.printMatrix(B, n)


    # --- Оптимизация:
    #print("9. Оптимизация пропускной способности линий связи:")
    #O.optimization(B, A, L, n)


    
if __name__ == "__main__":
    main()
