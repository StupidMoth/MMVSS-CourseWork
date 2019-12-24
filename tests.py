import calc as Calculate

y = Calculate.calcNodeIntensity([5, 10, 15], 0.1, 3)
print("y посчитанно: ")
for i in range(0, 3):
    print(y[i])
