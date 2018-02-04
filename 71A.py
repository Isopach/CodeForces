for _ in range(input()):
    n=raw_input()
    if(len(n) <= 10):
        print n
    else:
        print n[0] + str(len(n)-2) + n[-1:] 