''' reading a file  '''

f=open("new.txt") #<--- it  contins two parameters path of file then mode , mode can be r or w deafult is r , where r is read and w is write. There are many explained in mode.py
data=f.read()
f.close()
print(data)
