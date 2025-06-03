def selection_sort(a):
    for phase in range(len(a) - 1):
        min_idx = phase
        for i in range(phase + 1, len(a)):
            if a[i] < a[min_idx]:
                min_idx = i
        if min_idx != phase:
            a[min_idx], a[phase] = a[phase], a[min_idx]
    return a

a = [21, 18, 61, 45, 81, 10]
print(selection_sort(a))
