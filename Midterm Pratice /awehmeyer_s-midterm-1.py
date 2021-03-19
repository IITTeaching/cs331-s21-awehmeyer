def h(i):
    t = i
    result = []
    for j in range(2,t+1):
        if j > t:
                break
        while (t % j) == 0:
            t = t // j
            result.append(j)
    print(result)

h(128)