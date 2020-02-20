io = [(list(y[0]), list(y[1])) for y in (x.split(" ") for x in open("round2Input.txt").read().splitlines())]

for z in io:
    while True:
        i = 0
        while i < min(len(z[0]), len(z[1])):
            if z[0][i] == z[1][i]:
                del z[0][i]
                del z[1][i]
            else:
                i += 1

        i = 0
        while i < min(len(z[0]), len(z[1])):
            if z[1][i] in z[0] and z[0].index(z[1][i]) == i + 1:
                z[0].pop(i)
                break
            elif z[0][i] in z[1] and z[1].index(z[0][i]) == i + 1:
                z[1].pop(i)
                break
            i += 1
        else:
            break

i = 0
for a, b in io:
    i += 1
    score = 0
    for x in zip(a, b):
        score += ord(x[0]) - ord(x[1])
    score += max(len(a), len(b)) - min(len(a), len(b))
    print(f"{i}. {score}")
