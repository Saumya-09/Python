import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=string)
parser.add_argument("-e", "--enter", type=string)
args=parser.parse_args()
def file_copy(n):
    f=open("Files\Demo.txt", "r")
    f1=open("Files\Abc.txt", "w")
    l1=(f.read())
    f1.write(l1)

file_copy(args.enter, args.file)