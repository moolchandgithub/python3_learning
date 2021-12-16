my_file = open("textfile.txt", "a")
my_file.write(str("This is a test file") + "\n")

my_file.close()

read_my_file = open("textfile.txt", "r")
a = read_my_file.read()
print (a)
read_my_file.close()

with open("tempfile.txt", "w") as my_temp:
    my_temp.write(str("first line") + "\n")
    my_temp.write(str("Second line") + "\n")
    my_temp.write(str("Third line") + "\n")

with open("tempfile.txt", "r") as read_temp:
    for a in read_temp.readlines():
        print(a)
