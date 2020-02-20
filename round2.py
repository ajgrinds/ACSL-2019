for a, z in enumerate([(list(y[0]), list(y[1])) for y in (x.split(" ") for x in open("round2Input.txt").read().splitlines())]):
    while True:
        i = 0
        while i < min(len(z[0]), len(z[1])):
            if z[0][i] == z[1][i]:
                del z[0][i], z[1][i]
            else:
                i += 1

        for i in range(min(len(z[0]), len(z[1]))):
            if z[1][i] in z[0] and z[0].index(z[1][i]) == i + 1:
                z[0].pop(i)
                break
            elif z[0][i] in z[1] and z[1].index(z[0][i]) == i + 1:
                z[1].pop(i)
                break
        else:
            break

    print(f"{a + 1}. {sum(ord(x[0]) - ord(x[1]) for x in zip(z[0], z[1])) + max(len(z[0]), len(z[1])) - min(len(z[0]), len(z[1]))}")
