def pattern(x):
    for i in (0,x):
        for j in (0,x-1):
            print("*", end=" ")
    x-=1
    print(end="\n")
if __name__ == '__main__':
    x = int(input())
    pattern(x)