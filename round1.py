[print(*[*[(n[index] + n[len(n) - p]) % 10 for index in range(len(n) - p)], n[len(n) - p], *[abs(n[index] - n[len(n) - p]) for index in range(len(n) - p + 1, len(n))]], sep="") for n, p in map(lambda x: [list(map(lambda a: int(a), z)) if i == 0 else int(z) for i, z in enumerate(filter(lambda y: y, x.split(" ")))], open("round1Input.txt").read().splitlines())]
# lol
