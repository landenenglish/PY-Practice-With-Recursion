# Write code for algorithm 1 below

def count_down(n):
    if n > 0:
        print(n)
        count_down(n-1)


count_down(10)
