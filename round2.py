io = [(list(y[0]), list(y[1])) for y in (x.split(" ") for x in open("round2Input.txt").read().splitlines())]

i = 0
while i < min(len(io[0][0]), len(io[0][1])):
    if io[0][0][i] == io[0][1][i]:
        del io[0][0][i]
        del io[0][1][i]
    else:
        i += 1

print(io)
