def quick_sort(a, s, e):
    if s < e:
        pivot_index = partition(a, s, e)
        quick_sort(a, s, pivot_index - 1)
        quick_sort(a, pivot_index + 1, e)

def partition(a, s, e):
    pivot = e
    l = e - 1
    while s <= l:
        while s <= l and a[s] < a[pivot]:
            s += 1
        while l >= 0 and a[l] >= a[pivot]:
            l -= 1
        if s < l:
            a[s], a[l] = a[l], a[s]
    a[s], a[pivot] = a[pivot], a[s]
    return s

a = [21, 18, 61, 45, 81, 10]
quick_sort(a, 0, len(a) - 1)
print(a)
