x= [64, 34, 25, 12, 22, 11, 90]
def order(x):
    n = len(x)
    for i in range(n):
        for j in range(0, n-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1],x[j]
    return x
sorted_array = order(x)
print("Sorted array:", sorted_array)
