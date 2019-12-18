for n, p in map(lambda x: [list(map(lambda a: int(a), z)) if i == 0 else int(z) for i, z in enumerate(filter(lambda y: y, x.split(" ")))], open("round1Input.txt").read().splitlines()):
    # lol
    for index in range(p + 1, len(n)):
        n[index] = abs(n[index] - n[len(n) - p])
    for index in range(p):
        n[index] = (n[index] + n[len(n) - p]) % 10
    for val in n:
        print(val, end="")
    print()
