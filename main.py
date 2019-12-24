import calc as Calculate

def main():
    # --- Входные данные:
    # Количество узлов связи
    n = 20
    
    # Распределение абонентов по узлам связи (количество)
    N = [7916, 9084, 7295, 6958, 8765, 
         4897, 9029, 9484, 7254, 2479, 
         3384, 4371, 9992, 7318, 5953,
         1647, 5455, 7300, 4146, 5903]
    
    # Интенсивность исходящего трафика от каждого из узлов сети (yi)
    y = [0.1] # y0 = 0.1 Эрл


    # --- Рассчеты:
    # Интенсивность исходящего трафика от каждого из узлов сети:
    y = Calculate.calcTrafficNodeIntensity(N, y[0], n)
    print("1. Интенсивность исходящего трафика от каждого из узлов сети была вычислена.")

    # Коэффициенты распределения трафика по направлениям связи:
    k = Calculate.calcTrafficRatio(y, n)
    print("2. Коэффициенты распределения трафика по направлениям связи были вычислены.")
    
    # Матрица интенсивностей трафика в направлениях связи:
    Y = Calculate.calcTrafficMatrixIntensity(k, y, n)
    print("3. Матрица интенсивностей трафика в направлениях связи была вычислена.")
    
if __name__ == "__main__":
    main()
