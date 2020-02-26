def pattern(x):
    for i in range(0, x+1):
        for j in range(0, i):
            print(j+1, end=" ")
        print(end="\n")
if __name__ == '__main__':
    x = int(input())
    pattern(x)