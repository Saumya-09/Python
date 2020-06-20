import os
import sys
import hashlib

# Finding Duplicate Files
dirnam = input(" Enter path: ")

flis = []

for r, d, f in os.walk(dirnam):
    for file in f:
        flis.append(os.path.join(r, file))

for x in range(0, len(flis)):
    ffirst = open(flis[x], 'r')
    l1 = []
    for y in ffirst:
        l1.append(y)

    for z in range(x + 1, len(flis)):
        fsecond = open(flis[z], 'r')
        flag = 0

        l2 = []

        for y in fsecond:
            l2.append(y)

        if len(l1) != len(l2):
            continue
        else:

            for i in range(0, len(l1)):
                if l1[i] != l2[i]:
                    flag = 1
                    break
            if flag == 1:
                continue
            else:
                print()
                print(" Duplicate File:  ")
                ffirst.close()
                fsecond.close()
                # print(flis[z], end=" ")

                print(flis[x])
        fsecond.close()
    ffirst.close()

# Listing All the Files
print()
print()
path = input(" Enter path: ")

df_l = os.walk(path)
filesList = []

for (path, folder, files) in os.walk(path):
    filePaths = [os.path.join(path, file)
                 for file in files
                 ]
    filesList.extend(filePaths)
print(" ----------------------------------All the Files:  -----------------------------------------")
for file in filesList:
    print(">> ",file)


# define a function to calculate md5checksum for a given file:
def md5(f):
    """takes one file f as an argument and generates an md5checksum for that file"""
    return hashlib.md5(open(f, 'rb').read()).hexdigest()

for file in filesList:
    print()
    print(">> ",file)
    print("The checksum is:  ", md5(file))


# define our main function to remove Duplicates:
def rm_dup(path):
    """relies on the md5 function above to remove duplicate files"""
    if not os.path.isdir(path):  # make sure the given directory exists
        print('specified directory does not exist!')
    else:
        md5_dict = {}
        for root, dirs, files in os.walk(path):  # the os.walk function allows checking subdirectories too...
            for f in files:
                if not md5(os.path.join(root, f)) in md5_dict:
                    md5_dict.update({md5(os.path.join(root, f)): [os.path.join(root, f)]})
                else:
                    md5_dict[md5(os.path.join(root, f))].append(os.path.join(root, f))
        for key in md5_dict:
            while len(md5_dict[key]) > 1:
                for item in md5_dict[key]:
                    os.remove(item)
                    md5_dict[key].remove(item)
        print()
        print("------------------------------Done!---------------------------------")
        print("All the duplicate files removed")

if __name__ == '__main__':
    print()
    print()
    path = input(" Enter path:  ")
    print()
    rm_dup(path)




#Listing Files after removing duplicates
print()
print()
path = input(" Enter path:  ")

df_l = os.walk(path)
filesList = []

for (path, folder, files) in os.walk(path):
    filePaths = [os.path.join(path, file)
                 for file in files
                 ]
    filesList.extend(filePaths)
print()
print()
print(" All the remaining files after removing duplicates ")
print()
for file in filesList:
    print(">> ",file)
