''' With Statement '''

#generally we use 
f=open("file.txt")
data=f.read()
f.close()

#now we can write this same logic with with statement, traditonally we have to close file also and sometime we write bunch line we can miss it 

with open("file.txt") as f:
    print(f.read())
