def bubble_sort(a):
    for phase in range(1, len(a)):
        for i in range(len(a) - phase):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a

a = [21, 18, 61, 45, 81, 10]
print(bubble_sort(a))
