fh = open("file_demo.txt", 'w')

try:
    for a in range(1, 11):
        fh.write(f"Line: {a}\n")
finally:
    fh.close()
        
with open("file_demo.txt", 'a') as fh1:
    for a in range(11, 21):
        fh1.write(f"Line:: {a} \n")

with open("file_demo.txt", 'r') as rfh:
    # print(rfh.read(3))
    # print(rfh.readline())
    # print(rfh.readlines())
    print(rfh.readlines()[2])

fh2 = open("file_demo.txt", 'r')
fh3 = open("file1_demo.txt", 'w')

#fh3.write(fh2.readline())
for line in fh2:
    fh3.write(f"{str(line)}")

fh2.close()
fh3.close()

fh2 = open("file1_demo.txt", 'r')
fh3 = open("file2_demo.txt", 'w')

#print([line for line in fh2 if line.endswith('2')])
for line in fh2:
    print(line)
    if line.endswith('2 \n'):
        print("********* Inside if **********")
        fh3.write(line)

fh2.close()
fh3.close()
