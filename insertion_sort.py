def insertion_sort(a):
    for i in range(1, len(a)):
        j = i - 1
        temp = a[i]
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp
    return a

a = [21, 18, 61, 45, 81, 10]
print(insertion_sort(a))
