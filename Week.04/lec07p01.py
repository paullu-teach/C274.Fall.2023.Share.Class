try:
    while True:
        x, y, z = map(float, input().strip().split())
        print(x, y, z, "--> max ", end='')
        max_val = max(x, y, z)
        print(max_val)
except EOFError:
    pass
