''' reading a file  '''

f=open("file.txt") #<--- it  contins two parameters path of file then mode , mode can be r or w deafult is r , where r is read and w is write. There are many explained in mode.py
data=f.read()
f.close()
print(data)

''' writng in a file /can create file using this w mode'''
emails = "alpha_test123@fakemail.com\nrandom_user567@nomail.net\nghostemail999@tempmail.org\nfake_address101@mockmail.xyz\ntrial_mailer456@noemail.com\nnonexistent987@randommail.net\ndummyemail2024@fakemail.org\ntesting_acc001@madeup.com\nsample_mail789@notreal.net\ntestuserX23@nowhere.xyz"
# here emails is a string conatianing some sample emails .

x=open("emails.txt","w") # here mode is w for writing in a file/ in my pc emials.txt doesnt exist but it will crerate / to insert in a existing file we use a mode where a is append
x.write(emails)
x.close()

# Readlines fn -using this we can print all lines in the form of a list

b=open("poem.txt")
line=b.readlines()
print(b,type(b))


# Readline fn -using this we can print all lines in the form of a list

line1=b.readline() # we can name var of your wish it isnt neccesary to give line1, the no of time function is called ,number of thaat line will print from  poem.txt
print(line1,type(line1))

line2=b.readline()
print(line2,type(line2))

line3=b.readline()
print(line3,type(line3))

line4=b.readline()
print(line4,type(line4))

line5=b.readline()
print(line5,type(line5))

line6=b.readline()
print(line6,type(line6)) # our txt doesnt contain 6th line but it will not raise a errror instead of that it will give a empty string 

print(line6=="")#this will give True

b.close()

# doing same thing by loop

c=open("file.txt")
line=c.readline()

while(line!=""):
    print(line)
    line=c.readline()
    
