


f=open("lesson.txt")
#reading the file
print(f.read())
f.close()

print (f.read_line())
with open("lesson2.txt",'w',encoding = 'utf-8')as f:
    f.write("This is my file\n")
    f.write("This file\n\n")
    f.write("Contains three lines\n")
print(f.read)

