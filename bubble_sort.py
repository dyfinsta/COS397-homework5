def bubble(int_list):
    a = list(int_list)   
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                # swap
                a[j], a[j + 1] = a[j + 1], a[j]

    return a
