def bubble_sort(a):
    for phase in range(1, len(a)):
        flag = 0
        for i in range(len(a) - phase):
            if a[i] > a[i + 1]:
                flag = 1
                a[i], a[i + 1] = a[i + 1], a[i]
        if flag == 0:
            break
    return a

a = [21, 18, 61, 45, 81, 10]
print(bubble_sort(a))
