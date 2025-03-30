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
