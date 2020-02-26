def file_write(n):
    try:
        f=open("Files\Demo.txt","r")
        print(f.read())
    except:
        print("File does not exist ")

n=input("Enter the filename ")
file_write(n)