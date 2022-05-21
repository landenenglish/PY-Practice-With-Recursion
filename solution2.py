# Write code for algorithm 2 below
def natural_numbers(x, i=1):
    # your code here
    if x >= i:
        print(i)
        natural_numbers(x, i+1)


natural_numbers(8)
