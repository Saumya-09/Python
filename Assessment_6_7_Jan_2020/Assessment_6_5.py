def file_freq(n,str1):
    f = open("Files\Demo.txt", "r")
    words = f.read().split()

    count = 0
    key = []
    value = []

    for word in words:
        if not word in key:
            key.append(word)
            value.append(1)
        else:
            x=key.index(word)
            value[x]+=1

    print(dict(zip(key, value)))

n=input("Enter filename: ")
str1 = input("Enter the word : ")
file_freq(n,str1)