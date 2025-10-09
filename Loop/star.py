def star_tree(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(2*n-2*i-1):
            print("*", end="")
        print()

n = 5
star_tree(n)
