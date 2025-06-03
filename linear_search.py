def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return f"{key} found in the index of {i}"
    return "not found"

a = [4, 6, 7, 420, 3, 20, 41, 81]
print(linear_search(a, 420))
print(linear_search(a, 5))
