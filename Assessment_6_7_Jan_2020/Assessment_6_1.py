# Write a program which accepts file name from user and check whether that file exists in current directory or not.
# Input: Demo.txt
# Check whether Demo.txt exists or not.

def file_exist(n):
    try:
        f=open("Files\Demo.txt","a")
    except:
        print("File does not exist ")

n=input("Enter the filename ")
file_exist(n)

